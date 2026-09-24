# Curated logos — authentic art from fastfetch repo (src/logo/ascii/*).
# Keys = lowercase os-release ID slugs, matching collect.py "OS ID" field.
# $N color markers kept — view.py converts them to rich colors at render.
# "linux" = fallback for unknown distros.
LOGOS = {
    "cachyos": r'''

           $3.$1-------------------------:
          .$2+=$1========================.
         :$2++$1===$2++===$1===============-       :$2++$1-
        :$2*++$1====$2+++++==$1===========-        .==:
       -$2*+++$1=====$2+***++=$1=========:
      =$2*++++=$1=======------------:
     =$2*+++++=$1====-                     $3...$1
   .$2+*+++++$1=-===:                    .$2=+++=$1:
  :$2++++$1=====-==:                     -***$2**$1+
 :$2++=$1=======-=.                      .=+**+$3.$1
.$2+$1==========-.                          $3.$1
 :$2+++++++$1====-                                $3.$1--==-$3.$1
  :$2++$1==========.                             $3:$2+++++++$1$3:
   $1.-===========.                            =*****+*+
    $1.-===========:                           .+*****+:
      $1-=======$2++++$1:::::::::::::::::::::::::-:  $3.$1---:
       :======$2++++$1====$2+++******************=.
        $1:=====$2+++$1==========$2++++++++++++++*-
         $1.====$2++$1==============$2++++++++++*-
          $1.===$2+$1==================$2+++++++:
           $1.-=======================$2+++:
             $3..........................


''',
    "arch": r'''

                  -`
                 .o+`
                `ooo/
               `+oooo:
              `+oooooo:
              -+oooooo+:
            `/:-:++oooo+:
           `/++++/+++++++:
          `/++++++++++++++:
         `/+++o$2oooooooo$1oooo/`
        ./$2ooosssso++osssssso$1+`
$2       .oossssso-````/ossssss+`
      -osssssso.      :ssssssso.
     :osssssss/        osssso+++.
    /ossssssss/        +ssssooo/-
  `/ossssso+/:-        -:/+osssso+-
 `+sso+:-`                 `.-/+oso:
`++:.                           `-/+/
.`                                 `/


''',
    "fedora": r'''

             .',;::::;,'.
         .';:cccccccccccc:;,.
      .;cccccccccccccccccccccc;.
    .:cccccccccccccccccccccccccc:.
  .;ccccccccccccc;$2.:dddl:.$1;ccccccc;.
 .:ccccccccccccc;$2OWMKOOXMWd$1;ccccccc:.
.:ccccccccccccc;$2KMMc$1;cc;$2xMMc$1;ccccccc:.
,cccccccccccccc;$2MMM.$1;cc;$2;WW:$1;cccccccc,
:cccccccccccccc;$2MMM.$1;cccccccccccccccc:
:ccccccc;$2oxOOOo$1;$2MMM000k.$1;cccccccccccc:
cccccc;$20MMKxdd:$1;$2MMMkddc.$1;cccccccccccc;
ccccc;$2XMO'$1;cccc;$2MMM.$1;cccccccccccccccc'
ccccc;$2MMo$1;ccccc;$2MMW.$1;ccccccccccccccc;
ccccc;$20MNc.$1ccc$2.xMMd$1;ccccccccccccccc;
cccccc;$2dNMWXXXWM0:$1;cccccccccccccc:,
cccccccc;$2.:odl:.$1;cccccccccccccc:,.
ccccccccccccccccccccccccccccc:'.
:ccccccccccccccqccccccccccc:;,..
  ':cccccccccccccccc::;,..


''',
    "ubuntu": r'''

                             ....
              $2.',:clooo:  $1.:looooo:.
           $2.;looooooooc  $1.oooooooooo'
        $2.;looooool:,''.  $1:ooooooooooc
       $2;looool;.         'oooooooooo,
      $2;clool'             .cooooooc.  $2,,
         $2...                ......  .:oo,
  $1.;clol:,.                        $2.loooo'
 $1:ooooooooo,                        'ooool
$1'ooooooooooo.                        loooo.
$1'ooooooooool                         coooo.
 $1,loooooooc.                        .loooo.
   $1.,;;;'.                          ;ooooc
       $2...                         ,ooool.
    $2.cooooc.              $1..',,'.  $2.cooo.
      $2;ooooo:.           $1;oooooooc.  $2:l.
       $2.coooooc,..      $1coooooooooo.
         $2.:ooooooolc:. $1.ooooooooooo'
           $2.':loooooo;  $1,oooooooooc
               $2..';::c'  $1.;loooo:'


''',
    "linux": r'''

        $2#####
       $2#######
       $2##$1O$2#$1O$2##
       $2#$3#####$2#
     $2##$1##$3###$1##$2##
    $2#$1##########$2##
   $2#$1############$2##
   $2#$1############$2###
  $3##$2#$1###########$2##$3#
$3######$2#$1#######$2#$3######
$3#######$2#$1#####$2#$3#######
  $3#####$2#######$3#####


''',
    "windows": r'''

$1/////////////////  $2/////////////////
$1/////////////////  $2/////////////////
$1/////////////////  $2/////////////////
$1/////////////////  $2/////////////////
$1/////////////////  $2/////////////////
$1/////////////////  $2/////////////////
$1/////////////////  $2/////////////////
$1/////////////////  $2/////////////////

$3/////////////////  $4/////////////////
$3/////////////////  $4/////////////////
$3/////////////////  $4/////////////////
$3/////////////////  $4/////////////////
$3/////////////////  $4/////////////////
$3/////////////////  $4/////////////////
$3/////////////////  $4/////////////////
$3/////////////////  $4/////////////////


''',
    "macos": r'''

                    'c.
                 ,xNMM.
               .OMMMMo
               lMM"
     .;loddo:.  .olloddol;.
   cKMMMMMMMMMMNWMMMMMMMMMM0:
 $2.KMMMMMMMMMMMMMMMMMMMMMMMWd.
 XMMMMMMMMMMMMMMMMMMMMMMMX.
$3;MMMMMMMMMMMMMMMMMMMMMMMM:
:MMMMMMMMMMMMMMMMMMMMMMMM:
$4.MMMMMMMMMMMMMMMMMMMMMMMMX.
 kMMMMMMMMMMMMMMMMMMMMMMMMWd.
 $5'XMMMMMMMMMMMMMMMMMMMMMMMMMMk
  'XMMMMMMMMMMMMMMMMMMMMMMMMK.
    $6kMMMMMMMMMMMMMMMMMMMMMMd
     ;KMMMMMMMWXXWMMMMMMMk.
       "cooc*"    "*coo'"


''',
    "alpine": r'''       .hddddddddddddddddddddddh.
      :dddddddddddddddddddddddddd:
     /dddddddddddddddddddddddddddd/
    +dddddddddddddddddddddddddddddd+
  `sdddddddddddddddddddddddddddddddds`
 `ydddddddddddd++hdddddddddddddddddddy`
.hddddddddddd+`  `+ddddh:-sdddddddddddh.
hdddddddddd+`      `+y:    .sddddddddddh
ddddddddh+`   `//`   `.`     -sddddddddd
ddddddh+`   `/hddh/`   `:s-    -sddddddd
ddddh+`   `/+/dddddh/`   `+s-    -sddddd
ddd+`   `/o` :dddddddh/`   `oy-    .yddd
hdddyo+ohddyosdddddddddho+oydddy++ohdddh
.hddddddddddddddddddddddddddddddddddddh.
 `yddddddddddddddddddddddddddddddddddy`
  `sdddddddddddddddddddddddddddddddds`
    +dddddddddddddddddddddddddddddd+
     /dddddddddddddddddddddddddddd/
      :dddddddddddddddddddddddddd:
       .hddddddddddddddddddddddh.
''',
    "artix": r'''                   '
                  'o'
                 'ooo'
                'ooxoo'
               'ooxxxoo'
              'oookkxxoo'
             'oiioxkkxxoo'
            ':;:iiiioxxxoo'
               `'.;::ioxxoo'
          '-.      `':;jiooo'
         'oooio-..     `'i:io'
        'ooooxxxxoio:,.   `'-;'
       'ooooxxxxxkkxoooIi:-.  `'
      'ooooxxxxxkkkkxoiiiiiji'
     'ooooxxxxxkxxoiiii:'`     .i'
    'ooooxxxxxoi:::'`       .;ioxo'
   'ooooxooi::'`         .:iiixkxxo'
  'ooooi:'`                `'';ioxxo'
 'i:'`                          '':io'
'`                                   `'
''',
    "debian": r'''        
        $2_,met$$$$$$$$$$gg.
     ,g$$$$$$$$$$$$$$$$$$$$$P.
   ,g$$$$P""       """Y$$$$.".
  ,$$$$P'              `$$$$$$.
',$$$$P       ,ggs.     `$$$$b:
`d$$$$'     ,$P"'   $1.$2    $$$$$$
 $$$$P      d$'     $1,$2    $$$$P
 $$$$:      $$$.   $1-$2    ,d$$$$'
 $$$$;      Y$b._   _,d$P'
 Y$$$$.    $1`.$2`"Y$$$$$$$$P"'
 `$$$$b      $1"-.__
  $2`Y$$$$b
   `Y$$$$.
     `$$$$b.
       `Y$$$$b.
         `"Y$$b._
             `""""
''',
    "elementary": r'''         eeeeeeeeeeeeeeeee
      eeeeeeeeeeeeeeeeeeeeeee
    eeeee  eeeeeeeeeeee   eeeee
  eeee   eeeee       eee     eeee
 eeee   eeee          eee     eeee
eee    eee            eee       eee
eee   eee            eee        eee
ee    eee           eeee       eeee
ee    eee         eeeee      eeeeee
ee    eee       eeeee      eeeee ee
eee   eeee   eeeeee      eeeee  eee
eee    eeeeeeeeee     eeeeee    eee
 eeeeeeeeeeeeeeeeeeeeeeee    eeeee
  eeeeeeee eeeeeeeeeeee      eeee
    eeeee                 eeeee
      eeeeeee         eeeeeee
         eeeeeeeeeeeeeeeee
''',
    "endeavouros": r'''                     $2./$1o$3.
                   $2./$1sssso$3-
                 $2`:$1osssssss+$3-
               $2`:+$1sssssssssso$3/.
             $2`-/o$1ssssssssssssso$3/.
           $2`-/+$1sssssssssssssssso$3+:`
         $2`-:/+$1sssssssssssssssssso$3+/.
       $2`.://o$1sssssssssssssssssssso$3++-
      $2.://+$1ssssssssssssssssssssssso$3++:
    $2.:///o$1ssssssssssssssssssssssssso$3++:
  $2`:////$1ssssssssssssssssssssssssssso$3+++.
$2`-////+$1ssssssssssssssssssssssssssso$3++++-
 $2`..-+$1oosssssssssssssssssssssssso$3+++++/`
   $3./++++++++++++++++++++++++++++++/:.
  `:::::::::::::::::::::::::------``
''',
    "garuda": r'''                   .%;888:8898898:
                 x;XxXB%89b8:b8%b88:
              .8Xxd                8X:.
            .8Xx;                    8x:.
          .tt8x          .d            x88;
       .@8x8;          .db:              xx@;
     ,tSXX°          .bbbbbbbbbbbbbbbbbbbB8x@;
   .SXxx            bBBBBBBBBBBBBBBBBBBBbSBX8;
 ,888S                                     pd!
8X88/                                       q
8X88/
GBB.
 x%88        d888@8@X@X@X88X@@XX@@X@8@X.
   dxXd    dB8b8b8B8B08bB88b998888b88x.
    dxx8o                      .@@;.
      dx88                   .t@x.
        d:SS@8ba89aa67a853Sxxad.
          .d988999889889899dd.
''',
    "kali": r"""..............
            ..,;:ccc,.
          ......''';lxO.
.....''''..........,:ld;
           .';;;:::;,,.x,
      ..'''.            0Xxoc:,.  ...
  ....                ,ONkc;,;cokOdc',.
 .                   OMo           ':$2dd$1o.
                    dMc               :OO;
                    0M.                 .:o.
                    ;Wd
                     ;XO,
                       ,d0Odlc;,..
                           ..',;:cdOOd::,.
                                    .:d;.':;.
                                       'd,  .'
                                         ;l   ..
                                          .o
                                            c
                                            .'
                                             .
""",
    "linuxmint": r'''            $2_.-ppOOOOOOqq-._
         .oOOOOPPPPPPPPPPOOOOo.
      .oOOOO$1.=oOOOOOOOOOOo=.$2OOOOo.
    .:OOO$1.=oOOOOOOOOOOOOOOOOo=.$2OOO:.
   .OOO$1.OOOOOOOOOOOOOOOOOOOOOOOO.$2OOO.
  .OOO$1.OO    OOO:´   `::´    `:OOO.$2OO:
 .OOO$1.OOO    OO                OOO.$2OOO:
 OOO$1.OOOO    OO    oo    oo    OOOO.$2OOO
:OOO$1:OOOO    OO    OO    OO    OOOO:$2OOO:
:OOO$1:OOOO    OO    OO    OO    OOOO:$2OOO:
'OOO$1'OOOO    OO    OO    OO    OOOO'$2OOO'
 OOO$1'OOOO    OO____OO____OO    OOOO'$2OOO'
 'OOO$1'OOO    'OOOOOOOOOOOO'    OOOO'$2OOO
  'OOO$1'OOO                    .OOO'$2OOO'
   'OOO$1'OOOO:ooooooooooooooo:OOOO'$2OOO'
    ':OOOo$1'=OOOOOOOOOOOOOOOOO='$2oOOO:'
      ':OOOOo$1'=OOOOOOOOOOO='$2oOOOO:'
         ``-OOOOooooooooooOOOO-´´
             ```-=:OOOO:=-´´´
''',
    "manjaro": r'''██████████████████  ████████
██████████████████  ████████
██████████████████  ████████
██████████████████  ████████
████████            ████████
████████  ████████  ████████
████████  ████████  ████████
████████  ████████  ████████
████████  ████████  ████████
████████  ████████  ████████
████████  ████████  ████████
████████  ████████  ████████
████████  ████████  ████████
████████  ████████  ████████
''',
    "opensuse": r"""           $2.;ldkO0000Okdl;.
       .;d00xl:^''''''^:ok00d;.
     .d00l'                'o00d.
   .d0Kd'$1  Okxol:;,.          $2:O0d
  .OK$1KKK0kOKKKKKKKKKKOxo:,      $2lKO.
 ,0K$1KKKKKKKKKKKKKKK0P^$2,,,$1^dx:$2    ;00,
.OK$1KKKKKKKKKKKKKKKk'$2.oOPPb.$1'0k.$2   cKO.
:KK$1KKKKKKKKKKKKKKK: $2kKx..dd $1lKd$2   'OK:
dKK$1KKKKKKKKKOx0KKKd $2^0KKKO' $1kKKc$2   dKd
dKK$1KKKKKKKKKK;.;oOKx,..$2^$1..;kKKK0.$2  dKd
:KK$1KKKKKKKKKK0o;...^cdxxOK0O/^^'  $2.0K:
 kKK$1KKKKKKKKKKKKK0x;,,......,;od  $2lKk
 '0K$1KKKKKKKKKKKKKKKKKKKK00KKOo^  $2c00'
  'kK$1KKOxddxkOO00000Okxoc;''   $2.dKk'
    l0Ko.                    .c00l'
     'l0Kk:.              .;xK0l'
        'lkK0xl:;,,,,;:ldO0kl'
            '^:ldxkkkkxdl:^'
""",
    "pop": r'''             /////////////
         /////////////////////
      ///////$2*767$1////////////////
    //////$27676767676*$1//////////////
   /////$276767$1//$27676767$1//////////////
  /////$2767676$1///$2*76767$1///////////////
 ///////$2767676$1///$276767$1.///$27676*$1///////
/////////$2767676$1//$276767$1///$2767676$1////////
//////////$276767676767$1////$276767$1/////////
///////////$276767676$1//////$27676$1//////////
////////////,$27676$1,///////$2767$1///////////
/////////////*$27676$1///////$276$1////////////
///////////////$27676$1////////////////////
 ///////////////$27676$1///$2767$1////////////
  //////////////////////$2'$1////////////
   //////$2.7676767676767676767,$1//////
    /////$2767676767676767676767$1/////
      ///////////////////////////
         /////////////////////
             /////////////
''',
    "zorin": r'''        `osssssssssssssssssssso`
       .osssssssssssssssssssssso.
      .+oooooooooooooooooooooooo+.


  `::::::::::::::::::::::.         .:`
 `+ssssssssssssssssss+:.`     `.:+ssso`
.ossssssssssssssso/.       `-+ossssssso.
ssssssssssssso/-`      `-/osssssssssssss
.ossssssso/-`      .-/ossssssssssssssso.
 `+sss+:.      `.:+ssssssssssssssssss+`
  `:.         .::::::::::::::::::::::`


      .+oooooooooooooooooooooooo+.
       -osssssssssssssssssssssso-
        `osssssssssssssssssssso`
''',
}

# Aliases — must stay OUTSIDE the literal: LOGOS is not bound mid-build,
# so LOGOS["mint"]: LOGOS["linuxmint"] inside the dict would raise NameError.
LOGOS["mint"] = LOGOS["linuxmint"]
LOGOS["opensuse-leap"] = LOGOS["opensuse"]
LOGOS["opensuse-tumbleweed"] = LOGOS["opensuse"]
