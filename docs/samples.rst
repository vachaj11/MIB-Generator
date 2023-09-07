C-code samples
================

Here you will find examples of how various objects which are recognised by this program can be stated in the inputted C code.

.. highlight:: c

TM packets
----------

This program first looks for the TM ``.c`` file, in which it expects to see two things (in this order):

1. An array defining all the apids to be used: ::

	const uint16_t apidNum[APID_LAST] =
	{
	    [APID_DAPU] = 1265,
	    [APID_FGM] = 1231,
	    [APID_DISC] = 1232,
	    [APID_COMPLIMENT] = 1233,
	    [APID_LEES] = 1234,
	    [APID_SCIENA] = 1235,
	};
	
   This is then used similarly to an ``enum`` to match apid numbers to packets.

2. An array of structures defining all TM packets types to be interpreted by their name, apid, type and subtype. For e.g. two packet types: ::

	const struct TmProperties tmProperties[TM_LAST] =
	{
	    {
		.type = TM_ACK1,
		.apid = APID_DAPU,
		.serviceType = 1,
		.serviceSubType = 1      
	    },
	    {
		.type = TM_NACK2,
		.apid = APID_DAPU,
		.serviceType = 1,
		.serviceSubType = 2        
	    }
	};

The program then turns to the TM ``.h`` file. There it first resolves parts of pre-processor logic to figure out what parts of the code to omit
and then starts looking at what C-objects are included and what they represent. This is a multi step process so I won't go into full detail here,
hopefully it will be sufficient to provide some examples.

1. All ``enum`` objects and ``#define`` macros are added to one giant dictionary which is then used to evaluate stuff. E.g. if the following
   lines are in the file: ::
  
	#define CRC_SIZE 2

	// Telemetry packet definition
	enum TmType
	{
	    TM_ACK1, 
	    TM_NACK2,
	    TM_ACK7,
	    TM_NACK8
	};
	
   the result will be the following Python evaluation dictionary:

   .. code-block:: python
  	
  	{"CRC_SIZE": 2, "TM_ACK1": 0, "TM_NACK2": 1, "TM_ACK7": 2, "TM_NACK8": 3}
  	
2. All instances of ``struct`` preceded by an appropriate comment which includes json5 syntax with the  ``"pack_type"`` entry can be interpreted as 
   a declaration of a packet structure. For instance here is defined a packet of type ``"TM_DISC"``: ::
   
	/*{ packet: "TM", pack_type: "TM_DISC", "base_par_index": 59200, prefix: "LWT",
	    text_id: "LWY_SCI0002", spid: 75032, desc: "TM Acceptance success", Mnemonic: "ACK_jez" }*/
	struct PACKED TmDiscFull
	{
	    uint16_t sid; /*{ sid: true, enum: "sci_sids", desc: "DISC_B2_FULL",  const_value: "SID_SCI_DISC_FULL" }*/
	    uint8_t time[7]; /*{ "desc": "Acquisition time", "type": "CUCTIME4_3" }*/ 
	    uint8_t compression:5; ///< 0 not compression
	    uint8_t numBlocks; /*{ "desc": "Number of full blocks", vpd: "count" }*/
	    // NOTE: Here you need to create a nested VPD block
	    struct DiscFullBlock dataBlocks[4]; /*{ "desc": "DISC data", vpd: "data" , cal: "voltage_cal"}*/;     
	};
	
   Lots of things can be seen here. First, any comment which is of the type ``/*{ ... }*/`` is taken as an interpretable comment and will be assumed
   to contain a json5 dictionary (where as the comment ``// NOTE...`` will be ignored). In terms of the comment directly preceding the ``struct``, 
   this is taken to provide additional information about the packet. Here:
   
   	#. ``packet`` - This describes whether the packet is telemetry or telecommand. It is not used anywhere.
   	#. ``pack_type`` - This describes packet type of this packet. It is used to match the packet to appropriate type, subtype and apid numbers
   	   as declared in the TM ``.c`` file.
   	#. ``base_par_index`` and ``prefix`` - This is a basis on which the parameters inside the packet will be assigned unique names. E.g. here
   	   the parameter named in C as ``compression`` will be assigned name ``"LWT59202"``.
   	#. ``text_id`` - A name that will be used for this packet in the MIB database.
   	#. ``spid`` - Spid of this packet.
   	#. ``desc`` - Description of the purpose/task of this packet.
   	#. ``Mnemonic`` - Used for more systematic naming scheme. So far not implemented.
   	
   Comments are also used for each of the entries/parameters to states their additional properties. Here:
   
   	#. ``sid`` - This means that this entry is an additional identification field for this packet, with its value defined in the ``const_value`` entry.
   	#. ``type`` - This defines the type of the parameter in addition to its type in C and information on whether it is an array.
   	#. ``desc`` - Description of the entry/parameter.
   	#. ``vpd`` - This describes that the parameter is part of variable packet definition. Three values are possible here:
   	
   		* ``"fixed"`` - in which case the parameter is taken to repeat a fixed amount of times (this amount being described by its array).
   		* ``"count"`` - in which case the parameter defines the number of times the parameter/groups of parameters following it will be repeated.
   		* ``"data"`` - in which case the parameter is the one being repeated (or part of such group).
	#. ``cal`` - This states whether and what calibration should be used for this parameter.
	
   Also notice here that one of the entries is itself a ``struct``. The code will "unpack" this ``struct`` (if it finds its declaration) by including all
   its entries inside this packet (in this case marking them as a repeating vpd group).
   
   Custom bit sizes are also implemented so the entry ``"compression"`` here will only be taken to have length of 5 bits.
   
3. Calibration of TM parameters can be defined in both the Tm and TcTm ``.h`` files and can be stated in various ways:

   **Polynomial calibrations** are expected to have the following format: ::
   
	/*{
	    "cal_def": "second_cal", "cal_ident": "CAL00004", "desc": "Time to seconds calibration",
	    "mcf": {"a0": 0, "a1": 0.1, "a2": 0, "a3": 0}
	}*/
	
   where the nature of the calibration is recognised by the ``"mcf"`` key and the entries in the sub-dictionary define the polynomial coefficients.
   
   **Logarithmic calibrations** are expected to have the following format: ::
   
	/*{
	    "cal_def": brightness_cal", "cal_ident": "CAL00008", "desc": "Brightness calibration",
	    "lgf": {"a0": 1, "a1": 2.1, "a2": 0, "a3": 6.2}
	}*/
	
   where the nature of the calibration is recognised by the ``"lgf"`` key and the entries in the sub-dictionary define the calibration coefficients.
   
   **Textual calibrations** can be formatted in two ways, either wholly through a comment or through an ``enum``: ::
   
	/*{
	    cal_def: "load_levels", cal_ident: "CAL00003", "desc": "Voltage calibration",
	    text_cal: { min: 0, max: 10, lookup: [
		{ val: 1, text: "Low" },
		{ val: 2, text: "Less low" },
		{ from: 3, to: 9, text: "Higher" },
	    ]}
	}*/

   or ::
   
	/*{ "enum": "error_codes", "cal_ident": "CAL00002", "desc": "Error code lookup" }*/
	enum ErrorCode {
	    DAPU_ERROR_1 = 1, /*{ text: "DPU Error 1"}*/
	    DAPU_ERROR_2 = 2, /*{ text: "DPU Error 2"}*/
	    DAPU_ERROR_3 = 3  /*{ text: "DPU Error 3"}*/
	};
	
   In the former case the calibration type is recognised by the ``"text_cal"``, in the latter by the ``"enum"``.
   
   **Numerical calibrations** should be of the format: ::
   
	/*{
	    cal_def: "sinus", cal_ident: "CAL00007", "desc": "Sinus curve",
	    num_cal: [[0.0, 0.0], [0.44, 0.43], [0.89, 0.78], [1.34, 0.97], [1.79, 0.97], [2.24, 0.78], [2.69, 0.43]],
	}*/
	
   Recognised by the ``"num_cal"`` key.

TC packets
----------

The case with TC packets/commands is mostly similar to TM packets with the main difference being that in their case, there is no Tc ``.c`` file, so the command
definitions are searched for directly in the Tc ``.h`` file. Three various things (apart from enums and preprocessor stuff which is analogous to TM packets)
can be recognised in this file:

1. TC header/s. Are recognised by their names, etc. Only basic analysis is performed on them and overall this side of things is not very much implemented.
   Example header (not much interesting to see here): ::
   
	struct PACKED TcHead
	{
	    struct Id id;
	    struct Sequence sequence;
	    uint16_t length;
	    // End of Packet primary header, start of packet secondary header
	    unsigned int version :4; ///< 1 for ECSS-E-70-41A, 2 for ECSS-E-ST-70-41C
	    unsigned int ackFlags:4; ///< B3 acceptence, B2 execution, B1 progress, B0 completion acknowledgment requested
	    uint8_t serviceType; ///< Service type
	    uint8_t subType; ///< Service subtype
	    uint16_t sourceID; ///< TC source
	    uint8_t spare; /*{ desc: "spare", const_value: 0 }*/
	};
	
2. Command definition. This mostly conforms to what was said about the TM packet definitions above. Example Tc command defined with ``struct`` can be: ::

	/*{ packet: "TC", service: 3, sub: 6, "base_par_index": 66400, prefix: "LWP",
	    text_id: "LWC00306", desc: "TC Disable HK", Mnemonic: "ACK_jez", cvs: [17001] }*/
	struct TcHkDisable
	{
	    struct SpwHead spwHead; // ignore this for MIB - common SpW header
	    struct TcHead tcHead;   // ignore this for MIB - common PUS header
	    uint16_t numPars;   /*{ cdf: "count", desc : "Number of Sids", max : "MAX_BLOCKS_IN_PUS", min : 1}*/
	    uint16_t hkSid[1];  /*{ cdf: "data", enum: "hk_sids", desc : "HK SID", min : "SID_HK_REPORT_DAPU",
		                    max: "SID_HK_REPORT_PSU",  default: "SID_HK_REPORT_DAPU"}*/
	    uint8_t spare; /*{ desc: "spare", const_value: 0 }*/
	};

   Unlike with with TM however:
   
   	1. ``sub`` and ``service`` - state what is the service type and subtype of the packet that this command is send by
   	2. ``cvs`` - defines what verifications should be used for this command (if this is not stated, then the defaults are used)
   	
   And for parameters:
   	
   	1. ``cdf`` - defines repetition of some parameter in this command in a way analogous to ``vpd`` in TM packets.
   	2. ``min`` and ``max`` - define a range check to be applied to the parameter.
   	3. ``default`` - define a default value to be used for the parameter.
   	4. ``const_value`` - used like this with the ``spare`` entry, it defines an entry which is a fixed area in the command.
   	5. ``enum`` - here means that decalibration of the specified name should be used for the parameter.
   	
3. Decalibrations and verifications. **Decalibrations** in case of Tc commands are analogous to textual calibrations for Tm packets defined through 
   ``enum``. They can look e.g. like: ::
   
	/*{ "enum": "on_off", "dec_ident": "DEC00005", "cal_ident": "CAL00005", "cal_desc": "on/off" }*/
	enum OnOff {
	    ONOFF_OFF = 0, /*{ text: "Off"}*/
	    ONOFF_ON = 1  /*{ text: "On"}*/    
	};
   
   The decalibration is recognised through the ``"dec_ident"`` key in the comment. Since ``"cal_ident"`` is also a key, this structure also defines
   a Tm textual calibration at the same time.
   
   **Verifications** are defined through a single isolated comments. They have e.g. the following form: ::
   
	// Verification definitions to generate CVS file: CVS_SOURCE is always R, CVS start is 0
	/*{ cvs_def: 17001, cvs_type: "A", cvs_interval: 60, default: true }*/
	/*{ cvs_def: 17002, cvs_type: "C", cvs_interval: 60, default: true }*/

   Here the parameters inside are passed to the cvs mib table apart from ``default`` which is used to determine whether the given verification should
   be applied by default automatically to commands which do not have specific set of verifications assigned to them.
