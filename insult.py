from random import randrange

# phareses taken from https://www.literarygenius.info/a1-shakespearean-insults-generator.htm

first_phrase = ["artless","bawdy","beslubbering","bootless","churlish","clouted",
"cockered","craven","currish","dankish","dissembling","droning","errant","fawning",
"fobbing","frothy","froward","gleeking","goatish","gorbellied","impertinent",
"infectious","jarring","loggerheaded","lumpish","mammering","mangled","mewling",
"paunchy","pribbling","puking","puny","qualling","rank","reeky","roguish","ruttish",
"saucy","spleeny","spongy","surly","tottering","unmuzzled","vain","venomed",
"villainous","warped","wayward","weedy","yeasty","abominable","accursed","adulterate","arrogant","babbling",
"barbarous","base","mumbling","overwheening","perfidious","pestilent","poisonous","pragging","rancorous","rascally",
"sanctimonious","shameless","slanderous","soulless","spongey","crusty","withered","loathed",
"tongueless","traitorous","unwholesome","viperous","greasy","obscene","beggarly","scandalous","creeping",
"lascivious","degenerate","meddling"]
second_phrase = ["base-court","prick-eared","puisny-tilted","puke-stockinged","open-arsed","bat-fowling","beef-witted","beetle-headed",
"boil-brained","clapper-clawed","clay-brained","common-kissing","crook-pated",
"dismal-dreaming","dizzy-eyed","doghearted","dread-bolted","earth-vexing",
"elf-skinned","fat-kidneyed","fen-sucked","flap-mouthed","fly-bitten",
"folly-fallen","fool-born","full-gorged","guts-griping","half-faced","hasty-witted",
"hedge-born","hell-hated","idle-headed","ill-bred","ill-nurtured","knotty-pated",
"milk-livered","motley-minded","onion-eyed","plume-plucked","pottle-deep",
"pox-marked","reeling-ripe","rough-hewn","rude-growing","rump-fed","shard-borne",
"sheep-biting","spur-galled","swag-bellied","tardy-gaited","tickle-brained","white-livered",
"toad-spotted","urchin-snouted","weather-bitten","shag-haired","tallow-faced","beef-witted",
"decayed","deformed","muddy-mottled","hag-born","long-tongued","toad-spotted"]
third_phrase = ["baggage","barnacle","bladder","boar-pig","bugbear",
"bum-bailey","canker-blossom","clack-dish","clotpole","codpiece","coxcomb","death-token",
"dewberry","flap-dragon","flax-wench","flirt-gill","foot-licker","fustilarian",
"giglet","gudgeon","haggard","harpy","hedge-pig","horn-beast","hugger-mugger",
"joithead","lewdster","lout","maggot-pie","malt-worm","mammet","measle","minnow",
"miscreant","moldwarp","mumble-news","nut-hook","pigeon-egg","pignut","pumpion",
"puttock","ratsbane","scut","skainsmate","strumpet","varlet","vassal","wagtail",
"whey-face","scullion","serpents-egg","callet","slug","bag of guts","punk","bitch-wolf","botch","withered-hag",
"mangy-dog","foul deformity","odiferous stench","no bowels","drunkard","turd","bear-whelp","eunuch",
"devil-incarnate","filthy rogue","vile worm","writhled shrimp","scurvy-knave","whore-master","malt-horse",
"varlet","worms-meat","canker-blossom","carrion","hag-seed","ruinous-butt","contriver","hypocrite","infection",
"imbossed carbunkle","eternal devil","execrable-wretch","murderous coward","foul adulterer","ingested-lump","wrinkled-witch",
"plebian","strumpet","horse-drench","promise-breaker","incontinent varlet","leprous witch","babbling gossip",
"tyrant","purified-cur","misbegotten-divel","mildewed-ear"]


def status_text(): 
    return f"Thou {first_phrase[randrange(0, len(first_phrase))]} {second_phrase[randrange(0, len(second_phrase))]} {third_phrase[randrange(0, len(third_phrase))]}"
