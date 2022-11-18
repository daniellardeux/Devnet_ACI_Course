#!/usr/bin/env python
'''
Autogenerated code using arya
Original Object Document Input: 
{"totalCount":"1","imdata":[{"fvTenant":{"attributes":{"annotation":"","descr":"","dn":"uni/tn-Sales","name":"Sales","nameAlias":"","ownerKey":"","ownerTag":"","userdom":":all:"},"children":[{"vzBrCP":{"attributes":{"annotation":"","descr":"","intent":"install","name":"FileServices_Ct","nameAlias":"","ownerKey":"","ownerTag":"","prio":"unspecified","scope":"context","targetDscp":"unspecified","userdom":":all:"},"children":[{"vzSubj":{"attributes":{"annotation":"","consMatchT":"AtleastOne","descr":"","name":"FileServices_Subj","nameAlias":"","prio":"unspecified","provMatchT":"AtleastOne","revFltPorts":"yes","targetDscp":"unspecified","userdom":":all:"},"children":[{"vzRsSubjFiltAtt":{"attributes":{"action":"permit","annotation":"","directives":"","priorityOverride":"default","tnVzFilterName":"FTP_Fltr","userdom":":all:"}}}]}}]}},{"vzBrCP":{"attributes":{"annotation":"","descr":"","intent":"install","name":"BasicServices_Ct","nameAlias":"","ownerKey":"","ownerTag":"","prio":"unspecified","scope":"context","targetDscp":"unspecified","userdom":":all:"},"children":[{"vzSubj":{"attributes":{"annotation":"","consMatchT":"AtleastOne","descr":"","name":"BasicServices_Subj","nameAlias":"","prio":"unspecified","provMatchT":"AtleastOne","revFltPorts":"yes","targetDscp":"unspecified","userdom":":all:"},"children":[{"vzRsSubjFiltAtt":{"attributes":{"action":"permit","annotation":"","directives":"","priorityOverride":"default","tnVzFilterName":"Basic_Fltr","userdom":":all:"}}}]}}]}},{"vzBrCP":{"attributes":{"annotation":"","descr":"","intent":"install","name":"WebServices","nameAlias":"","ownerKey":"","ownerTag":"","prio":"unspecified","scope":"context","targetDscp":"unspecified","userdom":":all:"},"children":[{"vzSubj":{"attributes":{"annotation":"","consMatchT":"AtleastOne","descr":"","name":"WebServices_Subject","nameAlias":"","prio":"unspecified","provMatchT":"AtleastOne","revFltPorts":"yes","targetDscp":"unspecified","userdom":":all:"},"children":[{"vzRsSubjFiltAtt":{"attributes":{"action":"permit","annotation":"","directives":"","priorityOverride":"default","tnVzFilterName":"TCP443_Filter","userdom":":all:"}}},{"vzRsSubjFiltAtt":{"attributes":{"action":"permit","annotation":"","directives":"","priorityOverride":"default","tnVzFilterName":"TCP80_Filter","userdom":":all:"}}}]}}]}},{"vnsSvcCont":{"attributes":{"annotation":"","userdom":"all"}}},{"fvEpTags":{"attributes":{"annotation":"","userdom":"all"}}},{"fvCtx":{"attributes":{"annotation":"","bdEnforcedEnable":"no","descr":"","ipDataPlaneLearning":"enabled","knwMcastAct":"permit","name":"Presales_VRF","nameAlias":"","ownerKey":"","ownerTag":"","pcEnfDir":"ingress","pcEnfPref":"enforced","userdom":":all:","vrfIndex":"0"},"children":[{"fvRsVrfValidationPol":{"attributes":{"annotation":"","tnL3extVrfValidationPolName":"","userdom":"all"}}},{"vzAny":{"attributes":{"annotation":"","descr":"","matchT":"AtleastOne","name":"","nameAlias":"","prefGrMemb":"disabled","userdom":"all"}}},{"fvRsOspfCtxPol":{"attributes":{"annotation":"","tnOspfCtxPolName":"","userdom":"all"}}},{"fvRsCtxToEpRet":{"attributes":{"annotation":"","tnFvEpRetPolName":"","userdom":"all"}}},{"fvRsCtxToExtRouteTagPol":{"attributes":{"annotation":"","tnL3extRouteTagPolName":"","userdom":"all"}}},{"fvRsBgpCtxPol":{"attributes":{"annotation":"","tnBgpCtxPolName":"","userdom":"all"}}}]}},{"fvBD":{"attributes":{"OptimizeWanBandwidth":"no","annotation":"","arpFlood":"no","descr":"","epClear":"no","epMoveDetectMode":"","hostBasedRouting":"no","intersiteBumTrafficAllow":"no","intersiteL2Stretch":"no","ipLearning":"yes","ipv6McastAllow":"no","limitIpLearnToSubnets":"yes","llAddr":"::","mac":"00:22:BD:F8:19:FF","mcastAllow":"no","multiDstPktAct":"bd-flood","name":"DB_BD","nameAlias":"","ownerKey":"","ownerTag":"","type":"regular","unicastRoute":"yes","unkMacUcastAct":"proxy","unkMcastAct":"flood","userdom":":all:","v6unkMcastAct":"flood","vmac":"not-applicable"},"children":[{"fvSubnet":{"attributes":{"annotation":"","ctrl":"nd","descr":"","ip":"10.0.2.254/24","ipDPLearning":"enabled","name":"","nameAlias":"","preferred":"no","scope":"private","userdom":":all:","virtual":"no"}}},{"fvRsMldsn":{"attributes":{"annotation":"","tnMldSnoopPolName":"","userdom":"all"}}},{"fvRsIgmpsn":{"attributes":{"annotation":"","tnIgmpSnoopPolName":"","userdom":"all"}}},{"fvRsCtx":{"attributes":{"annotation":"","tnFvCtxName":"","userdom":"all"}}},{"fvRsBdToEpRet":{"attributes":{"annotation":"","resolveAct":"resolve","tnFvEpRetPolName":"","userdom":"all"}}},{"fvRsBDToNdP":{"attributes":{"annotation":"","tnNdIfPolName":"","userdom":"all"}}}]}},{"fvBD":{"attributes":{"OptimizeWanBandwidth":"no","annotation":"","arpFlood":"no","descr":"","epClear":"no","epMoveDetectMode":"","hostBasedRouting":"no","intersiteBumTrafficAllow":"no","intersiteL2Stretch":"no","ipLearning":"yes","ipv6McastAllow":"no","limitIpLearnToSubnets":"yes","llAddr":"::","mac":"00:22:BD:F8:19:FF","mcastAllow":"no","multiDstPktAct":"bd-flood","name":"Presales_BD","nameAlias":"","ownerKey":"","ownerTag":"","type":"regular","unicastRoute":"yes","unkMacUcastAct":"proxy","unkMcastAct":"flood","userdom":":all:","v6unkMcastAct":"flood","vmac":"not-applicable"},"children":[{"fvSubnet":{"attributes":{"annotation":"","ctrl":"nd","descr":"","ip":"10.0.1.254/24","ipDPLearning":"enabled","name":"","nameAlias":"","preferred":"no","scope":"private","userdom":":all:","virtual":"no"}}},{"fvRsMldsn":{"attributes":{"annotation":"","tnMldSnoopPolName":"","userdom":"all"}}},{"fvRsIgmpsn":{"attributes":{"annotation":"","tnIgmpSnoopPolName":"","userdom":"all"}}},{"fvRsCtx":{"attributes":{"annotation":"","tnFvCtxName":"","userdom":"all"}}},{"fvRsBdToEpRet":{"attributes":{"annotation":"","resolveAct":"resolve","tnFvEpRetPolName":"","userdom":"all"}}},{"fvRsBDToNdP":{"attributes":{"annotation":"","tnNdIfPolName":"","userdom":"all"}}}]}},{"vzFilter":{"attributes":{"annotation":"","descr":"","name":"TCP80_Filter_cobra","nameAlias":"","ownerKey":"","ownerTag":"","userdom":":all:"},"children":[{"vzEntry":{"attributes":{"annotation":"","applyToFrag":"no","arpOpc":"unspecified","dFromPort":"http","dToPort":"http","descr":"","etherT":"ip","icmpv4T":"unspecified","icmpv6T":"unspecified","matchDscp":"unspecified","name":"TCP80_cobra","nameAlias":"","prot":"tcp","sFromPort":"unspecified","sToPort":"unspecified","stateful":"no","tcpRules":"","userdom":":all:"}}}]}},{"vzFilter":{"attributes":{"annotation":"","descr":"","name":"FTP_Fltr","nameAlias":"","ownerKey":"","ownerTag":"","userdom":":all:"},"children":[{"vzEntry":{"attributes":{"annotation":"","applyToFrag":"no","arpOpc":"unspecified","dFromPort":"21","dToPort":"21","descr":"","etherT":"ip","icmpv4T":"unspecified","icmpv6T":"unspecified","matchDscp":"unspecified","name":"TCP21","nameAlias":"","prot":"tcp","sFromPort":"unspecified","sToPort":"unspecified","stateful":"no","tcpRules":"","userdom":":all:"}}}]}},{"vzFilter":{"attributes":{"annotation":"","descr":"","name":"Basic_Fltr","nameAlias":"","ownerKey":"","ownerTag":"","userdom":":all:"},"children":[{"vzEntry":{"attributes":{"annotation":"","applyToFrag":"no","arpOpc":"unspecified","dFromPort":"unspecified","dToPort":"unspecified","descr":"","etherT":"ip","icmpv4T":"unspecified","icmpv6T":"unspecified","matchDscp":"unspecified","name":"ICMP","nameAlias":"","prot":"icmp","sFromPort":"unspecified","sToPort":"unspecified","stateful":"no","tcpRules":"","userdom":":all:"}}},{"vzEntry":{"attributes":{"annotation":"","applyToFrag":"no","arpOpc":"unspecified","dFromPort":"ssh","dToPort":"ssh","descr":"","etherT":"ip","icmpv4T":"unspecified","icmpv6T":"unspecified","matchDscp":"unspecified","name":"TCP22","nameAlias":"","prot":"tcp","sFromPort":"unspecified","sToPort":"unspecified","stateful":"yes","tcpRules":"","userdom":":all:"}}}]}},{"vzFilter":{"attributes":{"annotation":"","descr":"","name":"TCP443_Filter","nameAlias":"","ownerKey":"","ownerTag":"","userdom":":all:"},"children":[{"vzEntry":{"attributes":{"annotation":"","applyToFrag":"no","arpOpc":"unspecified","dFromPort":"https","dToPort":"https","descr":"","etherT":"ip","icmpv4T":"unspecified","icmpv6T":"unspecified","matchDscp":"unspecified","name":"TCP443","nameAlias":"","prot":"tcp","sFromPort":"unspecified","sToPort":"unspecified","stateful":"no","tcpRules":"","userdom":":all:"}}}]}},{"vzFilter":{"attributes":{"annotation":"","descr":"","name":"TCP80_Filter","nameAlias":"","ownerKey":"","ownerTag":"","userdom":":all:"},"children":[{"vzEntry":{"attributes":{"annotation":"","applyToFrag":"no","arpOpc":"unspecified","dFromPort":"http","dToPort":"http","descr":"","etherT":"ip","icmpv4T":"unspecified","icmpv6T":"unspecified","matchDscp":"unspecified","name":"TCP80","nameAlias":"","prot":"tcp","sFromPort":"unspecified","sToPort":"unspecified","stateful":"no","tcpRules":"","userdom":":all:"}}}]}},{"fvRsTenantMonPol":{"attributes":{"annotation":"","tnMonEPGPolName":"","userdom":"all"}}},{"fvAp":{"attributes":{"annotation":"","descr":"","name":"eCommerce","nameAlias":"","ownerKey":"","ownerTag":"","prio":"unspecified","userdom":":all:"},"children":[{"fvAEPg":{"attributes":{"annotation":"","descr":"","exceptionTag":"","floodOnEncap":"disabled","fwdCtrl":"","hasMcastSource":"no","isAttrBasedEPg":"no","matchT":"AtleastOne","name":"DB_EPG","nameAlias":"","pcEnfPref":"unenforced","prefGrMemb":"exclude","prio":"unspecified","shutdown":"no","userdom":":all:"},"children":[{"fvRsProv":{"attributes":{"annotation":"","intent":"install","matchT":"AtleastOne","prio":"unspecified","tnVzBrCPName":"FileServices_Ct","userdom":":all:"}}},{"fvRsCustQosPol":{"attributes":{"annotation":"","tnQosCustomPolName":"","userdom":"all"}}},{"fvRsBd":{"attributes":{"annotation":"","tnFvBDName":"DB_BD","userdom":"all"}}}]}},{"fvAEPg":{"attributes":{"annotation":"","descr":"","exceptionTag":"","floodOnEncap":"disabled","fwdCtrl":"","hasMcastSource":"no","isAttrBasedEPg":"no","matchT":"AtleastOne","name":"App_EPG","nameAlias":"","pcEnfPref":"unenforced","prefGrMemb":"exclude","prio":"unspecified","shutdown":"no","userdom":":all:"},"children":[{"fvRsProv":{"attributes":{"annotation":"","intent":"install","matchT":"AtleastOne","prio":"unspecified","tnVzBrCPName":"BasicServices_Ct","userdom":":all:"}}},{"fvRsProv":{"attributes":{"annotation":"","intent":"install","matchT":"AtleastOne","prio":"unspecified","tnVzBrCPName":"WebServices2","userdom":":all:"}}},{"fvRsProv":{"attributes":{"annotation":"","intent":"install","matchT":"AtleastOne","prio":"unspecified","tnVzBrCPName":"WebServices","userdom":":all:"}}},{"fvRsCons":{"attributes":{"annotation":"","intent":"install","prio":"unspecified","tnVzBrCPName":"FileServices_Ct","userdom":":all:"}}},{"fvRsCustQosPol":{"attributes":{"annotation":"","tnQosCustomPolName":"","userdom":"all"}}},{"fvRsBd":{"attributes":{"annotation":"","tnFvBDName":"Presales_BD","userdom":"all"}}}]}},{"fvAEPg":{"attributes":{"annotation":"","descr":"","exceptionTag":"","floodOnEncap":"disabled","fwdCtrl":"","hasMcastSource":"no","isAttrBasedEPg":"no","matchT":"AtleastOne","name":"Web_EPG","nameAlias":"","pcEnfPref":"unenforced","prefGrMemb":"exclude","prio":"unspecified","shutdown":"no","userdom":":all:"},"children":[{"fvRsCons":{"attributes":{"annotation":"","intent":"install","prio":"unspecified","tnVzBrCPName":"BasicServices_Ct","userdom":":all:"}}},{"fvRsCons":{"attributes":{"annotation":"","intent":"install","prio":"unspecified","tnVzBrCPName":"WebServices2","userdom":":all:"}}},{"fvRsCons":{"attributes":{"annotation":"","intent":"install","prio":"unspecified","tnVzBrCPName":"WebServices","userdom":":all:"}}},{"fvRsCustQosPol":{"attributes":{"annotation":"","tnQosCustomPolName":"","userdom":"all"}}},{"fvRsBd":{"attributes":{"annotation":"","tnFvBDName":"Presales_BD","userdom":"all"}}}]}}]}}]}}]}
'''

# list of packages that should be imported for this code to work
import cobra.mit.access
import cobra.mit.request
import cobra.mit.session
import cobra.model.fv
import cobra.model.pol
import cobra.model.vns
import cobra.model.vz
from cobra.internal.codec.xmlcodec import toXMLStr

# log into an APIC and create a directory object
ls = cobra.mit.session.LoginSession('https://apic', 'developer', '1234QWer')
md = cobra.mit.access.MoDirectory(ls)
md.login()

# the top level object on which operations will be made
polUni = cobra.model.pol.Uni('')

# build the request using cobra syntax
fvTenant = cobra.model.fv.Tenant(polUni, annotation='', descr='', name='Sales', nameAlias='', ownerKey='', ownerTag='', userdom=':all:')
vzBrCP = cobra.model.vz.BrCP(fvTenant, annotation='', descr='', intent='install', name='FileServices_Ct', nameAlias='', ownerKey='', ownerTag='', prio='unspecified', targetDscp='unspecified', userdom=':all:')
vzSubj = cobra.model.vz.Subj(vzBrCP, annotation='', consMatchT='AtleastOne', descr='', name='FileServices_Subj', nameAlias='', prio='unspecified', provMatchT='AtleastOne', revFltPorts='yes', targetDscp='unspecified', userdom=':all:')
vzRsSubjFiltAtt = cobra.model.vz.RsSubjFiltAtt(vzSubj, action='permit', annotation='', directives='', priorityOverride='default', tnVzFilterName='FTP_Fltr', userdom=':all:')
vzBrCP2 = cobra.model.vz.BrCP(fvTenant, annotation='', descr='', intent='install', name='BasicServices_Ct', nameAlias='', ownerKey='', ownerTag='', prio='unspecified', targetDscp='unspecified', userdom=':all:')
vzSubj2 = cobra.model.vz.Subj(vzBrCP2, annotation='', consMatchT='AtleastOne', descr='', name='BasicServices_Subj', nameAlias='', prio='unspecified', provMatchT='AtleastOne', revFltPorts='yes', targetDscp='unspecified', userdom=':all:')
vzRsSubjFiltAtt2 = cobra.model.vz.RsSubjFiltAtt(vzSubj2, action='permit', annotation='', directives='', priorityOverride='default', tnVzFilterName='Basic_Fltr', userdom=':all:')
vzBrCP3 = cobra.model.vz.BrCP(fvTenant, annotation='', descr='', intent='install', name='WebServices', nameAlias='', ownerKey='', ownerTag='', prio='unspecified', targetDscp='unspecified', userdom=':all:')
vzSubj3 = cobra.model.vz.Subj(vzBrCP3, annotation='', consMatchT='AtleastOne', descr='', name='WebServices_Subject', nameAlias='', prio='unspecified', provMatchT='AtleastOne', revFltPorts='yes', targetDscp='unspecified', userdom=':all:')
vzRsSubjFiltAtt3 = cobra.model.vz.RsSubjFiltAtt(vzSubj3, action='permit', annotation='', directives='', priorityOverride='default', tnVzFilterName='TCP443_Filter', userdom=':all:')
vzRsSubjFiltAtt4 = cobra.model.vz.RsSubjFiltAtt(vzSubj3, action='permit', annotation='', directives='', priorityOverride='default', tnVzFilterName='TCP80_Filter', userdom=':all:')
vnsSvcCont = cobra.model.vns.SvcCont(fvTenant, annotation='', userdom='all')
fvEpTags = cobra.model.fv.EpTags(fvTenant, annotation='', userdom='all')
fvCtx = cobra.model.fv.Ctx(fvTenant, annotation='', bdEnforcedEnable='no', descr='', ipDataPlaneLearning='enabled', knwMcastAct='permit', name='Presales_VRF', nameAlias='', ownerKey='', ownerTag='', pcEnfDir='ingress', pcEnfPref='enforced', userdom=':all:', vrfIndex='0')
fvRsVrfValidationPol = cobra.model.fv.RsVrfValidationPol(fvCtx, annotation='', tnL3extVrfValidationPolName='', userdom='all')
vzAny = cobra.model.vz.Any(fvCtx, annotation='', descr='', matchT='AtleastOne', name='', nameAlias='', prefGrMemb='disabled', userdom='all')
fvRsOspfCtxPol = cobra.model.fv.RsOspfCtxPol(fvCtx, annotation='', tnOspfCtxPolName='', userdom='all')
fvRsCtxToEpRet = cobra.model.fv.RsCtxToEpRet(fvCtx, annotation='', tnFvEpRetPolName='', userdom='all')
fvRsCtxToExtRouteTagPol = cobra.model.fv.RsCtxToExtRouteTagPol(fvCtx, annotation='', tnL3extRouteTagPolName='', userdom='all')
fvRsBgpCtxPol = cobra.model.fv.RsBgpCtxPol(fvCtx, annotation='', tnBgpCtxPolName='', userdom='all')
fvBD = cobra.model.fv.BD(fvTenant, OptimizeWanBandwidth='no', annotation='', arpFlood='no', descr='', epClear='no', epMoveDetectMode='', hostBasedRouting='no', intersiteBumTrafficAllow='no', intersiteL2Stretch='no', ipLearning='yes', ipv6McastAllow='no', limitIpLearnToSubnets='yes', llAddr='::', mac='00:22:BD:F8:19:FF', mcastAllow='no', multiDstPktAct='bd-flood', name='DB_BD', nameAlias='', ownerKey='', ownerTag='', type='regular', unicastRoute='yes', unkMacUcastAct='proxy', unkMcastAct='flood', userdom=':all:', v6unkMcastAct='flood', vmac='not-applicable')
fvSubnet = cobra.model.fv.Subnet(fvBD, annotation='', ctrl='nd', descr='', ip='10.0.2.254/24', ipDPLearning='enabled', name='', nameAlias='', preferred='no', userdom=':all:', virtual='no')
fvRsMldsn = cobra.model.fv.RsMldsn(fvBD, annotation='', tnMldSnoopPolName='', userdom='all')
fvRsIgmpsn = cobra.model.fv.RsIgmpsn(fvBD, annotation='', tnIgmpSnoopPolName='', userdom='all')
fvRsCtx = cobra.model.fv.RsCtx(fvBD, annotation='', tnFvCtxName='', userdom='all')
fvRsBdToEpRet = cobra.model.fv.RsBdToEpRet(fvBD, annotation='', resolveAct='resolve', tnFvEpRetPolName='', userdom='all')
fvRsBDToNdP = cobra.model.fv.RsBDToNdP(fvBD, annotation='', tnNdIfPolName='', userdom='all')
fvBD2 = cobra.model.fv.BD(fvTenant, OptimizeWanBandwidth='no', annotation='', arpFlood='no', descr='', epClear='no', epMoveDetectMode='', hostBasedRouting='no', intersiteBumTrafficAllow='no', intersiteL2Stretch='no', ipLearning='yes', ipv6McastAllow='no', limitIpLearnToSubnets='yes', llAddr='::', mac='00:22:BD:F8:19:FF', mcastAllow='no', multiDstPktAct='bd-flood', name='Presales_BD', nameAlias='', ownerKey='', ownerTag='', type='regular', unicastRoute='yes', unkMacUcastAct='proxy', unkMcastAct='flood', userdom=':all:', v6unkMcastAct='flood', vmac='not-applicable')
fvSubnet2 = cobra.model.fv.Subnet(fvBD2, annotation='', ctrl='nd', descr='', ip='10.0.1.254/24', ipDPLearning='enabled', name='', nameAlias='', preferred='no', userdom=':all:', virtual='no')
fvRsMldsn2 = cobra.model.fv.RsMldsn(fvBD2, annotation='', tnMldSnoopPolName='', userdom='all')
fvRsIgmpsn2 = cobra.model.fv.RsIgmpsn(fvBD2, annotation='', tnIgmpSnoopPolName='', userdom='all')
fvRsCtx2 = cobra.model.fv.RsCtx(fvBD2, annotation='', tnFvCtxName='', userdom='all')
fvRsBdToEpRet2 = cobra.model.fv.RsBdToEpRet(fvBD2, annotation='', resolveAct='resolve', tnFvEpRetPolName='', userdom='all')
fvRsBDToNdP2 = cobra.model.fv.RsBDToNdP(fvBD2, annotation='', tnNdIfPolName='', userdom='all')
vzFilter = cobra.model.vz.Filter(fvTenant, annotation='', descr='', name='TCP80_Filter_cobra', nameAlias='', ownerKey='', ownerTag='', userdom=':all:')
vzEntry = cobra.model.vz.Entry(vzFilter, annotation='', applyToFrag='no', arpOpc='unspecified', dFromPort='http', dToPort='http', descr='', etherT='ip', icmpv4T='unspecified', icmpv6T='unspecified', matchDscp='unspecified', name='TCP80_cobra', nameAlias='', prot='tcp', sFromPort='unspecified', sToPort='unspecified', stateful='no', tcpRules='', userdom=':all:')
vzFilter2 = cobra.model.vz.Filter(fvTenant, annotation='', descr='', name='FTP_Fltr', nameAlias='', ownerKey='', ownerTag='', userdom=':all:')
vzEntry2 = cobra.model.vz.Entry(vzFilter2, annotation='', applyToFrag='no', arpOpc='unspecified', dFromPort='21', dToPort='21', descr='', etherT='ip', icmpv4T='unspecified', icmpv6T='unspecified', matchDscp='unspecified', name='TCP21', nameAlias='', prot='tcp', sFromPort='unspecified', sToPort='unspecified', stateful='no', tcpRules='', userdom=':all:')
vzFilter3 = cobra.model.vz.Filter(fvTenant, annotation='', descr='', name='Basic_Fltr', nameAlias='', ownerKey='', ownerTag='', userdom=':all:')
vzEntry3 = cobra.model.vz.Entry(vzFilter3, annotation='', applyToFrag='no', arpOpc='unspecified', dFromPort='unspecified', dToPort='unspecified', descr='', etherT='ip', icmpv4T='unspecified', icmpv6T='unspecified', matchDscp='unspecified', name='ICMP', nameAlias='', prot='icmp', sFromPort='unspecified', sToPort='unspecified', stateful='no', tcpRules='', userdom=':all:')
vzEntry4 = cobra.model.vz.Entry(vzFilter3, annotation='', applyToFrag='no', arpOpc='unspecified', dFromPort='ssh', dToPort='ssh', descr='', etherT='ip', icmpv4T='unspecified', icmpv6T='unspecified', matchDscp='unspecified', name='TCP22', nameAlias='', prot='tcp', sFromPort='unspecified', sToPort='unspecified', stateful='yes', tcpRules='', userdom=':all:')
vzFilter4 = cobra.model.vz.Filter(fvTenant, annotation='', descr='', name='TCP443_Filter', nameAlias='', ownerKey='', ownerTag='', userdom=':all:')
vzEntry5 = cobra.model.vz.Entry(vzFilter4, annotation='', applyToFrag='no', arpOpc='unspecified', dFromPort='https', dToPort='https', descr='', etherT='ip', icmpv4T='unspecified', icmpv6T='unspecified', matchDscp='unspecified', name='TCP443', nameAlias='', prot='tcp', sFromPort='unspecified', sToPort='unspecified', stateful='no', tcpRules='', userdom=':all:')
vzFilter5 = cobra.model.vz.Filter(fvTenant, annotation='', descr='', name='TCP80_Filter', nameAlias='', ownerKey='', ownerTag='', userdom=':all:')
vzEntry6 = cobra.model.vz.Entry(vzFilter5, annotation='', applyToFrag='no', arpOpc='unspecified', dFromPort='http', dToPort='http', descr='', etherT='ip', icmpv4T='unspecified', icmpv6T='unspecified', matchDscp='unspecified', name='TCP80', nameAlias='', prot='tcp', sFromPort='unspecified', sToPort='unspecified', stateful='no', tcpRules='', userdom=':all:')
fvRsTenantMonPol = cobra.model.fv.RsTenantMonPol(fvTenant, annotation='', tnMonEPGPolName='', userdom='all')
fvAp = cobra.model.fv.Ap(fvTenant, annotation='', descr='', name='eCommerce', nameAlias='', ownerKey='', ownerTag='', prio='unspecified', userdom=':all:')
fvAEPg = cobra.model.fv.AEPg(fvAp, annotation='', descr='', exceptionTag='', floodOnEncap='disabled', fwdCtrl='', hasMcastSource='no', isAttrBasedEPg='no', matchT='AtleastOne', name='DB_EPG', nameAlias='', pcEnfPref='unenforced', prefGrMemb='exclude', prio='unspecified', shutdown='no', userdom=':all:')
fvRsProv = cobra.model.fv.RsProv(fvAEPg, annotation='', intent='install', matchT='AtleastOne', prio='unspecified', tnVzBrCPName='FileServices_Ct', userdom=':all:')
fvRsCustQosPol = cobra.model.fv.RsCustQosPol(fvAEPg, annotation='', tnQosCustomPolName='', userdom='all')
fvRsBd = cobra.model.fv.RsBd(fvAEPg, annotation='', tnFvBDName='DB_BD', userdom='all')
fvAEPg2 = cobra.model.fv.AEPg(fvAp, annotation='', descr='', exceptionTag='', floodOnEncap='disabled', fwdCtrl='', hasMcastSource='no', isAttrBasedEPg='no', matchT='AtleastOne', name='App_EPG', nameAlias='', pcEnfPref='unenforced', prefGrMemb='exclude', prio='unspecified', shutdown='no', userdom=':all:')
fvRsProv2 = cobra.model.fv.RsProv(fvAEPg2, annotation='', intent='install', matchT='AtleastOne', prio='unspecified', tnVzBrCPName='BasicServices_Ct', userdom=':all:')
fvRsProv3 = cobra.model.fv.RsProv(fvAEPg2, annotation='', intent='install', matchT='AtleastOne', prio='unspecified', tnVzBrCPName='WebServices2', userdom=':all:')
fvRsProv4 = cobra.model.fv.RsProv(fvAEPg2, annotation='', intent='install', matchT='AtleastOne', prio='unspecified', tnVzBrCPName='WebServices', userdom=':all:')
fvRsCons = cobra.model.fv.RsCons(fvAEPg2, annotation='', intent='install', prio='unspecified', tnVzBrCPName='FileServices_Ct', userdom=':all:')
fvRsCustQosPol2 = cobra.model.fv.RsCustQosPol(fvAEPg2, annotation='', tnQosCustomPolName='', userdom='all')
fvRsBd2 = cobra.model.fv.RsBd(fvAEPg2, annotation='', tnFvBDName='Presales_BD', userdom='all')
fvAEPg3 = cobra.model.fv.AEPg(fvAp, annotation='', descr='', exceptionTag='', floodOnEncap='disabled', fwdCtrl='', hasMcastSource='no', isAttrBasedEPg='no', matchT='AtleastOne', name='Web_EPG', nameAlias='', pcEnfPref='unenforced', prefGrMemb='exclude', prio='unspecified', shutdown='no', userdom=':all:')
fvRsCons2 = cobra.model.fv.RsCons(fvAEPg3, annotation='', intent='install', prio='unspecified', tnVzBrCPName='BasicServices_Ct', userdom=':all:')
fvRsCons3 = cobra.model.fv.RsCons(fvAEPg3, annotation='', intent='install', prio='unspecified', tnVzBrCPName='WebServices2', userdom=':all:')
fvRsCons4 = cobra.model.fv.RsCons(fvAEPg3, annotation='', intent='install', prio='unspecified', tnVzBrCPName='WebServices', userdom=':all:')
fvRsCustQosPol3 = cobra.model.fv.RsCustQosPol(fvAEPg3, annotation='', tnQosCustomPolName='', userdom='all')
fvRsBd3 = cobra.model.fv.RsBd(fvAEPg3, annotation='', tnFvBDName='Presales_BD', userdom='all')


# commit the generated code to APIC
print(toXMLStr(polUni))
c = cobra.mit.request.ConfigRequest()
c.addMo(polUni)
md.commit(c)
