# Embedded file name: /usr/lib/enigma2/python/Components/Converter/ASBlueExtraInfo.py
from enigma import iServiceInformation, iPlayableService
from Components.Converter.Converter import Converter
from Components.Element import cached
from Components.config import config
from Tools.Transponder import ConvertToHumanReadable
from Tools.GetEcmInfo import GetEcmInfo
from Poll import Poll

def addspace(text):
    if text:
        text += '  '
    return text


class AMBExtraInfo(Poll, Converter, object):

    def __init__(self, type):
        Converter.__init__(self, type)
        Poll.__init__(self)
        self.type = type
        self.poll_interval = 1000
        self.poll_enabled = True
        self.caid_data = (('0x100',
          '0x1ff',
          'Seca',
          'S',
          True),
         ('0x500',
          '0x5ff',
          'Via',
          'V',
          True),
         ('0x600',
          '0x6ff',
          'Irdeto',
          'I',
          True),
         ('0x900',
          '0x9ff',
          'NDS',
          'Nd',
          True),
         ('0xb00',
          '0xbff',
          'Conax',
          'Co',
          True),
         ('0xd00',
          '0xdff',
          'CryptoW',
          'Cw',
          True),
         ('0xe00',
          '0xeff',
          'PowerVU',
          'P',
          False),
         ('0x1700',
          '0x17ff',
          'Beta',
          'B',
          True),
         ('0x1800',
          '0x18ff',
          'Nagra',
          'N',
          True),
         ('0x2600',
          '0x2600',
          'Biss',
          'Bi',
          False),
         ('0x4ae0',
          '0x4ae1',
          'Dre',
          'D',
          False),
         ('0x4aee',
          '0x4aee',
          'BulCrypt',
          'B1',
          False),
         ('0x5581',
          '0x5581',
          'BulCrypt',
          'B2',
          False))
        self.ca_table = (('CryptoCaidSecaAvailable', 'S', False),
         ('CryptoCaidViaAvailable', 'V', False),
         ('CryptoCaidIrdetoAvailable', 'I', False),
         ('CryptoCaidNDSAvailable', 'Nd', False),
         ('CryptoCaidConaxAvailable', 'Co', False),
         ('CryptoCaidCryptoWAvailable', 'Cw', False),
         ('CryptoCaidPowerVUAvailable', 'P', False),
         ('CryptoCaidBetaAvailable', 'B', False),
         ('CryptoCaidNagraAvailable', 'N', False),
         ('CryptoCaidBissAvailable', 'Bi', False),
         ('CryptoCaidDreAvailable', 'D', False),
         ('CryptoCaidBulCrypt1Available', 'B1', False),
         ('CryptoCaidBulCrypt2Available', 'B2', False),
         ('CryptoCaidSecaSelected', 'S', True),
         ('CryptoCaidViaSelected', 'V', True),
         ('CryptoCaidIrdetoSelected', 'I', True),
         ('CryptoCaidNDSSelected', 'Nd', True),
         ('CryptoCaidConaxSelected', 'Co', True),
         ('CryptoCaidCryptoWSelected', 'Cw', True),
         ('CryptoCaidPowerVUSelected', 'P', True),
         ('CryptoCaidBetaSelected', 'B', True),
         ('CryptoCaidNagraSelected', 'N', True),
         ('CryptoCaidBissSelected', 'Bi', True),
         ('CryptoCaidDreSelected', 'D', True),
         ('CryptoCaidBulCrypt1Selected', 'B1', True),
         ('CryptoCaidBulCrypt2Selected', 'B2', True))
        self.ecmdata = GetEcmInfo()
        self.feraw = self.fedata = self.updateFEdata = None
        return

    def getCryptoInfo(self, info):
        if info.getInfo(iServiceInformation.sIsCrypted) == 1:
            data = self.ecmdata.getEcmData()
            self.current_source = data[0]
            self.current_caid = data[1]
            self.current_provid = data[2]
            self.current_ecmpid = data[3]
        else:
            self.current_source = ''
            self.current_caid = '0'
            self.current_provid = '0'
            self.current_ecmpid = '0'

    def createCryptoBar(self, info):
        res = ''
        available_caids = info.getInfoObject(iServiceInformation.sCAIDs)
        for caid_entry in self.caid_data:
            if int(self.current_caid, 16) >= int(caid_entry[0], 16) and int(self.current_caid, 16) <= int(caid_entry[1], 16):
                color = '\\c0000??00'
            else:
                color = '\\c007?7?7?'
                try:
                    for caid in available_caids:
                        if caid >= int(caid_entry[0], 16) and caid <= int(caid_entry[1], 16):
                            color = '\\c00????00'

                except:
                    pass

            if color != '\\c007?7?7?' or caid_entry[4]:
                if res:
                    res += ' '
                res += color + caid_entry[3]

        res += '\\c00??????'
        return res

    def createCryptoSeca(self, info):
        available_caids = info.getInfoObject(iServiceInformation.sCAIDs)
        if int(self.current_caid, 16) >= int('0x100', 16) and int(self.current_caid, 16) <= int('0x1ff', 16):
            color = '\\c004c7d3f'
        else:
            color = '\\c009?9?9?'
            try:
                for caid in available_caids:
                    if caid >= int('0x100', 16) and caid <= int('0x1ff', 16):
                        color = '\\c00eeee00'

            except:
                pass

        res = color + 'S'
        res += '\\c00??????'
        return res

    def createCryptoVia(self, info):
        available_caids = info.getInfoObject(iServiceInformation.sCAIDs)
        if int(self.current_caid, 16) >= int('0x500', 16) and int(self.current_caid, 16) <= int('0x5ff', 16):
            color = '\\c004c7d3f'
        else:
            color = '\\c009?9?9?'
            try:
                for caid in available_caids:
                    if caid >= int('0x500', 16) and caid <= int('0x5ff', 16):
                        color = '\\c00eeee00'

            except:
                pass

        res = color + 'V'
        res += '\\c00??????'
        return res

    def createCryptoIrdeto(self, info):
        available_caids = info.getInfoObject(iServiceInformation.sCAIDs)
        if int(self.current_caid, 16) >= int('0x600', 16) and int(self.current_caid, 16) <= int('0x6ff', 16):
            color = '\\c004c7d3f'
        else:
            color = '\\c009?9?9?'
            try:
                for caid in available_caids:
                    if caid >= int('0x600', 16) and caid <= int('0x6ff', 16):
                        color = '\\c00eeee00'

            except:
                pass

        res = color + 'I'
        res += '\\c00??????'
        return res

    def createCryptoNDS(self, info):
        available_caids = info.getInfoObject(iServiceInformation.sCAIDs)
        if int(self.current_caid, 16) >= int('0x900', 16) and int(self.current_caid, 16) <= int('0x9ff', 16):
            color = '\\c004c7d3f'
        else:
            color = '\\c009?9?9?'
            try:
                for caid in available_caids:
                    if caid >= int('0x900', 16) and caid <= int('0x9ff', 16):
                        color = '\\c00eeee00'

            except:
                pass

        res = color + 'NDS'
        res += '\\c00??????'
        return res

    def createCryptoConax(self, info):
        available_caids = info.getInfoObject(iServiceInformation.sCAIDs)
        if int(self.current_caid, 16) >= int('0xb00', 16) and int(self.current_caid, 16) <= int('0xbff', 16):
            color = '\\c004c7d3f'
        else:
            color = '\\c009?9?9?'
            try:
                for caid in available_caids:
                    if caid >= int('0xb00', 16) and caid <= int('0xbff', 16):
                        color = '\\c00eeee00'

            except:
                pass

        res = color + 'CO'
        res += '\\c00??????'
        return res

    def createCryptoCryptoW(self, info):
        available_caids = info.getInfoObject(iServiceInformation.sCAIDs)
        if int(self.current_caid, 16) >= int('0xd00', 16) and int(self.current_caid, 16) <= int('0xdff', 16):
            color = '\\c004c7d3f'
        else:
            color = '\\c009?9?9?'
            try:
                for caid in available_caids:
                    if caid >= int('0xd00', 16) and caid <= int('0xdff', 16):
                        color = '\\c00eeee00'

            except:
                pass

        res = color + 'CW'
        res += '\\c00??????'
        return res

    def createCryptoPowerVU(self, info):
        available_caids = info.getInfoObject(iServiceInformation.sCAIDs)
        if int(self.current_caid, 16) >= int('0xe00', 16) and int(self.current_caid, 16) <= int('0xeff', 16):
            color = '\\c004c7d3f'
        else:
            color = '\\c009?9?9?'
            try:
                for caid in available_caids:
                    if caid >= int('0xe00', 16) and caid <= int('0xeff', 16):
                        color = '\\c00eeee00'

            except:
                pass

        res = color + 'P'
        res += '\\c00??????'
        return res

    def createCryptoBeta(self, info):
        available_caids = info.getInfoObject(iServiceInformation.sCAIDs)
        if int(self.current_caid, 16) >= int('0x1700', 16) and int(self.current_caid, 16) <= int('0x17ff', 16):
            color = '\\c004c7d3f'
        else:
            color = '\\c009?9?9?'
            try:
                for caid in available_caids:
                    if caid >= int('0x1700', 16) and caid <= int('0x17ff', 16):
                        color = '\\c00eeee00'

            except:
                pass

        res = color + 'B'
        res += '\\c00??????'
        return res

    def createCryptoNagra(self, info):
        available_caids = info.getInfoObject(iServiceInformation.sCAIDs)
        if int(self.current_caid, 16) >= int('0x1800', 16) and int(self.current_caid, 16) <= int('0x18ff', 16):
            color = '\\c004c7d3f'
        else:
            color = '\\c009?9?9?'
            try:
                for caid in available_caids:
                    if caid >= int('0x1800', 16) and caid <= int('0x18ff', 16):
                        color = '\\c00eeee00'

            except:
                pass

        res = color + 'N'
        res += '\\c00??????'
        return res

    def createCryptoBiss(self, info):
        available_caids = info.getInfoObject(iServiceInformation.sCAIDs)
        if int(self.current_caid, 16) >= int('0x2600', 16) and int(self.current_caid, 16) <= int('0x26ff', 16):
            color = '\\c004c7d3f'
        else:
            color = '\\c009?9?9?'
            try:
                for caid in available_caids:
                    if caid >= int('0x2600', 16) and caid <= int('0x26ff', 16):
                        color = '\\c00eeee00'

            except:
                pass

        res = color + 'BI'
        res += '\\c00??????'
        return res

    def createCryptoDre(self, info):
        available_caids = info.getInfoObject(iServiceInformation.sCAIDs)
        if int(self.current_caid, 16) >= int('0x4ae0', 16) and int(self.current_caid, 16) <= int('0x4ae1', 16):
            color = '\\c004c7d3f'
        else:
            color = '\\c009?9?9?'
            try:
                for caid in available_caids:
                    if caid >= int('0x4ae0', 16) and caid <= int('0x4ae1', 16):
                        color = '\\c00eeee00'

            except:
                pass

        res = color + 'DC'
        res += '\\c00??????'
        return res

    def createCryptoSpecial(self, info):
        caid_name = 'FTA'
        try:
            for caid_entry in self.caid_data:
                if int(self.current_caid, 16) >= int(caid_entry[0], 16) and int(self.current_caid, 16) <= int(caid_entry[1], 16):
                    caid_name = caid_entry[2]
                    break

            return caid_name + ':%04x:%04x:%04x:%04x' % (int(self.current_caid, 16),
             int(self.current_provid, 16),
             info.getInfo(iServiceInformation.sSID),
             int(self.current_ecmpid, 16))
        except:
            pass

        return ''

    def createResolution(self, info):
        xres = info.getInfo(iServiceInformation.sVideoWidth)
        if xres == -1:
            return ''
        yres = info.getInfo(iServiceInformation.sVideoHeight)
        mode = ('i', 'p', '')[info.getInfo(iServiceInformation.sProgressive)]
        fps = str((info.getInfo(iServiceInformation.sFrameRate) + 500) / 1000)
        return str(xres) + 'x' + str(yres) + mode + fps

    def createVideoCodec(self, info):
        return ('MPEG2', 'MPEG4', 'MPEG1', 'MPEG4-II', 'VC1', 'VC1-SM', '')[info.getInfo(iServiceInformation.sVideoType)]

    def createPIDInfo(self, info):
        vpid = info.getInfo(iServiceInformation.sVideoPID)
        apid = info.getInfo(iServiceInformation.sAudioPID)
        pcrpid = info.getInfo(iServiceInformation.sPCRPID)
        sidpid = info.getInfo(iServiceInformation.sSID)
        if vpid < 0:
            vpid = 0
        if apid < 0:
            apid = 0
        if pcrpid < 0:
            pcrpid = 0
        if sidpid < 0:
            sidpid = 0
        return 'Pids:%04d:%04d:%04d:%05d' % (vpid,
         apid,
         pcrpid,
         sidpid)

    def createTransponderInfo(self, fedata, feraw):
        return addspace(self.createTunerSystem(fedata)) + addspace(self.createFrequency(fedata)) + addspace(self.createPolarization(fedata)) + addspace(self.createSymbolRate(fedata)) + addspace(self.createFEC(fedata)) + addspace(self.createModulation(fedata)) + self.createOrbPos(feraw)

    def createFrequency(self, fedata):
        frequency = fedata.get('frequency')
        if frequency:
            return str(frequency / 1000)
        return ''

    def createSymbolRate(self, fedata):
        symbolrate = fedata.get('symbol_rate')
        if symbolrate:
            return str(symbolrate / 1000)
        return ''

    def createPolarization(self, fedata):
        polarization = fedata.get('polarization_abbreviation')
        if polarization:
            return polarization
        return ''

    def createFEC(self, fedata):
        fec = fedata.get('fec_inner')
        if fec:
            return fec
        return ''

    def createModulation(self, fedata):
        modulation = fedata.get('modulation')
        if modulation:
            return modulation
        return ''

    def createTunerType(self, feraw):
        tunertype = feraw.get('tuner_type')
        if tunertype:
            return tunertype
        return ''

    def createTunerSystem(self, fedata):
        tunersystem = fedata.get('system')
        if tunersystem:
            return tunersystem
        return ''

    def createOrbPos(self, feraw):
        orbpos = feraw.get('orbital_position')
        if orbpos > 1800:
            return str(float(3600 - orbpos) / 10.0) + '\xc2\xb0 W'
        if orbpos > 0:
            return str(float(orbpos) / 10.0) + '\xc2\xb0 E'
        return ''

    def createOrbPosOrTunerSystem(self, fedata, feraw):
        orbpos = self.createOrbPos(feraw)
        if orbpos != '':
            return orbpos
        return self.createTunerSystem(fedata)

    def createTransponderName(self, feraw):
        orb_pos = ''
        orbpos = feraw.get('orbital_position')
        if orbpos > 1800:
            if orbpos == 3590:
                orb_pos = 'Thor/Intelsat'
            elif orbpos == 3560:
                orb_pos = 'Amos (4'
            elif orbpos == 3550:
                orb_pos = 'Atlantic Bird'
            elif orbpos == 3530:
                orb_pos = 'Nilesat/Atlantic Bird'
            elif orbpos == 3520:
                orb_pos = 'Atlantic Bird'
            elif orbpos == 3475:
                orb_pos = 'Atlantic Bird'
            elif orbpos == 3460:
                orb_pos = 'Express'
            elif orbpos == 3450:
                orb_pos = 'Telstar'
            elif orbpos == 3420:
                orb_pos = 'Intelsat'
            elif orbpos == 3380:
                orb_pos = 'Nss'
            elif orbpos == 3355:
                orb_pos = 'Intelsat'
            elif orbpos == 3325:
                orb_pos = 'Intelsat'
            elif orbpos == 3300:
                orb_pos = 'Hispasat'
            elif orbpos == 3285:
                orb_pos = 'Intelsat'
            elif orbpos == 3170:
                orb_pos = 'Intelsat'
            elif orbpos == 3150:
                orb_pos = 'Intelsat'
            elif orbpos == 3070:
                orb_pos = 'Intelsat'
            elif orbpos == 3045:
                orb_pos = 'Intelsat'
            elif orbpos == 3020:
                orb_pos = 'Intelsat 9'
            elif orbpos == 2990:
                orb_pos = 'Amazonas'
            elif orbpos == 2900:
                orb_pos = 'Star One'
            elif orbpos == 2880:
                orb_pos = 'AMC 6 (72'
            elif orbpos == 2875:
                orb_pos = 'Echostar 6'
            elif orbpos == 2860:
                orb_pos = 'Horizons'
            elif orbpos == 2810:
                orb_pos = 'AMC5'
            elif orbpos == 2780:
                orb_pos = 'NIMIQ 4'
            elif orbpos == 2690:
                orb_pos = 'NIMIQ 1'
            elif orbpos == 3592:
                orb_pos = 'Thor/Intelsat'
            elif orbpos == 2985:
                orb_pos = 'Echostar 3,12'
            elif orbpos == 2830:
                orb_pos = 'Echostar 8'
            elif orbpos == 2630:
                orb_pos = 'Galaxy 19'
            elif orbpos == 2500:
                orb_pos = 'Echostar 10,11'
            elif orbpos == 2502:
                orb_pos = 'DirectTV 5'
            elif orbpos == 2410:
                orb_pos = 'Echostar 7 Anik F3'
            elif orbpos == 2391:
                orb_pos = 'Galaxy 23'
            elif orbpos == 2390:
                orb_pos = 'Echostar 9'
            elif orbpos == 2412:
                orb_pos = 'DirectTV 7S'
            elif orbpos == 2310:
                orb_pos = 'Galaxy 27'
            elif orbpos == 2311:
                orb_pos = 'Ciel 2'
            elif orbpos == 2120:
                orb_pos = 'Echostar 2'
            else:
                orb_pos = str(float(3600 - orbpos) / 10.0) + 'W'
        elif orbpos > 0:
            if orbpos == 192:
                orb_pos = 'Astra 1F'
            elif orbpos == 130:
                orb_pos = 'Hot Bird 6,7A,8'
            elif orbpos == 235:
                orb_pos = 'Astra 1E'
            elif orbpos == 1100:
                orb_pos = 'BSat 1A,2A'
            elif orbpos == 1101:
                orb_pos = 'N-Sat 110'
            elif orbpos == 1131:
                orb_pos = 'KoreaSat 5'
            elif orbpos == 1440:
                orb_pos = 'SuperBird 7,C2'
            elif orbpos == 1006:
                orb_pos = 'AsiaSat 2'
            elif orbpos == 1030:
                orb_pos = 'Express A2'
            elif orbpos == 1056:
                orb_pos = 'Asiasat 3S'
            elif orbpos == 1082:
                orb_pos = 'NSS 11'
            elif orbpos == 881:
                orb_pos = 'ST1'
            elif orbpos == 900:
                orb_pos = 'Yamal 201'
            elif orbpos == 917:
                orb_pos = 'Mesat'
            elif orbpos == 950:
                orb_pos = 'Insat 4B'
            elif orbpos == 951:
                orb_pos = 'NSS 6'
            elif orbpos == 765:
                orb_pos = 'Telestar'
            elif orbpos == 785:
                orb_pos = 'ThaiCom 5'
            elif orbpos == 800:
                orb_pos = 'Express'
            elif orbpos == 830:
                orb_pos = 'Insat 4A'
            elif orbpos == 850:
                orb_pos = 'Intelsat 709'
            elif orbpos == 750:
                orb_pos = 'Abs'
            elif orbpos == 720:
                orb_pos = 'Intelsat'
            elif orbpos == 705:
                orb_pos = 'Eutelsat W5'
            elif orbpos == 685:
                orb_pos = 'Intelsat'
            elif orbpos == 620:
                orb_pos = 'Intelsat 902'
            elif orbpos == 600:
                orb_pos = 'Intelsat 904'
            elif orbpos == 570:
                orb_pos = 'Nss'
            elif orbpos == 530:
                orb_pos = 'Express AM22'
            elif orbpos == 480:
                orb_pos = 'Eutelsat 2F2'
            elif orbpos == 450:
                orb_pos = 'Intelsat'
            elif orbpos == 420:
                orb_pos = 'Turksat 2A'
            elif orbpos == 400:
                orb_pos = 'Express AM1'
            elif orbpos == 390:
                orb_pos = 'Hellas Sat 2'
            elif orbpos == 380:
                orb_pos = 'Paksat 1'
            elif orbpos == 360:
                orb_pos = 'Eutelsat Sesat'
            elif orbpos == 335:
                orb_pos = 'Astra 1M'
            elif orbpos == 330:
                orb_pos = 'Eurobird 3'
            elif orbpos == 328:
                orb_pos = 'Galaxy 11'
            elif orbpos == 315:
                orb_pos = 'Astra 5A'
            elif orbpos == 310:
                orb_pos = 'Turksat'
            elif orbpos == 305:
                orb_pos = 'Arabsat'
            elif orbpos == 285:
                orb_pos = 'Eurobird 1'
            elif orbpos == 284:
                orb_pos = 'Eurobird/Astra'
            elif orbpos == 282:
                orb_pos = 'Eurobird/Astra'
            elif orbpos == 1220:
                orb_pos = 'AsiaSat'
            elif orbpos == 1380:
                orb_pos = 'Telstar 18'
            elif orbpos == 260:
                orb_pos = 'Badr 3/4'
            elif orbpos == 255:
                orb_pos = 'Eurobird 2'
            elif orbpos == 215:
                orb_pos = 'Eutelsat'
            elif orbpos == 216:
                orb_pos = 'Eutelsat W6'
            elif orbpos == 210:
                orb_pos = 'AfriStar 1'
            elif orbpos == 160:
                orb_pos = 'Eutelsat W2'
            elif orbpos == 100:
                orb_pos = 'Eutelsat W1'
            elif orbpos == 90:
                orb_pos = 'Eurobird 9'
            elif orbpos == 70:
                orb_pos = 'Eutelsat W3A'
            elif orbpos == 50:
                orb_pos = 'Sirius 4'
            elif orbpos == 48:
                orb_pos = 'Sirius 4'
            elif orbpos == 30:
                orb_pos = 'Telecom 2'
            else:
                orb_pos = str(float(orbpos) / 10.0) + 'E'
        return orb_pos

    def createProviderName(self, info):
        return info.getInfoString(iServiceInformation.sProvider)

    @cached
    def getText(self):
        service = self.source.service
        if service is None:
            return ''
        info = service and service.info()
        if not info:
            return ''
        if self.type == 'CryptoInfo':
            self.getCryptoInfo(info)
            if int(config.usage.show_cryptoinfo.getValue()) > 0:
                return addspace(self.createCryptoBar(info)) + self.createCryptoSpecial(info)
            else:
                return addspace(self.createCryptoBar(info)) + addspace(self.current_source) + self.createCryptoSpecial(info)
        if self.type == 'CryptoBar':
            if int(config.usage.show_cryptoinfo.getValue()) > 0:
                self.getCryptoInfo(info)
                return self.createCryptoBar(info)
            else:
                return ''
        if self.type == 'CryptoSeca':
            if int(config.usage.show_cryptoinfo.getValue()) > 0:
                self.getCryptoInfo(info)
                return self.createCryptoSeca(info)
            else:
                return ''
        if self.type == 'CryptoVia':
            if int(config.usage.show_cryptoinfo.getValue()) > 0:
                self.getCryptoInfo(info)
                return self.createCryptoVia(info)
            else:
                return ''
        if self.type == 'CryptoIrdeto':
            if int(config.usage.show_cryptoinfo.getValue()) > 0:
                self.getCryptoInfo(info)
                return self.createCryptoIrdeto(info)
            else:
                return ''
        if self.type == 'CryptoNDS':
            if int(config.usage.show_cryptoinfo.getValue()) > 0:
                self.getCryptoInfo(info)
                return self.createCryptoNDS(info)
            else:
                return ''
        if self.type == 'CryptoConax':
            if int(config.usage.show_cryptoinfo.getValue()) > 0:
                self.getCryptoInfo(info)
                return self.createCryptoConax(info)
            else:
                return ''
        if self.type == 'CryptoCryptoW':
            if int(config.usage.show_cryptoinfo.getValue()) > 0:
                self.getCryptoInfo(info)
                return self.createCryptoCryptoW(info)
            else:
                return ''
        if self.type == 'CryptoBeta':
            if int(config.usage.show_cryptoinfo.getValue()) > 0:
                self.getCryptoInfo(info)
                return self.createCryptoBeta(info)
            else:
                return ''
        if self.type == 'CryptoNagra':
            if int(config.usage.show_cryptoinfo.getValue()) > 0:
                self.getCryptoInfo(info)
                return self.createCryptoNagra(info)
            else:
                return ''
        if self.type == 'CryptoBiss':
            if int(config.usage.show_cryptoinfo.getValue()) > 0:
                self.getCryptoInfo(info)
                return self.createCryptoBiss(info)
            else:
                return ''
        if self.type == 'CryptoDre':
            if int(config.usage.show_cryptoinfo.getValue()) > 0:
                self.getCryptoInfo(info)
                return self.createCryptoDre(info)
            else:
                return ''
        if self.type == 'CryptoSpecial':
            if int(config.usage.show_cryptoinfo.getValue()) > 0:
                self.getCryptoInfo(info)
                return self.createCryptoSpecial(info)
            else:
                return ''
        if self.type == 'ResolutionString':
            return self.createResolution(info)
        elif self.type == 'VideoCodec':
            return self.createVideoCodec(info)
        if self.updateFEdata:
            feinfo = service.frontendInfo()
            if feinfo:
                self.feraw = feinfo.getAll(True)
                if self.feraw:
                    self.fedata = ConvertToHumanReadable(self.feraw)
        feraw = self.feraw
        fedata = self.fedata
        if not feraw or not fedata:
            return ''
        if self.type == 'All':
            self.getCryptoInfo(info)
            if int(config.usage.show_cryptoinfo.getValue()) > 0:
                return addspace(self.createProviderName(info)) + self.createTransponderInfo(fedata, feraw) + '\n' + addspace(self.createCryptoBar(info)) + addspace(self.createCryptoSpecial(info)) + '\n' + addspace(self.createPIDInfo(info)) + addspace(self.createVideoCodec(info)) + self.createResolution(info)
            else:
                return addspace(self.createProviderName(info)) + self.createTransponderInfo(fedata, feraw) + '\n' + addspace(self.createCryptoBar(info)) + self.current_source + '\n' + addspace(self.createCryptoSpecial(info)) + addspace(self.createVideoCodec(info)) + self.createResolution(info)
        if self.type == 'ServiceInfo':
            return addspace(self.createProviderName(info)) + addspace(self.createTunerSystem(fedata)) + addspace(self.createFrequency(fedata)) + addspace(self.createPolarization(fedata)) + addspace(self.createSymbolRate(fedata)) + addspace(self.createFEC(fedata)) + addspace(self.createModulation(fedata)) + addspace(self.createOrbPos(feraw)) + addspace(self.createVideoCodec(info)) + self.createResolution(info)
        elif self.type == 'TransponderInfo2line':
            return addspace(self.createProviderName(info)) + addspace(self.createTunerSystem(fedata)) + addspace(self.createTransponderName(feraw)) + '\n' + self.createFrequency(fedata) + addspace(' MHz') + addspace(self.createPolarization(fedata)) + addspace(self.createSymbolRate(fedata)) + self.createModulation(fedata) + '-' + addspace(self.createFEC(fedata))
        elif self.type == 'TransponderInfo':
            return self.createTransponderInfo(fedata, feraw)
        elif self.type == 'TransponderFrequency':
            return self.createFrequency(fedata)
        elif self.type == 'TransponderSymbolRate':
            return self.createSymbolRate(fedata)
        elif self.type == 'TransponderPolarization':
            return self.createPolarization(fedata)
        elif self.type == 'TransponderFEC':
            return self.createFEC(fedata)
        elif self.type == 'TransponderModulation':
            return self.createModulation(fedata)
        elif self.type == 'OrbitalPosition':
            return self.createOrbPos(feraw)
        elif self.type == 'TunerType':
            return self.createTunerType(feraw)
        elif self.type == 'TunerSystem':
            return self.createTunerSystem(fedata)
        elif self.type == 'OrbitalPositionOrTunerSystem':
            return self.createOrbPosOrTunerSystem(fedata, feraw)
        elif self.type == 'PIDInfo':
            return self.createPIDInfo(info)
        else:
            return _('invalid type')

    text = property(getText)

    @cached
    def getBool(self):
        service = self.source.service
        info = service and service.info()
        if not info:
            return False
        else:
            request_caid = None
            for x in self.ca_table:
                if x[0] == self.type:
                    request_caid = x[1]
                    request_selected = x[2]
                    break

            if request_caid is None:
                return False
            if info.getInfo(iServiceInformation.sIsCrypted) != 1:
                return False
            data = self.ecmdata.getEcmData()
            if data is None:
                return False
            current_caid = data[1]
            available_caids = info.getInfoObject(iServiceInformation.sCAIDs)
            for caid_entry in self.caid_data:
                if caid_entry[3] == request_caid:
                    if request_selected:
                        if int(current_caid, 16) >= int(caid_entry[0], 16) and int(current_caid, 16) <= int(caid_entry[1], 16):
                            return True
                    else:
                        try:
                            for caid in available_caids:
                                if caid >= int(caid_entry[0], 16) and caid <= int(caid_entry[1], 16):
                                    return True

                        except:
                            pass

            return False

    boolean = property(getBool)

    def changed(self, what):
        if what[0] == self.CHANGED_SPECIFIC:
            self.updateFEdata = False
            if what[1] == iPlayableService.evNewProgramInfo:
                self.updateFEdata = True
            if what[1] == iPlayableService.evEnd:
                self.feraw = self.fedata = None
            Converter.changed(self, what)
        elif what[0] == self.CHANGED_POLL and self.updateFEdata is not None:
            self.updateFEdata = False
            Converter.changed(self, what)
        return
