import mysql.connector as sql;

con = sql.connect (host="mydb1.cfxj0ajszti7.us-east-1.rds.amazonaws.com",user="admin",password="12345678",database="mydb");
cur = con.cursor();

q1 = '''INSERT INTO pages_team VALUES
    (686,'MCLUST01TEAM12',' EPC','C325'),
    (687,'MCLUST01TEAM21',' EPC','C325'),
    (688,'MCLUST01TEAM23',' EPC','C325'),
    (689,'MCLUST01TEAM89',' EPC','C325'),
    (690,'MCLUST02TEAM100',' EPC','C325'),
    (691,'MCLUST02TEAM104',' EPC','C325'),
    (692,'MCLUST02TEAM79',' EPC','C325'),
    (693,'MCLUST02TEAM92',' EPC','C325'),
    (694,'MCLUST03TEAM35',' EPC','C325'),
    (695,'MCLUST03TEAM44',' EPC','C325'),
    (696,'MCLUST03TEAM78',' EPC','C325'),
    (697,'MCLUST01TEAM103','AAS','C108'),
    (698,'MCLUST01TEAM3','AAS','C108'),
    (699,'MCLUST01TEAM31','AAS','C108'),
    (700,'MCLUST01TEAM5','AAS','C108'),
    (701,'MCLUST01TEAM62','AAS','C108'),
    (702,'MCLUST02TEAM31','AAS','C108'),
    (703,'MCLUST02TEAM60','AAS','C108'),
    (704,'MCLUST02TEAM75','AAS','C108'),
    (705,'MCLUST03TEAM11','AAS','C108'),
    (706,'MCLUST03TEAM70','AAS','C108'),
    (707,'MCLUST03TEAM75','AAS','C108'),
    (708,'MCLUST01TEAM28','AMS','C110'),
    (709,'MCLUST01TEAM51','AMS','C110'),
    (710,'MCLUST01TEAM69','AMS','C110'),
    (711,'MCLUST01TEAM86','AMS','C110'),
    (712,'MCLUST01TEAM96','AMS','C110'),
    (713,'MCLUST01TEAM98','AMS','C110'),
    (714,'MCLUST02TEAM55','AMS','C110'),
    (715,'MCLUST02TEAM69','AMS','C110'),
    (716,'MCLUST02TEAM83','AMS','C110'),
    (717,'MCLUST03TEAM34','AMS','C110'),
    (718,'MCLUST03TEAM59','AMS','C110'),
    (719,'MCLUST01TEAM71','APS ','C121'),
    (720,'MCLUST01TEAM77','APS ','C121'),
    (721,'MCLUST02TEAM39','APS ','C121'),
    (722,'MCLUST02TEAM6','APS ','C121'),
    (723,'MCLUST02TEAM61','APS ','C121'),
    (724,'MCLUST02TEAM78','APS ','C121'),
    (725,'MCLUST02TEAM97','APS ','C121'),
    (726,'MCLUST03TEAM16','APS ','C121'),
    (727,'MCLUST03TEAM17','APS ','C121'),
    (728,'MCLUST03TEAM5','APS ','C121'),
    (729,'MCLUST03TEAM79','APS ','C121'),
    (730,'MCLUST01TEAM13','BDS','C225'),
    (731,'MCLUST01TEAM39','BDS','C225'),
    (732,'MCLUST01TEAM50','BDS','C225'),
    (733,'MCLUST01TEAM53','BDS','C225'),
    (734,'MCLUST01TEAM58','BDS','C225'),
    (735,'MCLUST01TEAM59','BDS','C225'),
    (736,'MCLUST02TEAM77','BDS','C225'),
    (737,'MCLUST03TEAM18','BDS','C225'),
    (738,'MCLUST03TEAM29','BDS','C225'),
    (739,'MCLUST03TEAM30','BDS','C225'),
    (740,'MCLUST03TEAM50','BDS','C225'),
    (741,'MCLUST03TEAM8','BDS','C225'),
    (742,'MCLUST01TEAM22','BFS','C308'),
    (743,'MCLUST01TEAM38','BFS','C308'),
    (744,'MCLUST02TEAM21','BFS','C308'),
    (745,'MCLUST02TEAM56','BFS','C308'),
    (746,'MCLUST02TEAM57','BFS','C308'),
    (747,'MCLUST02TEAM62','BFS','C308'),
    (748,'MCLUST02TEAM73','BFS','C308'),
    (749,'MCLUST02TEAM88','BFS','C308'),
    (750,'MCLUST03TEAM10','BFS','C308'),
    (751,'MCLUST03TEAM54','BFS','C308'),
    (752,'MCLUST03TEAM56','BFS','C308'),
    (753,'MCLUST01TEAM29','BMS','C321B2'),
    (754,'MCLUST01TEAM34','BMS','C321B2'),
    (755,'MCLUST01TEAM35','BMS','C321B2'),
    (756,'MCLUST01TEAM40','BMS','C321B2'),
    (757,'MCLUST01TEAM80','BMS','C321B2'),
    (758,'MCLUST02TEAM17','BMS','C321B2'),
    (759,'MCLUST02TEAM49','BMS','C321B2'),
    (760,'MCLUST02TEAM91','BMS','C321B2'),
    (761,'MCLUST03TEAM32','BMS','C321B2'),
    (762,'MCLUST03TEAM63','BMS','C321B2'),
    (763,'MCLUST03TEAM7','BMS','C321B2'),
    (764,'MCLUST01TEAM105','ERP','C121'),
    (765,'MCLUST01TEAM45','ERP','C121'),
    (766,'MCLUST01TEAM47','ERP','C121'),
    (767,'MCLUST02TEAM45','ERP','C121'),
    (768,'MCLUST02TEAM70','ERP','C121'),
    (769,'MCLUST02TEAM71','ERP','C121'),
    (770,'MCLUST03TEAM14','ERP','C121'),
    (771,'MCLUST03TEAM3','ERP','C121'),
    (772,'MCLUST03TEAM71','ERP','C121'),
    (773,'MCLUST03TEAM73','ERP','C121'),
    (774,'MCLUST03TEAM84','ERP','C121'),
    (775,'MCLUST01TEAM17','ETS','C407'),
    (776,'MCLUST01TEAM26','ETS','C407'),
    (777,'MCLUST01TEAM36','ETS','C407'),
    (778,'MCLUST01TEAM44','ETS','C407'),
    (779,'MCLUST01TEAM46','ETS','C407'),
    (780,'MCLUST01TEAM60','ETS','C407'),
    (781,'MCLUST01TEAM79','ETS','C407'),
    (782,'MCLUST02TEAM18','ETS','C407'),
    (783,'MCLUST02TEAM35','ETS','C407'),
    (784,'MCLUST02TEAM51','ETS','C407'),
    (785,'MCLUST03TEAM31','ETS','C407'),
    (786,'MCLUST01TEAM42','EVM','C411'),
    (787,'MCLUST01TEAM48','EVM','C411'),
    (788,'MCLUST01TEAM72','EVM','C411'),
    (789,'MCLUST01TEAM81','EVM','C411'),
    (790,'MCLUST01TEAM92','EVM','C411'),
    (791,'MCLUST02TEAM23','EVM','C411'),
    (792,'MCLUST02TEAM24','EVM','C411'),
    (793,'MCLUST02TEAM4','EVM','C411'),
    (794,'MCLUST02TEAM47','EVM','C411'),
    (795,'MCLUST03TEAM33','EVM','C411'),
    (796,'MCLUST03TEAM62','EVM','C411'),
    (797,'MCLUST01TEAM104','FDS','C422'),
    (798,'MCLUST01TEAM11','FDS','C422'),
    (799,'MCLUST01TEAM16','FDS','C422'),
    (800,'MCLUST01TEAM25','FDS','C422'),
    (801,'MCLUST01TEAM9','FDS','C422'),
    (802,'MCLUST02TEAM103','FDS','C422'),
    (803,'MCLUST02TEAM13','FDS','C422'),
    (804,'MCLUST02TEAM27','FDS','C422'),
    (805,'MCLUST02TEAM9','FDS','C422'),
    (806,'MCLUST03TEAM15','FDS','C422'),
    (807,'MCLUST03TEAM41','FDS','C422'),
    (808,'MCLUST03TEAM83','FDS','C422'),
    (809,'MCLUST01TEAM63','FHS','C425'),
    (810,'MCLUST01TEAM76','FHS','C425'),
    (811,'MCLUST02TEAM28','FHS','C425'),
    (812,'MCLUST02TEAM37','FHS','C425'),
    (813,'MCLUST02TEAM46','FHS','C425'),
    (814,'MCLUST02TEAM5','FHS','C425'),
    (815,'MCLUST03TEAM25','FHS','C425'),
    (816,'MCLUST03TEAM26','FHS','C425'),
    (817,'MCLUST03TEAM27','FHS','C425'),
    (818,'MCLUST03TEAM39','FHS','C425'),
    (819,'MCLUST03TEAM46','FHS','C425'),
    (820,'MCLUST01TEAM100','HLI','C525'),
    (821,'MCLUST01TEAM15','HLI','C525'),
    (822,'MCLUST01TEAM64','HLI','C525'),
    (823,'MCLUST01TEAM88','HLI','C525'),
    (824,'MCLUST01TEAM97','HLI','C525'),
    (825,'MCLUST02TEAM20','HLI','C525'),
    (826,'MCLUST02TEAM74','HLI','C525'),
    (827,'MCLUST02TEAM87','HLI','C525'),
    (828,'MCLUST02TEAM98','HLI','C525'),
    (829,'MCLUST03TEAM74','HLI','C525'),
    (830,'MCLUST03TEAM77','HLI','C525'),
    (831,'MCLUST01TEAM106','HWS','C625'),
    (832,'MCLUST01TEAM73','HWS','C625'),
    (833,'MCLUST02TEAM16','HWS','C625'),
    (834,'MCLUST02TEAM29','HWS','C625'),
    (835,'MCLUST02TEAM38','HWS','C625'),
    (836,'MCLUST02TEAM86','HWS','C625'),
    (837,'MCLUST02TEAM89','HWS','C625'),
    (838,'MCLUST03TEAM24','HWS','C625'),
    (839,'MCLUST03TEAM4','HWS','C625'),
    (840,'MCLUST03TEAM6','HWS','C625'),
    (841,'MCLUST03TEAM69','HWS','C625'),
    (842,'MCLUST01TEAM14','MPB','GroundFloorLab'),
    (843,'MCLUST01TEAM20','MPB','GroundFloorLab'),
    (844,'MCLUST01TEAM6','MPB','GroundFloorLab'),
    (845,'MCLUST01TEAM66','MPB','GroundFloorLab'),
    (846,'MCLUST02TEAM19','MPB','GroundFloorLab'),
    (847,'MCLUST03TEAM42','MPB','GroundFloorLab'),
    (848,'MCLUST01TEAM2','PFC','SixthFloorLab'),
    (849,'MCLUST01TEAM30','PFC','SixthFloorLab'),
    (850,'MCLUST01TEAM41','PFC','SixthFloorLab'),
    (851,'MCLUST01TEAM52','PFC','SixthFloorLab'),
    (852,'MCLUST02TEAM12','PFC','SixthFloorLab'),
    (853,'MCLUST02TEAM44','PFC','SixthFloorLab'),
    (854,'MCLUST02TEAM59','PFC','SixthFloorLab'),
    (855,'MCLUST02TEAM94','PFC','SixthFloorLab'),
    (856,'MCLUST03TEAM43','PFC','SixthFloorLab'),
    (857,'MCLUST03TEAM51','PFC','SixthFloorLab'),
    (858,'MCLUST03TEAM60','PFC','SixthFloorLab'),
    (859,'MCLUST03TEAM72','PFC','SixthFloorLab'),
    (860,'MCLUST01TEAM102','PJM','FirstFloorLab'),
    (861,'MCLUST01TEAM33','PJM','FirstFloorLab'),
    (862,'MCLUST01TEAM67','PJM','FirstFloorLab'),
    (863,'MCLUST01TEAM91','PJM','FirstFloorLab'),
    (864,'MCLUST02TEAM10','PJM','FirstFloorLab'),
    (865,'MCLUST02TEAM102','PJM','FirstFloorLab'),
    (866,'MCLUST02TEAM3','PJM','FirstFloorLab'),
    (867,'MCLUST02TEAM33','PJM','FirstFloorLab'),
    (868,'MCLUST02TEAM40','PJM','FirstFloorLab'),
    (869,'MCLUST02TEAM53','PJM','FirstFloorLab'),
    (870,'MCLUST02TEAM76','PJM','FirstFloorLab'),
    (871,'MCLUST01TEAM49','PMS','SecondFloorLab'),
    (872,'MCLUST01TEAM57','PMS','SecondFloorLab'),
    (873,'MCLUST01TEAM61','PMS','SecondFloorLab'),
    (874,'MCLUST01TEAM90','PMS','SecondFloorLab'),
    (875,'MCLUST01TEAM99','PMS','SecondFloorLab'),
    (876,'MCLUST02TEAM11','PMS','SecondFloorLab'),
    (877,'MCLUST02TEAM14','PMS','SecondFloorLab'),
    (878,'MCLUST02TEAM63','PMS','SecondFloorLab'),
    (879,'MCLUST02TEAM8','PMS','SecondFloorLab'),
    (880,'MCLUST03TEAM21','PMS','SecondFloorLab'),
    (881,'MCLUST03TEAM37','PMS','SecondFloorLab'),
    (882,'MCLUST03TEAM9','PMS','SecondFloorLab'),
    (883,'MCLUST01TEAM110','REM','C225'),
    (884,'MCLUST01TEAM24','REM','C225'),
    (885,'MCLUST01TEAM43','REM','C225'),
    (886,'MCLUST01TEAM75','REM','C225'),
    (887,'MCLUST01TEAM87','REM','C225'),
    (888,'MCLUST02TEAM34','REM','C225'),
    (889,'MCLUST02TEAM58','REM','C225'),
    (890,'MCLUST02TEAM7','REM','C225'),
    (891,'MCLUST02TEAM93','REM','C225'),
    (892,'MCLUST03TEAM12','REM','C225'),
    (893,'MCLUST03TEAM80','REM','C225'),
    (894,'MCLUST03TEAM81','REM','C225'),
    (895,'MCLUST01TEAM18','RES','ThirdFloorLab'),
    (896,'MCLUST01TEAM37','RES','ThirdFloorLab'),
    (897,'MCLUST01TEAM54','RES','ThirdFloorLab'),
    (898,'MCLUST01TEAM78','RES','ThirdFloorLab'),
    (899,'MCLUST01TEAM82','RES','ThirdFloorLab'),
    (900,'MCLUST01TEAM93','RES','ThirdFloorLab'),
    (901,'MCLUST02TEAM30','RES','ThirdFloorLab'),
    (902,'MCLUST02TEAM42','RES','ThirdFloorLab'),
    (903,'MCLUST02TEAM68','RES','ThirdFloorLab'),
    (904,'MCLUST02TEAM99','RES','ThirdFloorLab'),
    (905,'MCLUST03TEAM45','RES','ThirdFloorLab'),
    (906,'MCLUST03TEAM64','RES','ThirdFloorLab'),
    (907,'MCLUST01TEAM32','SAM','SixthFloorLab'),
    (908,'MCLUST01TEAM74','SAM','SixthFloorLab'),
    (909,'MCLUST02TEAM15','SAM','SixthFloorLab'),
    (910,'MCLUST02TEAM26','SAM','SixthFloorLab'),
    (911,'MCLUST02TEAM50','SAM','SixthFloorLab'),
    (912,'MCLUST02TEAM52','SAM','SixthFloorLab'),
    (913,'MCLUST02TEAM72','SAM','SixthFloorLab'),
    (914,'MCLUST02TEAM82','SAM','SixthFloorLab'),
    (915,'MCLUST03TEAM19','SAM','SixthFloorLab'),
    (916,'MCLUST03TEAM20','SAM','SixthFloorLab'),
    (917,'MCLUST03TEAM36','SAM','SixthFloorLab'),
    (918,'MCLUST03TEAM66','SAM','SixthFloorLab'),
    (919,'MCLUST01TEAM109','SCM','C625'),
    (920,'MCLUST01TEAM19','SCM','C625'),
    (921,'MCLUST01TEAM4','SCM','C625'),
    (922,'MCLUST01TEAM83','SCM','C625'),
    (923,'MCLUST02TEAM41','SCM','C625'),
    (924,'MCLUST03TEAM22','SCM','C625'),
    (925,'MCLUST03TEAM28','SCM','C625'),
    (926,'MCLUST03TEAM38','SCM','C625'),
    (927,'MCLUST01TEAM56','SEM','FourthFloorLab'),
    (928,'MCLUST01TEAM85','SEM','FourthFloorLab'),
    (929,'MCLUST02TEAM25','SEM','FourthFloorLab'),
    (930,'MCLUST02TEAM32','SEM','FourthFloorLab'),
    (931,'MCLUST02TEAM66','SEM','FourthFloorLab'),
    (932,'MCLUST02TEAM81','SEM','FourthFloorLab'),
    (933,'MCLUST02TEAM84','SEM','FourthFloorLab'),
    (934,'MCLUST03TEAM13','SEM','FourthFloorLab'),
    (935,'MCLUST03TEAM23','SEM','FourthFloorLab');'''
q2 = '''INSERT INTO pages_team VALUES
    (936,'MCLUST03TEAM55','SEM','FourthFloorLab'),
    (937,'MCLUST03TEAM61','SEM','FourthFloorLab'),
    (938,'MCLUST03TEAM76','SEM','FourthFloorLab'),
    (939,'MCLUST01TEAM1','SMS','GroundFloorLab'),
    (940,'MCLUST01TEAM27','SMS','GroundFloorLab'),
    (941,'MCLUST01TEAM84','SMS','GroundFloorLab'),
    (942,'MCLUST02TEAM36','SMS','GroundFloorLab'),
    (943,'MCLUST02TEAM48','SMS','GroundFloorLab'),
    (944,'MCLUST02TEAM65','SMS','GroundFloorLab'),
    (945,'MCLUST02TEAM67','SMS','GroundFloorLab'),
    (946,'MCLUST02TEAM95','SMS','GroundFloorLab'),
    (947,'MCLUST03TEAM40','SMS','GroundFloorLab'),
    (948,'MCLUST03TEAM48','SMS','GroundFloorLab'),
    (949,'MCLUST03TEAM65','SMS','GroundFloorLab'),
    (950,'MCLUST01TEAM10','TTH','C121'),
    (951,'MCLUST01TEAM101','TTH','C121'),
    (952,'MCLUST01TEAM108','TTH','C121'),
    (953,'MCLUST01TEAM70','TTH','C121'),
    (954,'MCLUST02TEAM43','TTH','C121'),
    (955,'MCLUST02TEAM54','TTH','C121'),
    (956,'MCLUST02TEAM64','TTH','C121'),
    (957,'MCLUST02TEAM90','TTH','C121'),
    (958,'MCLUST03TEAM47','TTH','C121'),
    (959,'MCLUST03TEAM49','TTH','C121'),
    (960,'MCLUST03TEAM68','TTH','C121');
'''

query = '''INSERT INTO pages_team VALUES
    (686,' EPC','MCLUST01TEAM12','C325'),
    (687,' EPC','MCLUST01TEAM21','C325'),
    (688,' EPC','MCLUST01TEAM23','C325'),
    (689,' EPC','MCLUST01TEAM89','C325'),
    (690,' EPC','MCLUST02TEAM100','C325'),
    (691,' EPC','MCLUST02TEAM104','C325'),
    (692,' EPC','MCLUST02TEAM79','C325'),
    (693,' EPC','MCLUST02TEAM92','C325'),
    (694,' EPC','MCLUST03TEAM35','C325'),
    (695,' EPC','MCLUST03TEAM44','C325'),
    (696,' EPC','MCLUST03TEAM78','C325'),
    (697,'AAS','MCLUST01TEAM103','C108'),
    (698,'AAS','MCLUST01TEAM3','C108'),
    (699,'AAS','MCLUST01TEAM31','C108'),
    (700,'AAS','MCLUST01TEAM5','C108'),
    (701,'AAS','MCLUST01TEAM62','C108'),
    (702,'AAS','MCLUST02TEAM31','C108'),
    (703,'AAS','MCLUST02TEAM60','C108'),
    (704,'AAS','MCLUST02TEAM75','C108'),
    (705,'AAS','MCLUST03TEAM11','C108'),
    (706,'AAS','MCLUST03TEAM70','C108'),
    (707,'AAS','MCLUST03TEAM75','C108'),
    (708,'AMS','MCLUST01TEAM28','C110'),
    (709,'AMS','MCLUST01TEAM51','C110'),
    (710,'AMS','MCLUST01TEAM69','C110'),
    (711,'AMS','MCLUST01TEAM86','C110'),
    (712,'AMS','MCLUST01TEAM96','C110'),
    (713,'AMS','MCLUST01TEAM98','C110'),
    (714,'AMS','MCLUST02TEAM55','C110'),
    (715,'AMS','MCLUST02TEAM69','C110'),
    (716,'AMS','MCLUST02TEAM83','C110'),
    (717,'AMS','MCLUST03TEAM34','C110'),
    (718,'AMS','MCLUST03TEAM59','C110'),
    (719,'APS ','MCLUST01TEAM71','C121'),
    (720,'APS ','MCLUST01TEAM77','C121'),
    (721,'APS ','MCLUST02TEAM39','C121'),
    (722,'APS ','MCLUST02TEAM6','C121'),
    (723,'APS ','MCLUST02TEAM61','C121'),
    (724,'APS ','MCLUST02TEAM78','C121'),
    (725,'APS ','MCLUST02TEAM97','C121'),
    (726,'APS ','MCLUST03TEAM16','C121'),
    (727,'APS ','MCLUST03TEAM17','C121'),
    (728,'APS ','MCLUST03TEAM5','C121'),
    (729,'APS ','MCLUST03TEAM79','C121'),
    (730,'BDS','MCLUST01TEAM13','C225'),
    (731,'BDS','MCLUST01TEAM39','C225'),
    (732,'BDS','MCLUST01TEAM50','C225'),
    (733,'BDS','MCLUST01TEAM53','C225'),
    (734,'BDS','MCLUST01TEAM58','C225'),
    (735,'BDS','MCLUST01TEAM59','C225'),
    (736,'BDS','MCLUST02TEAM77','C225'),
    (737,'BDS','MCLUST03TEAM18','C225'),
    (738,'BDS','MCLUST03TEAM29','C225'),
    (739,'BDS','MCLUST03TEAM30','C225'),
    (740,'BDS','MCLUST03TEAM50','C225'),
    (741,'BDS','MCLUST03TEAM8','C225'),
    (742,'BFS','MCLUST01TEAM22','C308'),
    (743,'BFS','MCLUST01TEAM38','C308'),
    (744,'BFS','MCLUST02TEAM21','C308'),
    (745,'BFS','MCLUST02TEAM56','C308'),
    (746,'BFS','MCLUST02TEAM57','C308'),
    (747,'BFS','MCLUST02TEAM62','C308'),
    (748,'BFS','MCLUST02TEAM73','C308'),
    (749,'BFS','MCLUST02TEAM88','C308'),
    (750,'BFS','MCLUST03TEAM10','C308'),
    (751,'BFS','MCLUST03TEAM54','C308'),
    (752,'BFS','MCLUST03TEAM56','C308'),
    (753,'BMS','MCLUST01TEAM29','C321B2'),
    (754,'BMS','MCLUST01TEAM34','C321B2'),
    (755,'BMS','MCLUST01TEAM35','C321B2'),
    (756,'BMS','MCLUST01TEAM40','C321B2'),
    (757,'BMS','MCLUST01TEAM80','C321B2'),
    (758,'BMS','MCLUST02TEAM17','C321B2'),
    (759,'BMS','MCLUST02TEAM49','C321B2'),
    (760,'BMS','MCLUST02TEAM91','C321B2'),
    (761,'BMS','MCLUST03TEAM32','C321B2'),
    (762,'BMS','MCLUST03TEAM63','C321B2'),
    (763,'BMS','MCLUST03TEAM7','C321B2'),
    (764,'ERP','MCLUST01TEAM105','C121'),
    (765,'ERP','MCLUST01TEAM45','C121'),
    (766,'ERP','MCLUST01TEAM47','C121'),
    (767,'ERP','MCLUST02TEAM45','C121'),
    (768,'ERP','MCLUST02TEAM70','C121'),
    (769,'ERP','MCLUST02TEAM71','C121'),
    (770,'ERP','MCLUST03TEAM14','C121'),
    (771,'ERP','MCLUST03TEAM3','C121'),
    (772,'ERP','MCLUST03TEAM71','C121'),
    (773,'ERP','MCLUST03TEAM73','C121'),
    (774,'ERP','MCLUST03TEAM84','C121'),
    (775,'ETS','MCLUST01TEAM17','C407'),
    (776,'ETS','MCLUST01TEAM26','C407'),
    (777,'ETS','MCLUST01TEAM36','C407'),
    (778,'ETS','MCLUST01TEAM44','C407'),
    (779,'ETS','MCLUST01TEAM46','C407'),
    (780,'ETS','MCLUST01TEAM60','C407'),
    (781,'ETS','MCLUST01TEAM79','C407'),
    (782,'ETS','MCLUST02TEAM18','C407'),
    (783,'ETS','MCLUST02TEAM35','C407'),
    (784,'ETS','MCLUST02TEAM51','C407'),
    (785,'ETS','MCLUST03TEAM31','C407'),
    (786,'EVM','MCLUST01TEAM42','C411'),
    (787,'EVM','MCLUST01TEAM48','C411'),
    (788,'EVM','MCLUST01TEAM72','C411'),
    (789,'EVM','MCLUST01TEAM81','C411'),
    (790,'EVM','MCLUST01TEAM92','C411'),
    (791,'EVM','MCLUST02TEAM23','C411'),
    (792,'EVM','MCLUST02TEAM24','C411'),
    (793,'EVM','MCLUST02TEAM4','C411'),
    (794,'EVM','MCLUST02TEAM47','C411'),
    (795,'EVM','MCLUST03TEAM33','C411'),
    (796,'EVM','MCLUST03TEAM62','C411'),
    (797,'FDS','MCLUST01TEAM104','C422'),
    (798,'FDS','MCLUST01TEAM11','C422'),
    (799,'FDS','MCLUST01TEAM16','C422'),
    (800,'FDS','MCLUST01TEAM25','C422'),
    (801,'FDS','MCLUST01TEAM9','C422'),
    (802,'FDS','MCLUST02TEAM103','C422'),
    (803,'FDS','MCLUST02TEAM13','C422'),
    (804,'FDS','MCLUST02TEAM27','C422'),
    (805,'FDS','MCLUST02TEAM9','C422'),
    (806,'FDS','MCLUST03TEAM15','C422'),
    (807,'FDS','MCLUST03TEAM41','C422'),
    (808,'FDS','MCLUST03TEAM83','C422'),
    (809,'FHS','MCLUST01TEAM63','C425'),
    (810,'FHS','MCLUST01TEAM76','C425'),
    (811,'FHS','MCLUST02TEAM28','C425'),
    (812,'FHS','MCLUST02TEAM37','C425'),
    (813,'FHS','MCLUST02TEAM46','C425'),
    (814,'FHS','MCLUST02TEAM5','C425'),
    (815,'FHS','MCLUST03TEAM25','C425'),
    (816,'FHS','MCLUST03TEAM26','C425'),
    (817,'FHS','MCLUST03TEAM27','C425'),
    (818,'FHS','MCLUST03TEAM39','C425'),
    (819,'FHS','MCLUST03TEAM46','C425'),
    (820,'HLI','MCLUST01TEAM100','C525'),
    (821,'HLI','MCLUST01TEAM15','C525'),
    (822,'HLI','MCLUST01TEAM64','C525'),
    (823,'HLI','MCLUST01TEAM88','C525'),
    (824,'HLI','MCLUST01TEAM97','C525'),
    (825,'HLI','MCLUST02TEAM20','C525'),
    (826,'HLI','MCLUST02TEAM74','C525'),
    (827,'HLI','MCLUST02TEAM87','C525'),
    (828,'HLI','MCLUST02TEAM98','C525'),
    (829,'HLI','MCLUST03TEAM74','C525'),
    (830,'HLI','MCLUST03TEAM77','C525'),
    (831,'HWS','MCLUST01TEAM106','C625'),
    (832,'HWS','MCLUST01TEAM73','C625'),
    (833,'HWS','MCLUST02TEAM16','C625'),
    (834,'HWS','MCLUST02TEAM29','C625'),
    (835,'HWS','MCLUST02TEAM38','C625'),
    (836,'HWS','MCLUST02TEAM86','C625'),
    (837,'HWS','MCLUST02TEAM89','C625'),
    (838,'HWS','MCLUST03TEAM24','C625'),
    (839,'HWS','MCLUST03TEAM4','C625'),
    (840,'HWS','MCLUST03TEAM6','C625'),
    (841,'HWS','MCLUST03TEAM69','C625'),
    (842,'MPB','MCLUST01TEAM14','GroundFloorLab'),
    (843,'MPB','MCLUST01TEAM20','GroundFloorLab'),
    (844,'MPB','MCLUST01TEAM6','GroundFloorLab'),
    (845,'MPB','MCLUST01TEAM66','GroundFloorLab'),
    (846,'MPB','MCLUST02TEAM19','GroundFloorLab'),
    (847,'MPB','MCLUST03TEAM42','GroundFloorLab'),
    (848,'PFC','MCLUST01TEAM2','SixthFloorLab'),
    (849,'PFC','MCLUST01TEAM30','SixthFloorLab'),
    (850,'PFC','MCLUST01TEAM41','SixthFloorLab'),
    (851,'PFC','MCLUST01TEAM52','SixthFloorLab'),
    (852,'PFC','MCLUST02TEAM12','SixthFloorLab'),
    (853,'PFC','MCLUST02TEAM44','SixthFloorLab'),
    (854,'PFC','MCLUST02TEAM59','SixthFloorLab'),
    (855,'PFC','MCLUST02TEAM94','SixthFloorLab'),
    (856,'PFC','MCLUST03TEAM43','SixthFloorLab'),
    (857,'PFC','MCLUST03TEAM51','SixthFloorLab'),
    (858,'PFC','MCLUST03TEAM60','SixthFloorLab'),
    (859,'PFC','MCLUST03TEAM72','SixthFloorLab'),
    (860,'PJM','MCLUST01TEAM102','FirstFloorLab'),
    (861,'PJM','MCLUST01TEAM33','FirstFloorLab'),
    (862,'PJM','MCLUST01TEAM67','FirstFloorLab'),
    (863,'PJM','MCLUST01TEAM91','FirstFloorLab'),
    (864,'PJM','MCLUST02TEAM10','FirstFloorLab'),
    (865,'PJM','MCLUST02TEAM102','FirstFloorLab'),
    (866,'PJM','MCLUST02TEAM3','FirstFloorLab'),
    (867,'PJM','MCLUST02TEAM33','FirstFloorLab'),
    (868,'PJM','MCLUST02TEAM40','FirstFloorLab'),
    (869,'PJM','MCLUST02TEAM53','FirstFloorLab'),
    (870,'PJM','MCLUST02TEAM76','FirstFloorLab'),
    (871,'PMS','MCLUST01TEAM49','SecondFloorLab'),
    (872,'PMS','MCLUST01TEAM57','SecondFloorLab'),
    (873,'PMS','MCLUST01TEAM61','SecondFloorLab'),
    (874,'PMS','MCLUST01TEAM90','SecondFloorLab'),
    (875,'PMS','MCLUST01TEAM99','SecondFloorLab'),
    (876,'PMS','MCLUST02TEAM11','SecondFloorLab'),
    (877,'PMS','MCLUST02TEAM14','SecondFloorLab'),
    (878,'PMS','MCLUST02TEAM63','SecondFloorLab'),
    (879,'PMS','MCLUST02TEAM8','SecondFloorLab'),
    (880,'PMS','MCLUST03TEAM21','SecondFloorLab'),
    (881,'PMS','MCLUST03TEAM37','SecondFloorLab'),
    (882,'PMS','MCLUST03TEAM9','SecondFloorLab'),
    (883,'REM','MCLUST01TEAM110','C225'),
    (884,'REM','MCLUST01TEAM24','C225'),
    (885,'REM','MCLUST01TEAM43','C225'),
    (886,'REM','MCLUST01TEAM75','C225'),
    (887,'REM','MCLUST01TEAM87','C225'),
    (888,'REM','MCLUST02TEAM34','C225'),
    (889,'REM','MCLUST02TEAM58','C225'),
    (890,'REM','MCLUST02TEAM7','C225'),
    (891,'REM','MCLUST02TEAM93','C225'),
    (892,'REM','MCLUST03TEAM12','C225'),
    (893,'REM','MCLUST03TEAM80','C225'),
    (894,'REM','MCLUST03TEAM81','C225'),
    (895,'RES','MCLUST01TEAM18','ThirdFloorLab'),
    (896,'RES','MCLUST01TEAM37','ThirdFloorLab'),
    (897,'RES','MCLUST01TEAM54','ThirdFloorLab'),
    (898,'RES','MCLUST01TEAM78','ThirdFloorLab'),
    (899,'RES','MCLUST01TEAM82','ThirdFloorLab'),
    (900,'RES','MCLUST01TEAM93','ThirdFloorLab'),
    (901,'RES','MCLUST02TEAM30','ThirdFloorLab'),
    (902,'RES','MCLUST02TEAM42','ThirdFloorLab'),
    (903,'RES','MCLUST02TEAM68','ThirdFloorLab'),
    (904,'RES','MCLUST02TEAM99','ThirdFloorLab'),
    (905,'RES','MCLUST03TEAM45','ThirdFloorLab'),
    (906,'RES','MCLUST03TEAM64','ThirdFloorLab'),
    (907,'SAM','MCLUST01TEAM32','SixthFloorLab'),
    (908,'SAM','MCLUST01TEAM74','SixthFloorLab'),
    (909,'SAM','MCLUST02TEAM15','SixthFloorLab'),
    (910,'SAM','MCLUST02TEAM26','SixthFloorLab'),
    (911,'SAM','MCLUST02TEAM50','SixthFloorLab'),
    (912,'SAM','MCLUST02TEAM52','SixthFloorLab'),
    (913,'SAM','MCLUST02TEAM72','SixthFloorLab'),
    (914,'SAM','MCLUST02TEAM82','SixthFloorLab'),
    (915,'SAM','MCLUST03TEAM19','SixthFloorLab'),
    (916,'SAM','MCLUST03TEAM20','SixthFloorLab'),
    (917,'SAM','MCLUST03TEAM36','SixthFloorLab'),
    (918,'SAM','MCLUST03TEAM66','SixthFloorLab'),
    (919,'SCM','MCLUST01TEAM109','C625'),
    (920,'SCM','MCLUST01TEAM19','C625'),
    (921,'SCM','MCLUST01TEAM4','C625'),
    (922,'SCM','MCLUST01TEAM83','C625'),
    (923,'SCM','MCLUST02TEAM41','C625'),
    (924,'SCM','MCLUST03TEAM22','C625'),
    (925,'SCM','MCLUST03TEAM28','C625'),
    (926,'SCM','MCLUST03TEAM38','C625'),
    (927,'SEM','MCLUST01TEAM56','FourthFloorLab'),
    (928,'SEM','MCLUST01TEAM85','FourthFloorLab'),
    (929,'SEM','MCLUST02TEAM25','FourthFloorLab'),
    (930,'SEM','MCLUST02TEAM32','FourthFloorLab'),
    (931,'SEM','MCLUST02TEAM66','FourthFloorLab'),
    (932,'SEM','MCLUST02TEAM81','FourthFloorLab'),
    (933,'SEM','MCLUST02TEAM84','FourthFloorLab'),
    (934,'SEM','MCLUST03TEAM13','FourthFloorLab'),
    (935,'SEM','MCLUST03TEAM23','FourthFloorLab');'''

query2 = '''INSERT INTO pages_team VALUES
    (936,'SEM','MCLUST03TEAM55','FourthFloorLab'),
    (937,'SEM','MCLUST03TEAM61','FourthFloorLab'),
    (938,'SEM','MCLUST03TEAM76','FourthFloorLab'),
    (939,'SMS','MCLUST01TEAM1','GroundFloorLab'),
    (940,'SMS','MCLUST01TEAM27','GroundFloorLab'),
    (941,'SMS','MCLUST01TEAM84','GroundFloorLab'),
    (942,'SMS','MCLUST02TEAM36','GroundFloorLab'),
    (943,'SMS','MCLUST02TEAM48','GroundFloorLab'),
    (944,'SMS','MCLUST02TEAM65','GroundFloorLab'),
    (945,'SMS','MCLUST02TEAM67','GroundFloorLab'),
    (946,'SMS','MCLUST02TEAM95','GroundFloorLab'),
    (947,'SMS','MCLUST03TEAM40','GroundFloorLab'),
    (948,'SMS','MCLUST03TEAM48','GroundFloorLab'),
    (949,'SMS','MCLUST03TEAM65','GroundFloorLab'),
    (950,'TTH','MCLUST01TEAM10','C121'),
    (951,'TTH','MCLUST01TEAM101','C121'),
    (952,'TTH','MCLUST01TEAM108','C121'),
    (953,'TTH','MCLUST01TEAM70','C121'),
    (954,'TTH','MCLUST02TEAM43','C121'),
    (955,'TTH','MCLUST02TEAM54','C121'),
    (956,'TTH','MCLUST02TEAM64','C121'),
    (957,'TTH','MCLUST02TEAM90','C121'),
    (958,'TTH','MCLUST03TEAM47','C121'),
    (959,'TTH','MCLUST03TEAM49','C121'),
    (960,'TTH','MCLUST03TEAM68','C121');
'''

cur.execute(q1);
cur.execute(q2);

con.commit();
