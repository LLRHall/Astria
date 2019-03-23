function replacer(str) {
    var pairs = {
     "ACC(SC)":"<div>Accident and Compensation Cases (SC)</div>"
  ,
  
     "ACJ":"<div>Accidents Claims Journal</div>"
  ,
  
     "AIHC":"<div>All India High Court Cases</div>"
  ,
  
     "FAJ":"<div>All India Prevention of Food Adulteration Journal</div>"
  ,
  
     "AIR":"<div>All India Reporter</div>"
  ,
  
     "AIR(Mys)":"<div>All India Reporter (Mys)</div>"
  ,
  
     "ALLMR":"<div>ALL MAHARASHTRA LAW REPORTER</div>"
  ,
  
     "ALLMR (SC)":"<div>ALL MAHARASHTRA LAW REPORTER SC</div>"
  ,
  
     "ALLMR(Cri)":"<div>ALL MAHARSHTRA LAW REPORTER (Cri)</div>"
  ,
  
     "ARC":"<div>Allahabad Rent Cases</div>"
  ,
  
     "AWC":"<div>Allahabad Weekly Cases</div>"
  ,
  
     "AWCSC":"<div>Allahabad Weekly Cases (Supp - SC)</div>"
  ,
  
     "AWCUHC":"<div>Allahabad Weekly Cases UHC</div>"
  ,
  
     "ALT":"<div>Andhra Law Times</div>"
  ,
  
     "ALT(Cri)":"<div>Andhra Law Times (Criminal)</div>"
  ,
  
     "ALT(SC)":"<div>Andhra Law Times(SC)</div>"
  ,
  
     "ALD(Cri)":"<div>Andhra Legal Decision (Criminal)</div>"
  ,
  
     "ALD":"<div>Andhra Legal Decisions</div>"
  ,
  
     "ALD-SC":"<div>Andhra Legal Decisions (SC)</div>"
  ,
  
     "APLJ":"<div>Andhra Pradesh Law Journal</div>"
  ,
  
     "AnWR":"<div>Andhra Weekly Reporter</div>"
  ,
  
     "AD":"<div>Apex Decision</div>"
  ,
  
     "ARBLR":"<div>Arbitration Law Reporter</div>"
  ,
  
     "BC":"<div>Banking Cases</div>"
  ,
  
     "BC-SC":"<div>Banking Cases with court</div>"
  ,
  
     "BLJR":"<div>Bihar Law Journal Reports</div>"
  ,
  
     "BomCR":"<div>Bombay Cases Reporter</div>"
  ,
  
     "BomCR(Cri)":"<div>Bombay Cases Reporter (Criminal)</div>"
  ,
  
     "BomCRSupp":"<div>Bombay Cases Reporter(Supp)</div>"
  ,
  
     "BOMLR":"<div>Bombay Law Reporter</div>"
  ,
  
     "BusLR":"<div>Business Law Reports</div>"
  ,
  
     "CHN":"<div>Calcutta High Court Notes</div>"
  ,
  
     "CHN(SC)":"<div>Calcutta High Court Notes (SC)</div>"
  ,
  
     "CALLT":"<div>Calcutta Law Times</div>"
  ,
  
     "CWN":"<div>Calcutta Weekly Notes</div>"
  ,
  
     "CivilCC":"<div>Civil Court Cases</div>"
  ,
  
     "CivilCCSup":"<div>Civil Court Cases (Supp)</div>"
  ,
  
     "CompCas":"<div>Company Cases</div>"
  ,
  
     "CompLJ":"<div>Company Law Journal</div>"
  ,
  
     "CompAT":"<div>Competition Law Reports</div>"
  ,
  
     "CPJ":"<div>Consumer Protection Judgments</div>"
  ,
  
     "CTLJ":"<div>Contracts and Tenders Law Journal</div>"
  ,
  
     "CLA":"<div>Corporate Law Adviser</div>"
  ,
  
     "CLA-BL-Sup":"<div>Corporate Law Advisor – Business Law Supplement</div>"
  ,
  
     "Crime":"<div>Crimes</div>"
  ,
  
     "Crimes":"<div>Crimes (SC)</div>"
  ,
  
     "CriLJ":"<div>Criminal Law Journal</div>"
  ,
  
     "CCR":"<div>Current Criminal Reports</div>"
  ,
  
     "CCR(SC)":"<div>Current Criminal Reports (SC)</div>"
  ,
  
     "CTC":"<div>Current Tamil Nadu Cases</div>"
  ,
  
     "CTR":"<div>Current Tax Reporter</div>"
  ,
  
     "CLT":"<div>Cuttack Law Times</div>"
  ,
  
     "CLT(SC)":"<div>Cuttack Law Times (SC)</div>"
  ,
  
     "CWN":"<div>Calcutta Weekly Notes</div>"
  ,
  
     "DLT":"<div>Delhi Law Times</div>"
  ,
  
     "DLT(SC)":"<div>Delhi Law Times (SC)</div>"
  ,
  
     "DRJ":"<div>Delhi Reported Journal</div>"
  ,
  
     "DRJSupp":"<div>Delhi Reported Journal (Suppl)</div>"
  ,
  
     "DRJSupp NV":"<div>Delhi Reported Journal (Suppl)without Volume</div>"
  ,
  
     "DMC":"<div>Divorce and Matrimonial Cases</div>"
  ,
  
     "DMC(SC)":"<div>Divorce and Matrimonial Cases (SC)</div>"
  ,
  
     "ESC":"<div>Education and Service Cases</div>"
  ,
  
     "ELR":"<div>Energy Law Reports</div>"
  ,
  
     "ECC":"<div>Excise & Customs Cases</div>"
  ,
  
     "ECR":"<div>Excise and Custom Reprots (Without Volume)</div>"
  ,
  
     "ELT":"<div>Excise Law Times</div>"
  ,
  
     "FLR":"<div>Factory Law Reporter</div>"
  ,
  
     "GLD":"<div>Gauhati Law Decisions</div>"
  ,
  
     "GLDSupp":"<div>Gauhati Law Decisions Supp</div>"
  ,
  
     "GauLR":"<div>Gauhati Law Reports</div>"
  ,
  
     "GLT":"<div>Gauhati Law Times</div>"
  ,
  
     "GLT(SC)":"<div>Gauhati Law Times (SC)</div>"
  ,
  
     "GLH":"<div>Gujarat Law Herald</div>"
  ,
  
     "GLR":"<div>Gujarat Law Reporter</div>"
  ,
  
     "GLR (FB)":"<div>Gujarat Law Reporter (FB)</div>"
  ,
  
     "GLR (SC)":"<div>Gujarat Law Reporter (SC)</div>"
  ,
  
     "ITR":"<div>Income Tax Reporter</div>"
  ,
  
     "ITD":"<div>Income-tax Tribunal Decisions</div>"
  ,
  
     "Ind.Cas.":"<div>Indian Cases</div>"
  ,
  
     "ILR":"<div>Indian Law Reports</div>"
  ,
  
     "ILR (Bom)":"<div>Indian Law Reports (Bombay)</div>"
  ,
  
     "ILR (PC)":"<div>Indian Law Reports (P C)</div>"
  ,
  
     "ILR Pre":"<div>Indian Law Reports (Pre)</div>"
  ,
  
     "ITDSB":"<div>ITD Special Bench</div>"
  ,
  
     "JCR":"<div>Jharkhand Cases Reporter</div>"
  ,
  
     "JKJ":"<div>JK Judgments</div>"
  ,
  
     "JKJ [SC]":"<div>JK Judgments [SC]</div>"
  ,
  
     "JCC":"<div>Journal Of Criminal Cases</div>"
  ,
  
     "JCC(SC)":"<div>Journal Of Criminal Cases (SC)</div>"
  ,
  
     "JT":"<div>Judgment Today</div>"
  ,
  
     "JT (Suppl)":"<div>Judgment Today Supplement</div>"
  ,
  
     "KCCR":"<div>Karnataka Civil and Criminal Reporter</div>"
  ,
  
     "KarLJ":"<div>Karnataka Law Journal</div>"
  ,
  
     "KLJ":"<div>Kerala Law Journal</div>"
  ,
  
     "KLT":"<div>Kerala Law Times</div>"
  ,
  
     "KLT (SC)":"<div>Kerala Law Times (SC)</div>"
  ,
  
     "LabIC":"<div>Labour and Industrial cases</div>"
  ,
  
     "LLJ":"<div>Labour Law Journal</div>"
  ,
  
     "LS":"<div>Law Summary</div>"
  ,
  
     "MPLJ":"<div>M.P. Law Journal</div>"
  ,
  
     "MPLJ(SC)":"<div>M.P. Law Journal(SC)</div>"
  ,
  
     "MLJ":"<div>Madras Law Journal</div>"
  ,
  
     "MLJ(SC)":"<div>Madras Law Journal (SC)</div>"
  ,
  
     "MhLj":"<div>Maharashtra Law Journal</div>"
  ,
  
     "MhLJ(SC)":"<div>Maharastra Law Journal SC</div>"
  ,
  
     "MIPR":"<div>MIPR</div>"
  ,
  
     "M.I.A.":"<div>Moores Indian Appeals</div>"
  ,
  
     "MPHT":"<div>MP High Court Today</div>"
  ,
  
     "MPHT(CG)":"<div>MP High Court Today with court</div>"
  ,
  
     "MysLJ":"<div>Mysore Law Journal</div>"
  ,
  
     "MysLJ(SC)":"<div>Mysore Law Journal (SC)</div>"
  ,
  
     "OLR":"<div>Orissa Law Reviews</div>"
  ,
  
     "OLR (SC)":"<div>Orissa Law Reviews (SC)</div>"
  ,
  
     "PTC":"<div>Patent & Trade Marks Cases</div>"
  ,
  
     "PLR":"<div>Punjab Law Reporter</div>"
  ,
  
     "RLR":"<div>Rajasthan Law Reporter</div>"
  ,
  
     "RLW":"<div>Rajasthan Law Weekly</div>"
  ,
  
     "RAJ":"<div>Rajdhani Law Reporter</div>"
  ,
  
     "RArJ":"<div>Recent Arbitration Judgments</div>"
  ,
  
     "RAJ(SC)":"<div>Recent Arbitration Judgments (SC)</div>"
  ,
  
     "RLT":"<div>Revenue Law Times</div>"
  ,
  
     "STC":"<div>Sales Tax Cases</div>"
  ,
  
     "SCR no vol":"<div>SCR Supp without Volume</div>"
  ,
  
     "SCL":"<div>Sebi and Corporate laws</div>"
  ,
  
     "SOT":"<div>Selected Orders of ITAT</div>"
  ,
  
     "SCT":"<div>Service Cases Today</div>"
  ,
  
     "STJ":"<div>Service Tax Journal</div>"
  ,
  
     "STR":"<div>Service Tax Review</div>"
  ,
  
     "SLJ":"<div>Services Law Journal</div>"
  ,
  
     "SLR":"<div>Services Law Reporter</div>"
  ,
  
     "SLR(SC)":"<div>Services Law Reporter (SC)</div>"
  ,
  
     "ShimLC":"<div>Shimla Law Cases</div>"
  ,
  
     "SCALE":"<div>Supreme Court Almanac</div>"
  ,
  
     "SCC":"<div>Supreme Court Cases</div>"
  ,
  
     "SCC (Supp)":"<div>Supreme Court Cases (Supp)</div>"
  ,
  
     "SCR":"<div>Supreme Court Reporter</div>"
  ,
  
     "TTJ":"<div>Tax Tribunal Judgments</div>"
  ,
  
     "TAXLR":"<div>Taxation Law Reporter</div>"
  ,
  
     "TAXMAN":"<div>TAXMAN</div>"
  ,
  
     "STT":"<div>Taxman's Service Tax Today</div>"
  ,
  
     "Ind.Ap.":"<div>The Law Report - Indian Appeals</div>"
  ,
  
     "Ind.Ap.sv":"<div>The Law Report - Indian Appeals(Supp. Vol.)</div>"
  ,
  
     "UJ":"<div>The Unreported Judgments</div>"
  ,
  
     "UPLBEC":"<div>U.P. Local Bodies & Educational Cases</div>"
  ,
  
     "VST":"<div>VAT AND SERVICE TAX CASES</div>"
  ,
  
     "VR":"<div>Vat Reporter</div>"
  ,
  
     "WLN":"<div>Weekly Law Notes</div>"
  ,
  
     "WLNRev":"<div>Weekly Law Notes Revenue</div>"
  ,
  
     "WLNUC":"<div>Weekly Law Notes UC</div>"
  ,
  
     "WLNWV":"<div>Weekly Law Notes Without Volume</div>"
  ,
  
     "WLC":"<div>Western Law Cases</div>"
  ,
  
     "WLC(Raj)UC":"<div>Western Law Cases (Raj) UC</div>"
    };
    Object.keys(pairs).forEach(function (key) {
        str = str.split(key).join(pairs[key]);
    });
    return str;
}
};