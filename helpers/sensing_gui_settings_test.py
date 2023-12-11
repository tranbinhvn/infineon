from ifx_radar import ffi, lib

def setupConfiguration_of_sensing_gui(testo):
    power_down_config = ffi.new("Power_Down_Configuration_t*")
    adc_config = ffi.new("Adc_Bgt6x_Configuration_t*")
    chirp_timing = ffi.new("Chirp_Timing_t*")
    startup_timing = ffi.new("Startup_Timing_t*")
    frame_configuration = ffi.new("Frame_Definition_t*")
    frame_format = ffi.new("Frame_Format_t*")
    fmcw_configuration = ffi.new("Fmcw_Configuration_t*")
    baseband_configuration = ffi.new("Baseband_Configuration_t*")
    startup_delays = ffi.new("Startup_Delays_t*")
    duty_cycle_correction = ffi.new("Duty_Cycle_Correction_Settings_t*")
    anti_alias_settings = ffi.new("Anti_Alias_Filter_Settings_t*")
    pullup_configuration = ffi.new("Pullup_Resistor_Configuration_t*")


    #  /* switch to normal mode */
    try:
        testo.communication.RadarBGT60TRxx.enable_easy_mode(0)
        print("configuration on this EP is done OK.: RadarBGT60TRxx")
    except:
        print("configuration on this EP NOT done : RadarBGT60TRxx")


    #  /*******************/
    #  /* global settings */
    #  /*******************/

    #  /* configure deep sleep mode */
    power_down_config.enable_pll = 0
    power_down_config.enable_vco = 0
    power_down_config.enable_fdiv = 0
    power_down_config.enable_baseband = 0
    power_down_config.enable_rf = 0
    power_down_config.enable_madc = 0
    power_down_config.enable_madc_bandgap = 0
    power_down_config.enable_sadc = 0
    power_down_config.enable_sadc_bandgap = 0
    try:
        testo.communication.RadarBGT60TRxx.set_deep_sleep_configuration(power_down_config)
        print("configuration on this EP is done OK.: RadarBGT60TRxx")
    except:
        print("configuration on this EP NOT done : RadarBGT60TRxx")


    #  /* configure idle mode */
    power_down_config.enable_pll = 0
    power_down_config.enable_vco = 0
    power_down_config.enable_fdiv = 0
    power_down_config.enable_baseband = 0
    power_down_config.enable_rf = 0
    power_down_config.enable_madc = 0
    power_down_config.enable_madc_bandgap = 1
    power_down_config.enable_sadc = 0
    power_down_config.enable_sadc_bandgap = 0
    try:
        testo.communication.RadarBGT60TRxx.set_idle_configuration(power_down_config)
        print("configuration on this EP is done OK.: RadarBGT60TRxx")
    except:
        print("configuration on this EP NOT done : RadarBGT60TRxx")


    #  /* configure ADC */
    adc_config.samplerate_Hz = 1311475
    adc_config.sample_time = lib.RADAR_ADC_SAMPLETIME_50NS
    adc_config.tracking = lib.RADAR_ADCTRK_3_SUBCONVERSIONS
    adc_config.double_msb_time = 0
    adc_config.oversampling = lib.RADAR_ADC_OVERSAMPLING_OFF
    try:
        testo.communication.RadarBGT6x.set_adc_configuration(adc_config)
        print("configuration on this EP is done OK.: RadarBGT6x")
    except:
        print("configuration on this EP NOT done : RadarBGT6x")


    #  /* configure chirp timing */
    chirp_timing.pre_chirp_delay_100ps = 11250
    chirp_timing.post_chirp_delay_100ps = 14625
    chirp_timing.pa_delay_100ps = 30000
    chirp_timing.adc_delay_100ps = 31125
    try:
        testo.communication.RadarBGT60TRxx.set_chirp_timing(chirp_timing)
        print("configuration on this EP is done OK.: RadarBGT60TRxx")
    except:
        print("configuration on this EP NOT done : RadarBGT60TRxx")


    #  /* configure startup timing */
    startup_timing.wake_up_time_100ps = 9985375
    startup_timing.pll_settle_time_coarse_100ps = 450500
    startup_timing.pll_settle_time_fine_100ps = 70375
    try:
        testo.communication.RadarBGT60TRxx.set_startup_timing(startup_timing)
        print("configuration on this EP is done OK.: RadarBGT60TRxx")
    except:
        print("configuration on this EP NOT done : RadarBGT60TRxx")


    #  /* configure startup delays */
    startup_delays.bandgap_100ps = 48250
    startup_delays.madc_100ps = 32125
    startup_delays.pll_enable_100ps = 104250
    startup_delays.pll_divider_100ps = 8125
    try:
        testo.communication.RadarBGT60TRxxD.set_startup_delays(startup_delays)
        print("configuration on this EP is done OK.: RadarBGT60TRxxD")
    except:
        print("configuration on this EP NOT done : RadarBGT60TRxxD")


    #  /* configure BGT60TRxxD power settings */
    try:
        testo.communication.RadarBGT60TRxxD.set_fifo_power_mode(lib.EP_RADAR_BGT60TRXXD_FIFO_ALWAYS_ON)
        print("configuration on this EP is done OK.: RadarBGT60TRxxD")
    except:
        print("configuration on this EP NOT done : RadarBGT60TRxxD")
    try:
        testo.communication.RadarBGT60TRxxD.set_pad_driver_mode(lib.EP_RADAR_BGT60TRXXD_PAD_NORMAL)
        print("configuration on this EP is done OK.: RadarBGT60TRxxD")
    except:
        print("configuration on this EP NOT done : RadarBGT60TRxxD")


    #  /* configure clock frequency doubler */
    duty_cycle_correction.invert_input = 0
    duty_cycle_correction.adjust_in = 0
    duty_cycle_correction.adjust_out = 0
    try:
        testo.communication.RadarBGT60TRxxD.set_duty_cycle_correction(duty_cycle_correction)
        print("configuration on this EP is done OK.: RadarBGT60TRxxD")
    except:
        print("configuration on this EP NOT done : RadarBGT60TRxxD")


    #  /* configure pullup resistors */
    pullup_configuration.enable_spi_cs = 0
    pullup_configuration.enable_spi_clk = 0
    pullup_configuration.enable_spi_di = 0
    pullup_configuration.enable_spi_do = 0
    pullup_configuration.enable_spi_dio2 = 0
    pullup_configuration.enable_spi_dio3 = 0
    pullup_configuration.enable_irq = 0
    try:
        testo.communication.RadarBGT60TRxxE.set_pullup_resistor_configuration(pullup_configuration)
        print("configuration on this EP is done OK.: RadarBGT60TRxxE")
    except:
        print("configuration on this EP NOT done : RadarBGT60TRxxE")


    #  /* configure sensing */
    try:
        testo.communication.RadarBGT60TR11D.set_temperature_sens_enabled(0)
        print("configuration on this EP is done OK.: RadarBGT60TR11D")
    except:
        print("configuration on this EP NOT done : RadarBGT60TR11D")
    try:
        testo.communication.RadarBGT60TR11D.set_power_sens_enabled(0)
        print("configuration on this EP is done OK.: RadarBGT60TR11D")
    except:
        print("configuration on this EP NOT done : RadarBGT60TR11D")
    try:
        testo.communication.RadarBGT60TR11D.set_power_sens_delay(0)
        print("configuration on this EP is done OK.: RadarBGT60TR11D")
    except:
        print("configuration on this EP NOT done : RadarBGT60TR11D")


    #  /* configure frame */
    frame_configuration.shapes[0].num_repetitions = 1
    frame_configuration.shapes[0].following_power_mode = lib.EP_RADAR_BGT60TRXX_POW_GO_IDLE
    frame_configuration.shapes[0].post_delay_100ps = 100375
    frame_configuration.shapes[1].num_repetitions = 1
    frame_configuration.shapes[1].following_power_mode = lib.EP_RADAR_BGT60TRXX_POW_GO_IDLE
    frame_configuration.shapes[1].post_delay_100ps = 100375
    frame_configuration.shapes[2].num_repetitions = 0
    frame_configuration.shapes[2].following_power_mode = lib.EP_RADAR_BGT60TRXX_POW_GO_IDLE
    frame_configuration.shapes[2].post_delay_100ps = 4993250
    frame_configuration.shapes[3].num_repetitions = 0
    frame_configuration.shapes[3].following_power_mode = lib.EP_RADAR_BGT60TRXX_POW_GO_IDLE
    frame_configuration.shapes[3].post_delay_100ps = 4993250
    frame_configuration.shape_set.num_repetitions = 1
    frame_configuration.shape_set.following_power_mode = lib.EP_RADAR_BGT60TRXX_POW_GO_IDLE
    # frame_configuration.shape_set.post_delay_100ps = 119297500 # 80Hz
    frame_configuration.shape_set.post_delay_100ps = 10027010375 # 1Hz
    frame_configuration.num_frames = 0
    try:
        testo.communication.RadarBGT60TRxx.set_frame_definition(frame_configuration)
        print("configuration on this EP is done OK.: RadarBGT60TRxx")
    except:
        print("configuration on this EP NOT done : RadarBGT60TRxx")


    #  /***********/
    #  /* shape 1 */
    #  /***********/
    try:
        testo.communication.RadarBGT60TRxx.select_shape_to_configure(0, 0)
        print("configuration on this EP is done OK.: RadarBGT60TRxx")
    except:
        print("configuration on this EP NOT done : RadarBGT60TRxx")


    #  /* configure FMCW parameters */
    fmcw_configuration.direction = lib.EP_RADAR_FMCW_DIR_UPCHIRP_ONLY
    fmcw_configuration.lower_frequency_kHz = 58000000
    fmcw_configuration.upper_frequency_kHz = 61324303
    fmcw_configuration.tx_power = 31
    try:
        testo.communication.RadarFMCW.set_fmcw_configuration(fmcw_configuration)
        print("configuration on this EP is done OK.: RadarFMCW")
    except:
        print("configuration on this EP NOT done : RadarFMCW")


    #  /*********************/
    #  /* shape 1, up chirp */
    #  /*********************/
    try:
        testo.communication.RadarBGT60TRxx.select_shape_to_configure(0, 0)
        print("configuration on this EP is done OK.: RadarBGT60TRxx")
    except:
        print("configuration on this EP NOT done : RadarBGT60TRxx")


    #  /* configure frame format */
    frame_format.num_samples_per_chirp = 256
    frame_format.num_chirps_per_frame = 1
    frame_format.rx_mask = 15
    frame_format.eSignalPart = lib.EP_RADAR_BASE_SIGNAL_ONLY_I
    try:
        testo.communication.RadarBase.set_frame_format(frame_format)
        print("configuration on this EP is done OK.: RadarBase")
    except:
        print("configuration on this EP NOT done : RadarBase")


    #  /* configure TX antennas */
    try:
        testo.communication.RadarBGT6x.set_tx_mode(lib.EP_RADAR_BGT6X_MODE_TX_ONLY_TX1)
        # print("configuration on this EP is done OK.: RadarBGT6x")
        print("configuration on this EP is done OK.: RadarBGT6x Tx", lib.EP_RADAR_BGT6X_MODE_TX_ONLY_TX1)
    except:
        # print("configuration on this EP NOT done : RadarBGT6x")
        print("configuration on this EP NOT done : RadarBGT6x Tx", lib.EP_RADAR_BGT6X_MODE_TX_ONLY_TX1)


    #  /* configure additional delay at end of chirp */
    try:
        testo.communication.RadarBGT60TRxx.set_chirp_end_delay(251625)
        print("configuration on this EP is done OK.: RadarBGT60TRxx")
    except:
        print("configuration on this EP NOT done : RadarBGT60TRxx")


    #  /* configure analog baseband parameters */
    baseband_configuration.hp_gain_1 = lib.EP_RADAR_BGT6X_HP_GAIN_30DB
    baseband_configuration.hp_cutoff_1 = lib.EP_RADAR_BGT6X_HP_CUTOFF_20KHZ
    baseband_configuration.vga_gain_1 = lib.EP_RADAR_BGT6X_VGA_GAIN_10DB
    baseband_configuration.hp_gain_2 = lib.EP_RADAR_BGT6X_HP_GAIN_30DB
    baseband_configuration.hp_cutoff_2 = lib.EP_RADAR_BGT6X_HP_CUTOFF_20KHZ
    baseband_configuration.vga_gain_2 = lib.EP_RADAR_BGT6X_VGA_GAIN_10DB
    baseband_configuration.hp_gain_3 = lib.EP_RADAR_BGT6X_HP_GAIN_30DB
    baseband_configuration.hp_cutoff_3 = lib.EP_RADAR_BGT6X_HP_CUTOFF_20KHZ
    baseband_configuration.vga_gain_3 = lib.EP_RADAR_BGT6X_VGA_GAIN_10DB
    baseband_configuration.hp_gain_4 = lib.EP_RADAR_BGT6X_HP_GAIN_30DB
    baseband_configuration.hp_cutoff_4 = lib.EP_RADAR_BGT6X_HP_CUTOFF_20KHZ
    baseband_configuration.vga_gain_4 = lib.EP_RADAR_BGT6X_VGA_GAIN_10DB
    baseband_configuration.reset_timer_period_100ps = 15000
    try:
        testo.communication.RadarBGT6x.set_baseband_configuration(baseband_configuration)
        print("configuration on this EP is done OK.: RadarBGT6x")
    except:
        print("configuration on this EP NOT done : RadarBGT6x")


    #  /* configure anti alias filters */
    anti_alias_settings.frequency1 = lib.EP_RADAR_BGT60TRXXD_AAF_600kHz
    anti_alias_settings.frequency2 = lib.EP_RADAR_BGT60TRXXD_AAF_600kHz
    anti_alias_settings.frequency3 = lib.EP_RADAR_BGT60TRXXD_AAF_600kHz
    anti_alias_settings.frequency4 = lib.EP_RADAR_BGT60TRXXD_AAF_600kHz
    try:
        testo.communication.RadarBGT60TRxxD.set_anti_alias_filter_settings(anti_alias_settings)
        print("configuration on this EP is done OK.: RadarBGT60TRxxD")
    except:
        print("configuration on this EP NOT done : RadarBGT60TRxxD")


    #  /***********/
    #  /* shape 2 */
    #  /***********/
    try:
        testo.communication.RadarBGT60TRxx.select_shape_to_configure(1, 0)
        print("configuration on this EP is done OK.: RadarBGT60TRxx")
    except:
        print("configuration on this EP NOT done : RadarBGT60TRxx")


    #  /* configure FMCW parameters */
    fmcw_configuration.direction = lib.EP_RADAR_FMCW_DIR_UPCHIRP_ONLY
    fmcw_configuration.lower_frequency_kHz = 58000000
    fmcw_configuration.upper_frequency_kHz = 61324300
    fmcw_configuration.tx_power = 31
    try:
        testo.communication.RadarFMCW.set_fmcw_configuration(fmcw_configuration)
        print("configuration on this EP is done OK.: RadarFMCW")
    except:
        print("configuration on this EP NOT done : RadarFMCW")


    #  /*********************/
    #  /* shape 2, up chirp */
    #  /*********************/
    try:
        testo.communication.RadarBGT60TRxx.select_shape_to_configure(1, 0)
        print("configuration on this EP is done OK.: RadarBGT60TRxx")
    except:
        print("configuration on this EP NOT done : RadarBGT60TRxx")


    #  /* configure frame format */
    frame_format.num_samples_per_chirp = 256
    frame_format.num_chirps_per_frame = 1
    frame_format.rx_mask = 15
    frame_format.eSignalPart = lib.EP_RADAR_BASE_SIGNAL_ONLY_I
    try:
        testo.communication.RadarBase.set_frame_format(frame_format)
        print("configuration on this EP is done OK.: RadarBase")
    except:
        print("configuration on this EP NOT done : RadarBase")


    #  /* configure TX antennas */
    try:
        testo.communication.RadarBGT6x.set_tx_mode(lib.EP_RADAR_BGT6X_MODE_TX_ONLY_TX2)
        # print("configuration on this EP is done OK.: RadarBGT6x")
        print("configuration on this EP is done OK.: RadarBGT6x Tx", lib.EP_RADAR_BGT6X_MODE_TX_ONLY_TX2)
    except:
        # print("configuration on this EP NOT done : RadarBGT6x")
        print("configuration on this EP NOT done : RadarBGT6x Tx", lib.EP_RADAR_BGT6X_MODE_TX_ONLY_TX2)


    #  /* configure additional delay at end of chirp */
    try:
        testo.communication.RadarBGT60TRxx.set_chirp_end_delay(250625)
        print("configuration on this EP is done OK.: RadarBGT60TRxx")
    except:
        print("configuration on this EP NOT done : RadarBGT60TRxx")


    #  /* configure analog baseband parameters */
    baseband_configuration.hp_gain_1 = lib.EP_RADAR_BGT6X_HP_GAIN_30DB
    baseband_configuration.hp_cutoff_1 = lib.EP_RADAR_BGT6X_HP_CUTOFF_20KHZ
    baseband_configuration.vga_gain_1 = lib.EP_RADAR_BGT6X_VGA_GAIN_10DB
    baseband_configuration.hp_gain_2 = lib.EP_RADAR_BGT6X_HP_GAIN_30DB
    baseband_configuration.hp_cutoff_2 = lib.EP_RADAR_BGT6X_HP_CUTOFF_20KHZ
    baseband_configuration.vga_gain_2 = lib.EP_RADAR_BGT6X_VGA_GAIN_10DB
    baseband_configuration.hp_gain_3 = lib.EP_RADAR_BGT6X_HP_GAIN_30DB
    baseband_configuration.hp_cutoff_3 = lib.EP_RADAR_BGT6X_HP_CUTOFF_20KHZ
    baseband_configuration.vga_gain_3 = lib.EP_RADAR_BGT6X_VGA_GAIN_10DB
    baseband_configuration.hp_gain_4 = lib.EP_RADAR_BGT6X_HP_GAIN_30DB
    baseband_configuration.hp_cutoff_4 = lib.EP_RADAR_BGT6X_HP_CUTOFF_20KHZ
    baseband_configuration.vga_gain_4 = lib.EP_RADAR_BGT6X_VGA_GAIN_10DB
    baseband_configuration.reset_timer_period_100ps = 15000
    try:
        testo.communication.RadarBGT6x.set_baseband_configuration(baseband_configuration)
        print("configuration on this EP is done OK.: RadarBGT6x")
    except:
        print("configuration on this EP NOT done : RadarBGT6x")


    #  /* configure anti alias filters */
    anti_alias_settings.frequency1 = lib.EP_RADAR_BGT60TRXXD_AAF_600kHz
    anti_alias_settings.frequency2 = lib.EP_RADAR_BGT60TRXXD_AAF_600kHz
    anti_alias_settings.frequency3 = lib.EP_RADAR_BGT60TRXXD_AAF_600kHz
    anti_alias_settings.frequency4 = lib.EP_RADAR_BGT60TRXXD_AAF_600kHz
    try:
        testo.communication.RadarBGT60TRxxD.set_anti_alias_filter_settings(anti_alias_settings)
        print("configuration on this EP is done OK.: RadarBGT60TRxxD")
    except:
        print("configuration on this EP NOT done : RadarBGT60TRxxD")
