
#########################################################
#                                                       #
# Generated Automatically for the sake of a parametric  #
# response and fragility modeling study.                #
# Multi-Span Continious Concrete Girder Bridge          #
# with eastomeric bearings                              #
#                                                       #
# Number of Spans:         3                       #
# Longest Span Length:     787.402 in.                      #
# Column Height:           236.22 in.                      #
# Number of Columns:       2                          #
#                                                       #
# Units: in and kips                                    #
# Originaly created by: Bryant Nielson                  #
# Improved for parametrization and inculsion of aging   #
# by Sabarethinam Kameshwar and Navya Vishnu            #
#                                                       #
#      Simulation Number 1                           #
#########################################################
#
set begin [clock clicks -milliseconds]
#
 source modal.tcl
#
# ***MODIFICATION***
# SET THE VALUE OF PARAMETERS COMING FROM SWANAND'S MAIN FILE:
source parameterValues.tcl

puts "Delta t for the analysis: $dt"
puts "Delta t for the ground motion: $delta_t_gm"
puts "Record length: $record_length"
puts "Diameter in inches of the column in this run: $parameterFEM1"
puts "Bearing stiffness in kips in this run: $parameterFEM2"
puts "Deck area in inch^2 in this run: $parameterFEM3"

#                 number of dimensions
model BasicBuilder -ndm 3 -ndf 6
#
#
#
#==========================================================================
#                       NODE GENERATION
#==========================================================================
#
#
# NODES FOR DECK
#
#
#         ID         X         Y         Z
#       DECK NUMBER 1
node     10001     131.2       0.0    -102.2
node     10002     131.2       0.0       0.0
node     10003     131.2       0.0     102.2
node     10004     262.5       0.0    -102.2
node     10005     262.5       0.0       0.0
node     10006     262.5       0.0     102.2
node     10007     393.7       0.0    -102.2
node     10008     393.7       0.0       0.0
node     10009     393.7       0.0     102.2
node     10010     524.9       0.0    -102.2
node     10011     524.9       0.0       0.0
node     10012     524.9       0.0     102.2
node     10013     656.2       0.0    -102.2
node     10014     656.2       0.0       0.0
node     10015     656.2       0.0     102.2
#
#         ID         X         Y         Z
#       DECK NUMBER 2
node     10016     918.6       0.0    -102.2
node     10017     918.6       0.0       0.0
node     10018     918.6       0.0     102.2
node     10019    1049.9       0.0    -102.2
node     10020    1049.9       0.0       0.0
node     10021    1049.9       0.0     102.2
node     10022    1181.1       0.0    -102.2
node     10023    1181.1       0.0       0.0
node     10024    1181.1       0.0     102.2
node     10025    1312.3       0.0    -102.2
node     10026    1312.3       0.0       0.0
node     10027    1312.3       0.0     102.2
node     10028    1443.6       0.0    -102.2
node     10029    1443.6       0.0       0.0
node     10030    1443.6       0.0     102.2
#
#         ID         X         Y         Z
#       DECK NUMBER 3
node     10031    1706.0       0.0    -102.2
node     10032    1706.0       0.0       0.0
node     10033    1706.0       0.0     102.2
node     10034    1837.3       0.0    -102.2
node     10035    1837.3       0.0       0.0
node     10036    1837.3       0.0     102.2
node     10037    1968.5       0.0    -102.2
node     10038    1968.5       0.0       0.0
node     10039    1968.5       0.0     102.2
node     10040    2099.7       0.0    -102.2
node     10041    2099.7       0.0       0.0
node     10042    2099.7       0.0     102.2
node     10043    2231.0       0.0    -102.2
node     10044    2231.0       0.0       0.0
node     10045    2231.0       0.0     102.2
#======================================================================================
#              NODES RIGID LINKS AT DECKS (TRANSVERSE BEAMS)
#======================================================================================
#       DECK NUMBER 1 (Left End)
node     12001       0.0       0.0    -102.2
node     12002       0.0       0.0       0.0
node     12003       0.0       0.0     102.2
#       DECK NUMBER 1 (Right End)
node     12004     787.4       0.0    -102.2
node     12005     787.4       0.0       0.0
node     12006     787.4       0.0     102.2
#       DECK NUMBER 2 (Left End)
node     12007     787.4       0.0    -102.2
node     12008     787.4       0.0       0.0
node     12009     787.4       0.0     102.2
#       DECK NUMBER 2 (Right End)
node     12010    1574.8       0.0    -102.2
node     12011    1574.8       0.0       0.0
node     12012    1574.8       0.0     102.2
#       DECK NUMBER 3 (Left End)
node     12013    1574.8       0.0    -102.2
node     12014    1574.8       0.0       0.0
node     12015    1574.8       0.0     102.2
#       DECK NUMBER 3 (Right End)
node     12016    2362.2       0.0    -102.2
node     12017    2362.2       0.0       0.0
node     12018    2362.2       0.0     102.2
#======================================================================================
#              ABUTMENT AND BENT CAP NODES
#======================================================================================
# NODES FOR LEFT ABUTMENT
#         ID         X         Y         Z
node     501       0.0       0.0    -102.2
node     502       0.0       0.0       0.0
node     503       0.0       0.0     102.2
# NODES FOR DECK #1 LEFT BEARING
node     504       0.0       0.0    -102.2
node     505       0.0       0.0       0.0
node     506       0.0       0.0     102.2
#       BENT NUMBER 1 (Top)
node     507     787.4       0.0    -102.2
node     508     787.4       0.0       0.0
node     509     787.4       0.0     102.2
#       BENT NUMBER 1 (Bottom)
node     510     787.4     -14.9    -102.2
node     511     787.4     -14.9       0.0
node     512     787.4     -14.9     102.2
#       BENT NUMBER 2 (Top)
node     513    1574.8       0.0    -102.2
node     514    1574.8       0.0       0.0
node     515    1574.8       0.0     102.2
#       BENT NUMBER 2 (Bottom)
node     516    1574.8     -14.9    -102.2
node     517    1574.8     -14.9       0.0
node     518    1574.8     -14.9     102.2
# NODES FOR DECK #3 RIGHT BEARING
#         ID         X         Y         Z
node     519    2362.2       0.0    -102.2
node     520    2362.2       0.0       0.0
node     521    2362.2       0.0     102.2
# NODES FOR RIGHT ABUTMENT
node     522    2362.2       0.0    -102.2
node     523    2362.2       0.0       0.0
node     524    2362.2       0.0     102.2

#Additional nodes for points where the bent and the columns meet
#======================================================================================
#              FOUNDATION NODES
#======================================================================================
# NODES FOR FOUNDATION - BENT #1 
#         ID         X         Y         Z
node     8001     787.4    -299.1    -102.2
node     8002     787.4    -299.1    -102.2
node     8003     787.4    -299.1     102.2
node     8004     787.4    -299.1     102.2
# NODES FOR FOUNDATION - BENT #2 
#         ID         X         Y         Z
node     8005    1574.8    -299.1    -102.2
node     8006    1574.8    -299.1    -102.2
node     8007    1574.8    -299.1     102.2
node     8008    1574.8    -299.1     102.2
#======================================================================================
#              COLUMN NODES
#======================================================================================
#
#============BENT NUMBER 1========================
#   COLUMN NUMBER 1
#         ID         X         Y         Z
node     1050     787.4     -14.9    -102.2
node     1051     787.4     -29.8    -102.2
node     1052     787.4    -108.6    -102.2
node     1053     787.4    -187.3    -102.2
node     1054     787.4    -203.0    -102.2
node     1055     787.4    -218.8    -102.2
node     1056     787.4    -234.5    -102.2
node     1057     787.4    -250.3    -102.2
node     1058     787.4    -266.0    -102.2
#   COLUMN NUMBER 2
#         ID         X         Y         Z
node     1100     787.4     -14.9     102.2
node     1101     787.4     -29.8     102.2
node     1102     787.4    -108.6     102.2
node     1103     787.4    -187.3     102.2
node     1104     787.4    -203.0     102.2
node     1105     787.4    -218.8     102.2
node     1106     787.4    -234.5     102.2
node     1107     787.4    -250.3     102.2
node     1108     787.4    -266.0     102.2
#
#============BENT NUMBER 2========================
#   COLUMN NUMBER 1
#         ID         X         Y         Z
node     1150    1574.8     -14.9    -102.2
node     1151    1574.8     -29.8    -102.2
node     1152    1574.8    -108.6    -102.2
node     1153    1574.8    -187.3    -102.2
node     1154    1574.8    -203.0    -102.2
node     1155    1574.8    -218.8    -102.2
node     1156    1574.8    -234.5    -102.2
node     1157    1574.8    -250.3    -102.2
node     1158    1574.8    -266.0    -102.2
#   COLUMN NUMBER 2
#         ID         X         Y         Z
node     1200    1574.8     -14.9     102.2
node     1201    1574.8     -29.8     102.2
node     1202    1574.8    -108.6     102.2
node     1203    1574.8    -187.3     102.2
node     1204    1574.8    -203.0     102.2
node     1205    1574.8    -218.8     102.2
node     1206    1574.8    -234.5     102.2
node     1207    1574.8    -250.3     102.2
node     1208    1574.8    -266.0     102.2
#======================================================================================
#              NODE CONSTRAINTS
#======================================================================================
#
#    Abutments - Left
#        TAG   X   Y   Z  MX  MY  MZ
fix      501   1   1   1   1   1   1
fix      502   1   1   1   1   1   1
fix      503   1   1   1   1   1   1
#
#    Abutments - Right
#        TAG   X   Y   Z  MX  MY  MZ
fix      522   1   1   1   1   1   1
fix      523   1   1   1   1   1   1
fix      524   1   1   1   1   1   1
#
#    Left Abutment - Bearing
#        TAG   X   Y   Z  MX  MY  MZ
fix      504   0   1   0   1   1   1
fix      505   0   1   0   1   1   1
fix      506   0   1   0   1   1   1
#
#    Right Abutment - Bearing
#        TAG   X   Y   Z  MX  MY  MZ
fix      519   0   1   0   1   1   1
fix      520   0   1   0   1   1   1
fix      521   0   1   0   1   1   1
#
#    Foundation - Bent # 1
#        TAG   X   Y   Z  MX  MY  MZ
fix      8001   0   1   0   0   1   0
fix      8003   0   1   0   0   1   0
#
#    Foundation - Bent # 2
#        TAG   X   Y   Z  MX  MY  MZ
fix      8005   0   1   0   0   1   0
fix      8007   0   1   0   0   1   0
#
#    Foundation - Fixed Base - Bent # 1
#        TAG   X   Y   Z  MX  MY  MZ
fix      8002   1   1   1   1   1   1
fix      8004   1   1   1   1   1   1
#
#    Foundation - Fixed Base - Bent # 2
#        TAG   X   Y   Z  MX  MY  MZ
fix      8006   1   1   1   1   1   1
fix      8008   1   1   1   1   1   1
#======================================================================================
#              SLAVE NODES
#======================================================================================
#
#  These Constraints Create a Continuous Deck Action
#
#
#    Bent # 1
#        m-node   s-node   dof
equalDOF     12004 12007   1   2   3   4   5   6
equalDOF     12005 12008   1   2   3   4   5   6
equalDOF     12006 12009   1   2   3   4   5   6
#
#    Bent # 2
#        m-node   s-node   dof
equalDOF     12010 12013   1   2   3   4   5   6
equalDOF     12011 12014   1   2   3   4   5   6
equalDOF     12012 12015   1   2   3   4   5   6
#
#
#====================================================================
#                       COLUMN & BENT CAP MATERIAL
#==========================================================================
set cover 1.5
# ***MODIFICATION***
# Diameter of column bents is set as a parameter for the parametric study.
# puts "NOW PUTTING... diameter of the column in this run: $parameterFEM inches"
set D $parameterFEM1
set d 0.67*$D
set hoop_dia 0.69*$D
set Ast 0.31
set rho_t 0.0071
set fyst     41.7598; # Reinforcing steel yield strength
set fc     -7.1115; # Unconfined concrete strength
set fcon -7.114984785374884
set Ec 5148.221023783082
set fc     -7.1115; # Unconfined concrete strength
set fys     41.7598; # Reinforcing steel yield strength
set Es   29000.0; # Reinforcing steel Modulus of Elasticity
# Estimate yield curvature
# (Assuming no axial load and only top and bottom steel)
set epsy [expr $fys/$Es]	;# steel yield strain
set Ky [expr $epsy/(0.7*$d)]; # Yield Curvature
#
# Print estimate to standard output
puts "Estimated yield curvature: $Ky"
set name MSC-Concrete_1

set file_curve [open [concat $name/$name.crv] w]
puts $file_curve $Ky
close $file_curve
set ec [expr 0.002]
set ecu 0.012
set Econ  [expr 57.0*pow(-$fcon*1000,0.5)]
#
#
#  CONCRETE                 tag  f'c              ec0           f'cu     ecu
#  Core concrete (confined)
uniaxialMaterial Concrete04 1   $fcon   [expr -1.0*$ec]  [expr -1.0*$ecu]    $Econ
#
#  Cover concrete (un-confined)
uniaxialMaterial Concrete04 2     $fc       [expr -1.0*0.002]  [expr -1.0*0.004]    $Ec
#
#  REINFORCING STEEL        tag  
uniaxialMaterial Steel02   3  $fys $Es 0.025 18.0 0.925 0.15
#
# Torsion Material
uniaxialMaterial Elastic    4    1.0e10
#
#==========================================================================
#                       COLUMN SECTION GENERATION
#==========================================================================
# ***MODIFICATION*** The diameter affects patch generation as well, hence making changes here.
set d_b  1.128
set covCol 0.936
set coreDia [expr 0.5*$d-$covCol]
set outerDia [expr 0.5*$d]
set file_rho_tl [open [concat $name/$name.rho_tl] w]
puts $file_rho_tl 0.026951866689950605
puts $file_rho_tl 2.4347842559999952e-5
close $file_rho_tl
# ***MODIFICATION*** Substituting int-rad and out-rad using parameterFEM, also changing syntax with
section Fiber 1 -torsion 4 [subst {                                                                                        #                    angle
# Core concrete       tag      div     raddiv       Y-cen    Z-cen     int-rad                    out-rad                     start  end
patch circ             1 10 8 0.0 0.0 0.0 $coreDia 0.0 360.0
# Cover concrete 
patch circ             2 10 2 0.0 0.0 $coreDia $outerDia 0.0 360.0
# Reinforcing Steel
layer circ             3 10 0.17076023359999998 0.0 0.0 $coreDia 0.0 324.0
}]
#                   TAG  Mat  Dir    section
section Aggregator   2    4    T   -section 1
#
#==========================================================================
#                       COLUMN ELEMENTS
#==========================================================================
#
geomTransf	PDelta	3    1   0   0
#
#
set int  6	;# integration point
#
#  Bent No. 1 - Column No. 1
#                        TAG    In    Jn  int-pts   Sect   Transf
element dispBeamColumn  1051  1051  1052   $int     2     3 
element dispBeamColumn  1052  1052  1053   $int     2     3 
element dispBeamColumn  1053  1053  1054   $int     2     3 
element dispBeamColumn  1054  1054  1055   $int     2     3 
element dispBeamColumn  1055  1055  1056   $int     2     3 
element dispBeamColumn  1056  1056  1057   $int     2     3 
element dispBeamColumn  1057  1057  1058   $int     2     3 
#
#  Bent No. 1 - Column No. 2
#                        TAG    In    Jn  int-pts   Sect   Transf
element dispBeamColumn  1101  1101  1102   $int     2     3 
element dispBeamColumn  1102  1102  1103   $int     2     3 
element dispBeamColumn  1103  1103  1104   $int     2     3 
element dispBeamColumn  1104  1104  1105   $int     2     3 
element dispBeamColumn  1105  1105  1106   $int     2     3 
element dispBeamColumn  1106  1106  1107   $int     2     3 
element dispBeamColumn  1107  1107  1108   $int     2     3 
#
#  Bent No. 2 - Column No. 1
#                        TAG    In    Jn  int-pts   Sect   Transf
element dispBeamColumn  1151  1151  1152   $int     2     3 
element dispBeamColumn  1152  1152  1153   $int     2     3 
element dispBeamColumn  1153  1153  1154   $int     2     3 
element dispBeamColumn  1154  1154  1155   $int     2     3 
element dispBeamColumn  1155  1155  1156   $int     2     3 
element dispBeamColumn  1156  1156  1157   $int     2     3 
element dispBeamColumn  1157  1157  1158   $int     2     3 
#
#  Bent No. 2 - Column No. 2
#                        TAG    In    Jn  int-pts   Sect   Transf
element dispBeamColumn  1201  1201  1202   $int     2     3 
element dispBeamColumn  1202  1202  1203   $int     2     3 
element dispBeamColumn  1203  1203  1204   $int     2     3 
element dispBeamColumn  1204  1204  1205   $int     2     3 
element dispBeamColumn  1205  1205  1206   $int     2     3 
element dispBeamColumn  1206  1206  1207   $int     2     3 
element dispBeamColumn  1207  1207  1208   $int     2     3 
#
#==========================================================================
#                       BENT CAP SECTION GENERATION
#==========================================================================
#
set bWidth [expr 23.8196+2*1.5]
set bDepth [expr $bWidth+2*1.5]
#
set A_steel [expr 1.0767*($bWidth-2*$cover)*($bDepth-2*$cover)/100]
set factor [expr $A_steel/(15*1+4*0.32)]
set As1    [expr $factor*1.00];      
set As2    [expr $factor*0.32];     
set As1 [expr $As1*0.17096172224737186]
set As2 [expr $As2*0.0034292735999999937]
# some variables derived from the parameters
set y1 [expr $bDepth/2.0]
set z1 [expr $bWidth/2.0]
#
#
section Fiber 3 -torsion 4 {
#
    # Create the concrete core fibers
    patch quad 1 10 10 [expr $cover-$y1] [expr $cover-$z1] [expr $y1-$cover] [expr $cover-$z1] [expr $y1-$cover] [expr $z1-$cover] [expr $cover-$y1] [expr $z1-$cover]
#
    # Create the concrete cover fibers (top, bottom, left, right)
    patch quad 2 10 2  [expr -$y1] [expr $z1-$cover] $y1 [expr $z1-$cover] $y1 $z1 [expr -$y1] $z1
    patch quad 2 10 2  [expr -$y1] [expr -$z1] $y1 [expr -$z1] $y1 [expr $cover-$z1] [expr -$y1] [expr $cover-$z1]
    patch quad 2  2 10  [expr -$y1] [expr $cover-$z1] [expr $cover-$y1] [expr $cover-$z1] [expr $cover-$y1] [expr $z1-$cover] [expr -$y1] [expr $z1-$cover]
    patch quad 2  2 10  [expr $y1-$cover] [expr $cover-$z1] $y1 [expr $cover-$z1] $y1 [expr $z1-$cover] [expr $y1-$cover] [expr $z1-$cover]
#
    # Create the reinforcing fibers (right, middle, left)
    layer straight 3 9 $As1 [expr $y1-$cover] [expr $z1-$cover] [expr $y1-$cover] [expr $cover-$z1]
    layer straight 3 2 $As2 -7.0 [expr $z1-$cover] -7.0 [expr $cover-$z1]
    layer straight 3 2 $As2 7.0 [expr $z1-$cover] 7.0 [expr $cover-$z1]
    layer straight 3 6 $As1 [expr $cover-$y1] [expr $z1-$cover] [expr $cover-$y1] [expr $cover-$z1]
}
#
section Aggregator 4  4   T   -section 3
#
#==========================================================================
#                       BENT CAP ELEMENTS
#==========================================================================
#
geomTransf	PDelta	4  -1  0  0
#
#
set int3  4	;# integration point
#
element dispBeamColumn  5001    510  511   $int3     4      4
element dispBeamColumn  5002    511  512   $int3     4      4
element dispBeamColumn  5003    516  517   $int3     4      4
element dispBeamColumn  5004    517  518   $int3     4      4
equalDOF 1050 510  1 2 3 4 5 6
equalDOF 1100 512  1 2 3 4 5 6
equalDOF 1150 516  1 2 3 4 5 6
equalDOF 1200 518  1 2 3 4 5 6
#======================================================================================
#              NODAL MASSES
#======================================================================================
#======================================================================================
#              DECK MASSES
#======================================================================================
set dms 0.06306533703369566; # Type 1 Girder
set dms2 [expr $dms/2.]
set dml 0.06306533703369566; # Type 1 Girder
set dml2 [expr $dml/2.]
#
#          Deck No. 1
#       node X-mass   Y-mass   Z-mass   MX-mass  MY-mass  MZ-mass
#      Left End
mass     12001 $dms2    $dms2    $dms2    $dms2    $dms2    $dms2   
mass     12002 $dms2    $dms2    $dms2    $dms2    $dms2    $dms2   
mass     12003 $dms2    $dms2    $dms2    $dms2    $dms2    $dms2   
mass     10001 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10002 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10003 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10004 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10005 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10006 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10007 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10008 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10009 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10010 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10011 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10012 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10013 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10014 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10015 $dms     $dms     $dms     $dms     $dms     $dms    
#      Right End
mass     12004 $dms2    $dms2    $dms2    $dms2    $dms2    $dms2   
mass     12005 $dms2    $dms2    $dms2    $dms2    $dms2    $dms2   
mass     12006 $dms2    $dms2    $dms2    $dms2    $dms2    $dms2   
#
#          Deck No. 2
#       node X-mass   Y-mass   Z-mass   MX-mass  MY-mass  MZ-mass
#      Left End
mass     12007 $dml2    $dml2    $dml2    $dml2    $dml2    $dml2   
mass     12008 $dml2    $dml2    $dml2    $dml2    $dml2    $dml2   
mass     12009 $dml2    $dml2    $dml2    $dml2    $dml2    $dml2   
mass     10016 $dml     $dml     $dml     $dml     $dml     $dml    
mass     10017 $dml     $dml     $dml     $dml     $dml     $dml    
mass     10018 $dml     $dml     $dml     $dml     $dml     $dml    
mass     10019 $dml     $dml     $dml     $dml     $dml     $dml    
mass     10020 $dml     $dml     $dml     $dml     $dml     $dml    
mass     10021 $dml     $dml     $dml     $dml     $dml     $dml    
mass     10022 $dml     $dml     $dml     $dml     $dml     $dml    
mass     10023 $dml     $dml     $dml     $dml     $dml     $dml    
mass     10024 $dml     $dml     $dml     $dml     $dml     $dml    
mass     10025 $dml     $dml     $dml     $dml     $dml     $dml    
mass     10026 $dml     $dml     $dml     $dml     $dml     $dml    
mass     10027 $dml     $dml     $dml     $dml     $dml     $dml    
mass     10028 $dml     $dml     $dml     $dml     $dml     $dml    
mass     10029 $dml     $dml     $dml     $dml     $dml     $dml    
mass     10030 $dml     $dml     $dml     $dml     $dml     $dml    
#      Right End
mass     12010 $dml2    $dml2    $dml2    $dml2    $dml2    $dml2   
mass     12011 $dml2    $dml2    $dml2    $dml2    $dml2    $dml2   
mass     12012 $dml2    $dml2    $dml2    $dml2    $dml2    $dml2   
#
#          Deck No. 3
#       node X-mass   Y-mass   Z-mass   MX-mass  MY-mass  MZ-mass
#      Left End
mass     12013 $dms2    $dms2    $dms2    $dms2    $dms2    $dms2   
mass     12014 $dms2    $dms2    $dms2    $dms2    $dms2    $dms2   
mass     12015 $dms2    $dms2    $dms2    $dms2    $dms2    $dms2   
mass     10031 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10032 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10033 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10034 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10035 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10036 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10037 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10038 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10039 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10040 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10041 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10042 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10043 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10044 $dms     $dms     $dms     $dms     $dms     $dms    
mass     10045 $dms     $dms     $dms     $dms     $dms     $dms    
#      Right End
mass     12016 $dms2    $dms2    $dms2    $dms2    $dms2    $dms2   
mass     12017 $dms2    $dms2    $dms2    $dms2    $dms2    $dms2   
mass     12018 $dms2    $dms2    $dms2    $dms2    $dms2    $dms2   
#======================================================================================
#              BENT CAP MASSES
#======================================================================================
set gd_spc 102.2066
set  bcm   [expr (102.2066/75.)*($bWidth*$bDepth)*0.03397/(3.5*4.0*144)]  ; # bent cap mass for 75 inch section (k-s^2/in)
set  bcm2   [expr $bcm/2.]
set bmiz [expr $bcm*($bDepth*$bDepth+$bWidth*$bWidth)/12]
set bmix [expr $bcm*($bDepth*$bDepth+$gd_spc*$gd_spc)/12]
set bmiy [expr $bcm*($bWidth*$bWidth+$gd_spc*$gd_spc)/12]
set bmiz2 [expr $bcm2*($bDepth*$bDepth+$bWidth*$bWidth)/12]
set bmix2 [expr $bcm2*($bDepth*$bDepth+$gd_spc*$gd_spc/4.)/12+$bcm2*$gd_spc*$gd_spc/16.]
set bmiy2 [expr $bcm2*($bWidth*$bWidth+$gd_spc*$gd_spc/4.)/12+$bcm2*$gd_spc*$gd_spc/16.]
#
#          Bent No. 2
#       node X-mass   Y-mass   Z-mass   MX-mass  MY-mass  MZ-mass
mass     510 $bcm2    $bcm2    $bcm2    $bmix2   $bmiy2   $bmiz2  
mass     511 $bcm     $bcm     $bcm     $bmix    $bmiy    $bmiz   
mass     512 $bcm2    $bcm2    $bcm2    $bmix2   $bmiy2   $bmiz2  
#
#          Bent No. 3
#       node X-mass   Y-mass   Z-mass   MX-mass  MY-mass  MZ-mass
mass     516 $bcm2    $bcm2    $bcm2    $bmix2   $bmiy2   $bmiz2  
mass     517 $bcm     $bcm     $bcm     $bmix    $bmiy    $bmiz   
mass     518 $bcm2    $bcm2    $bcm2    $bmix2   $bmiy2   $bmiz2  
#======================================================================================
#              COLUMN MASSES
#======================================================================================
set  colm   0.00789395814836981  ; # column mass for 78.74 inch section (k-s^2/in)
set  colm2   [expr $colm/2.]
set ch 236.22
set cmix [expr $colm*(3*$D*$D+$ch*$ch/9)/12]
set cmix2 [expr $colm2*(3*$D*$D+$ch*$ch/36)/12+ $colm2*$ch*$ch/144]
set cmiz [expr $colm*(3*$D*$D+$ch*$ch/9)/12]
set cmiz2 [expr $colm2*(3*$D*$D+$ch*$ch/36)/12+ $colm2*$ch*$ch/144]
set cmiy [expr $colm*($D*$D)/2]
set cmiy2 [expr $colm2*($D*$D)/2]
#
#    Bent No. 1, Column No. 1
#       node X-mass   Y-mass   Z-mass   MX-mass  MY-mass  MZ-mass
mass     1051 $colm2   $colm2   $colm2   $cmix2   $cmiy2   $cmiz2  
mass     1052 $colm    $colm    $colm    $cmix    $cmiy    $cmiz   
mass     1053 $colm    $colm    $colm    $cmix    $cmiy    $cmiz   
mass     1058 $colm2   $colm2   $colm2   $cmix2   $cmiy2   $cmiz2  
#===================================================================
#
#    Bent No. 1, Column No. 2
#       node X-mass   Y-mass   Z-mass   MX-mass  MY-mass  MZ-mass
mass     1101 $colm2   $colm2   $colm2   $cmix2   $cmiy2   $cmiz2  
mass     1102 $colm    $colm    $colm    $cmix    $cmiy    $cmiz   
mass     1103 $colm    $colm    $colm    $cmix    $cmiy    $cmiz   
mass     1108 $colm2   $colm2   $colm2   $cmix2   $cmiy2   $cmiz2  
#===================================================================
#
#    Bent No. 2, Column No. 1
#       node X-mass   Y-mass   Z-mass   MX-mass  MY-mass  MZ-mass
mass     1151 $colm2   $colm2   $colm2   $cmix2   $cmiy2   $cmiz2  
mass     1152 $colm    $colm    $colm    $cmix    $cmiy    $cmiz   
mass     1153 $colm    $colm    $colm    $cmix    $cmiy    $cmiz   
mass     1158 $colm2   $colm2   $colm2   $cmix2   $cmiy2   $cmiz2  
#===================================================================
#
#    Bent No. 2, Column No. 2
#       node X-mass   Y-mass   Z-mass   MX-mass  MY-mass  MZ-mass
mass     1201 $colm2   $colm2   $colm2   $cmix2   $cmiy2   $cmiz2  
mass     1202 $colm    $colm    $colm    $cmix    $cmiy    $cmiz   
mass     1203 $colm    $colm    $colm    $cmix    $cmiy    $cmiz   
mass     1208 $colm2   $colm2   $colm2   $cmix2   $cmiy2   $cmiz2  
#===================================================================
#======================================================================================
#              FOUNDATION MASSES
#======================================================================================
set  fndm   0.02317  ; # (k-s^2/in)
set fmiz [expr $fndm*((96*96)+43*43)/12]
set fmix [expr $fndm*(96*96+43*43)/12]
set fmiy [expr $fndm*(96*96+96*96)/12]
#
#    Bent No. 1
#       node X-mass   Y-mass   Z-mass   MX-mass  MY-mass  MZ-mass
mass     8001 $fndm    $fndm    $fndm    $fmix    $fmiy    $fmiz   
mass     8002 $fndm    $fndm    $fndm    $fmix    $fmiy    $fmiz   
#===================================================================
#
#    Bent No. 2
#       node X-mass   Y-mass   Z-mass   MX-mass  MY-mass  MZ-mass
mass     8003 $fndm    $fndm    $fndm    $fmix    $fmiy    $fmiz   
mass     8004 $fndm    $fndm    $fndm    $fmix    $fmiy    $fmiz   
#===================================================================
#======================================================================================
#              GIRDER PROPERTIES
#======================================================================================
# ***MODIFICATION***
# set Ag       1553.314   ; # Cross-sectional Area in^2
set Ag       $parameterFEM3   ; # Cross-sectional Area in^2
set Izg      455764.4607   ; # Moment of Inertia in^4
set Iyg      813337.7107   ; # Moment of Inertia in^4
set Eg     5719.3827418084375         ; # Elastic Modulus  ksi
set Gg 2486.6881486123643
set Jg    [expr $Iyg+$Izg]
#======================================================================================
#              LONGITUDINAL DECK ELEMENTS
#======================================================================================
#                  TAG   Xv  Yv  Zv
geomTransf Corotational     1    0   1   0

#
#       DECK NUMBER 1
#                          Tag     iN    jN     A      E      G     J      Iz     Iy    Transf
element elasticBeamColumn 100001 12001 10001 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100002 10001 10004 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100003 10004 10007 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100004 10007 10010 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100005 10010 10013 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100006 10013 12004 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100007 12002 10002 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100008 10002 10005 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100009 10005 10008 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100010 10008 10011 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100011 10011 10014 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100012 10014 12005 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100013 12003 10003 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100014 10003 10006 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100015 10006 10009 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100016 10009 10012 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100017 10012 10015 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100018 10015 12006 $Ag $Eg $Gg $Jg $Izg $Iyg 1
#
#       DECK NUMBER 2
#                          Tag     iN    jN     A      E      G     J      Iz     Iy    Transf
element elasticBeamColumn 100019 12007 10016 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100020 10016 10019 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100021 10019 10022 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100022 10022 10025 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100023 10025 10028 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100024 10028 12010 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100025 12008 10017 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100026 10017 10020 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100027 10020 10023 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100028 10023 10026 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100029 10026 10029 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100030 10029 12011 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100031 12009 10018 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100032 10018 10021 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100033 10021 10024 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100034 10024 10027 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100035 10027 10030 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100036 10030 12012 $Ag $Eg $Gg $Jg $Izg $Iyg 1
#
#       DECK NUMBER 3
#                          Tag     iN    jN     A      E      G     J      Iz     Iy    Transf
element elasticBeamColumn 100037 12013 10031 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100038 10031 10034 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100039 10034 10037 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100040 10037 10040 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100041 10040 10043 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100042 10043 12016 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100043 12014 10032 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100044 10032 10035 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100045 10035 10038 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100046 10038 10041 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100047 10041 10044 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100048 10044 12017 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100049 12015 10033 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100050 10033 10036 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100051 10036 10039 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100052 10039 10042 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100053 10042 10045 $Ag $Eg $Gg $Jg $Izg $Iyg 1
element elasticBeamColumn 100054 10045 12018 $Ag $Eg $Gg $Jg $Izg $Iyg 1
#======================================================================================
#              TRANSVERSE DECK ELEMENTS
#======================================================================================
#                  TAG   Xv  Yv  Zv
geomTransf Corotational    2    0   1   0
#
set Atd     1e8        ; # Cross-sectional Area in^2
set Itd     1e9         ; # Moment of Inertia in^4
set Etd     1e8         ; # Elastic Modulus  ksi
set Gtd     1e8         ; # Modulus of Rigidity ksi
set Jtd     1e9         ; # Polar MOI  in^4 
#
uniaxialMaterial Elastic 1000 9e9
set E_t 5148.221023783082
set A_t     1481.8727        ; # Cross-sectional Area in^2
set Iz_t    15069.6304        ; # Moment of Inertia in^4
set Iy_t    2251535.2741         ; # Moment of Inertia in^4
set J_t    [expr $Iy_t+$Iz_t]
set G_t [expr $E_t/(2*(1+0.15))]
#
#       DECK NUMBER 1
#                          Tag     iN    jN     A      E      G     J      Iz     Iy    Transf
#      Left End
element elasticBeamColumn 12001 12001 12002 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 12002 12002 12003 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
#      Grillage members
element elasticBeamColumn 120001 10001 10002 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120002 10002 10003 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120003 10004 10005 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120004 10005 10006 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120005 10007 10008 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120006 10008 10009 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120007 10010 10011 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120008 10011 10012 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120009 10013 10014 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120010 10014 10015 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
#      Right End
element elasticBeamColumn 12003 12004 12005 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 12004 12005 12006 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
#
#       DECK NUMBER 2
#                          Tag     iN    jN     A      E      G     J      Iz     Iy    Transf
#      Left End
element elasticBeamColumn 12005 12007 12008 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 12006 12008 12009 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
#      Grillage members
element elasticBeamColumn 120011 10016 10017 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120012 10017 10018 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120013 10019 10020 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120014 10020 10021 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120015 10022 10023 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120016 10023 10024 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120017 10025 10026 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120018 10026 10027 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120019 10028 10029 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120020 10029 10030 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
#      Right End
element elasticBeamColumn 12007 12010 12011 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 12008 12011 12012 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
#
#       DECK NUMBER 3
#                          Tag     iN    jN     A      E      G     J      Iz     Iy    Transf
#      Left End
element elasticBeamColumn 12009 12013 12014 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 12010 12014 12015 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
#      Grillage members
element elasticBeamColumn 120021 10031 10032 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120022 10032 10033 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120023 10034 10035 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120024 10035 10036 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120025 10037 10038 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120026 10038 10039 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120027 10040 10041 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120028 10041 10042 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120029 10043 10044 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 120030 10044 10045 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
#      Right End
element elasticBeamColumn 12011 12016 12017 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
element elasticBeamColumn 12012 12017 12018 $A_t $E_t $G_t $J_t $Iz_t $Iy_t 2
#
#==========================================================================
#                       RIGID LINKS
#==========================================================================
#
#                  TAG   Xv  Yv  Zv
geomTransf Linear   6    1   0   0
#
# Links at the bent caps.
#    Bent No. 1
#                          Tag     iN    jN     A      E      G     J      Iz     Iy    Transf
element elasticBeamColumn  9001   507   510   $Atd   $Etd   $Gtd   $Jtd   $Itd   $Itd     6
element elasticBeamColumn  9002   508   511   $Atd   $Etd   $Gtd   $Jtd   $Itd   $Itd     6
element elasticBeamColumn  9003   509   512   $Atd   $Etd   $Gtd   $Jtd   $Itd   $Itd     6
#    Bent No. 2
#                          Tag     iN    jN     A      E      G     J      Iz     Iy    Transf
element elasticBeamColumn  9004   513   516   $Atd   $Etd   $Gtd   $Jtd   $Itd   $Itd     6
element elasticBeamColumn  9005   514   517   $Atd   $Etd   $Gtd   $Jtd   $Itd   $Itd     6
element elasticBeamColumn  9006   515   518   $Atd   $Etd   $Gtd   $Jtd   $Itd   $Itd     6
#
# Links at the column tops.
#    Bent No. 1
element elasticBeamColumn  9007  1050  1051   $Atd   $Etd   $Gtd   $Jtd   $Itd   $Itd     6
element elasticBeamColumn  9008  1100  1101   $Atd   $Etd   $Gtd   $Jtd   $Itd   $Itd     6
#    Bent No. 2
element elasticBeamColumn  9009  1150  1151   $Atd   $Etd   $Gtd   $Jtd   $Itd   $Itd     6
element elasticBeamColumn  9010  1200  1201   $Atd   $Etd   $Gtd   $Jtd   $Itd   $Itd     6
#
# Links at the column bases.
#    Bent No. 1
puts "*************************** ok till here ****************************"
element elasticBeamColumn  9011  8001  1058   $Atd   $Etd   $Gtd   $Jtd   $Itd   $Itd     6
puts "*************************** ok till here ****************************"
element elasticBeamColumn  9012  8003  1108   $Atd   $Etd   $Gtd   $Jtd   $Itd   $Itd     6
#    Bent No. 2
puts "*************************** ok till here ****************************"
element elasticBeamColumn  9013  8005  1158   $Atd   $Etd   $Gtd   $Jtd   $Itd   $Itd     6
puts "*************************** ok till here ****************************"
element elasticBeamColumn  9014  8007  1208   $Atd   $Etd   $Gtd   $Jtd   $Itd   $Itd     6
#
#==========================================================================
#        GENERATE MATERIAL AND ELEMENTS FOR FIXED ELASTOMERIC BEARINGS
#==========================================================================
#
uniaxialMaterial Elastic 8378 2900.0
# Define uniaxialMaterial
#  These materials define the response of the elastomeric pads
#                          Tag     Fy    Eo   b
uniaxialMaterial Steel01   203    27.337161383963316  $parameterFEM2    0.0;# End spans
uniaxialMaterial Steel01   204    27.337161383963316  $parameterFEM2    0.0;# Middle spans
#
# Define uniaxialMaterial
uniaxialMaterial ElasticPPGap 200  9e5   9e10   0.125
uniaxialMaterial ElasticPPGap 202  9e5  -9e10  -0.125
#
#  This material quantifies the response of the 2 - 1 in diameter dowels
#
uniaxialMaterial Hysteretic 201  18.786736812649767   .048     19.468121049378     0.21       0    0.2101  -18.786736812649767   -.048    -19.468121049378  -0.21     -0   -.2101    1.0   0.0    0.0   0.0    0.0  
# Combine them
uniaxialMaterial Parallel  5   200     202
uniaxialMaterial Series    6   201       5
#
# Combine them
uniaxialMaterial Parallel  7   6   203; # For end spans
uniaxialMaterial Parallel  8   6   204; # For middle spans
#
#================Generate elements===========================================
#
#
#      Fixed Bearing - Span No. 1
#                     tag  i-node j-node   material             X    Z 
element zeroLength 501 504 12001 -mat 7 8378 7 -dir 1 2 3
element zeroLength 502 505 12002 -mat 7 8378 7 -dir 1 2 3
element zeroLength 503 506 12003 -mat 7 8378 7 -dir 1 2 3
#
#      Fixed Bearing - Span No. 2
#                     tag  i-node j-node   material             X    Z 
element zeroLength 504 507 12007 -mat 8 8378 8 -dir 1 2 3
element zeroLength 505 508 12008 -mat 8 8378 8 -dir 1 2 3
element zeroLength 506 509 12009 -mat 8 8378 8 -dir 1 2 3
#
#      Fixed Bearing - Span No. 3
#                     tag  i-node j-node   material             X    Z 
element zeroLength 507 513 12013 -mat 7 8378 7 -dir 1 2 3
element zeroLength 508 514 12014 -mat 7 8378 7 -dir 1 2 3
element zeroLength 509 515 12015 -mat 7 8378 7 -dir 1 2 3
#
#==========================================================================
#        GENERATE MATERIAL AND ELEMENTS FOR EXPANSION ELASTOMERIC BEARINGS
#==========================================================================
# Use same pad materials 203 and 204 for end spans and middle spans respectively.
#
# Define uniaxialMaterial
uniaxialMaterial ElasticPPGap 300  9e5   9e10   1.2033
uniaxialMaterial ElasticPPGap 302  9e5  -9e10  -0.7967
#
#  Use same dowel material 201 as before
#
# Combine them
uniaxialMaterial Parallel  35   300     302
uniaxialMaterial Series    36   201      35
#
# Combine them
uniaxialMaterial Parallel  37   36   203; # For end spans
uniaxialMaterial Parallel  38   36   204; # For middle spans
#
#      Expansion Bearing - Span No. 1
#                     tag  i-node j-node   material             X    Z 
element zeroLength 701 507 12004 -mat 37 8378 7 -dir 1 2 3
element zeroLength 702 508 12005 -mat 37 8378 7 -dir 1 2 3
element zeroLength 703 509 12006 -mat 37 8378 7 -dir 1 2 3
#
#      Expansion Bearing - Span No. 2
#                     tag  i-node j-node   material             X    Z 
element zeroLength 704 513 12010 -mat 38 8378 8 -dir 1 2 3
element zeroLength 705 514 12011 -mat 38 8378 8 -dir 1 2 3
element zeroLength 706 515 12012 -mat 38 8378 8 -dir 1 2 3
#
#      Expansion Bearing - Span No. 3
#                     tag  i-node j-node   material             X    Z 
element zeroLength 707 519 12016 -mat 37 8378 7 -dir 1 2 3
element zeroLength 708 520 12017 -mat 37 8378 7 -dir 1 2 3
element zeroLength 709 521 12018 -mat 37 8378 7 -dir 1 2 3
#
#==========================================================================
#        GENERATE MATERIAL AND ELEMENTS FOR IMPACT OF DECKS
#==========================================================================
#
set gap1 -1.5783
set gap2 -1.5471
#
#     				tag       K         Fy      gap
uniaxialMaterial ElasticPPGap 402      6368    -637     [expr $gap1]
uniaxialMaterial ElasticPPGap 403      2190    -9e9     [expr $gap1-0.1418]
uniaxialMaterial ElasticPPGap 404      6368    -637     [expr $gap2]
uniaxialMaterial ElasticPPGap 405      2190    -9e9     [expr $gap2-0.1418]
#
# Combine them
uniaxialMaterial Parallel  131   402   403; # Left Abutment gap
uniaxialMaterial Parallel  132   404   405; # Right Abutment gap
#
#      Abutment No. 1 - Impact
#                      tag  i-node j-node material               X
element  zeroLength  14001   504 12001    -mat    131   -dir     1
element  zeroLength  14002   505 12002    -mat    131   -dir     1
element  zeroLength  14003   506 12003    -mat    131   -dir     1
#
#      Abutment No. 2 - Impact
#                      tag  i-node j-node material               X
element  zeroLength  14004 12016   519    -mat    132   -dir     1
element  zeroLength  14005 12017   520    -mat    132   -dir     1
element  zeroLength  14006 12018   521    -mat    132   -dir     1
#
#==========================================================================
#        GENERATE MATERIAL AND ELEMENTS FOR ABUTMENTS
#==========================================================================
#
#
#     Passive Soil Contribution per 75 in width (1 - girder) of deck
set   s1   182.98713047020706
set   e1   0.70827008
set   s2   370.9075093782599
set   e2   2.4789452799999996
set   s3   370.9075093782599
set   e3   7.0827008
#
#                             tag   s1p   e1p   s2p   e2p   s3p   e3p   s1n   e1n   s2n   e2n   s3n   e3n     px    py    d1    d2  beta
uniaxialMaterial Hysteretic    500  $s1   $e1   $s2   $e2   $s3   $e3  -$s1  -$e1  -$s2  -$e2  -$s3  -$e3    1.0   0.0   0.0   0.0  0.0
uniaxialMaterial ElasticPPGap  501  33.39730718116127   -153.75303728840674   -2.4789452799999996
uniaxialMaterial Parallel      502  500 501
uniaxialMaterial ENT           503  1e8
uniaxialMaterial Series        504  502 503
#
#   Pile Portion (for longitudinal and transverse) for 75 in. width
#
set   s1   47.851328340289925
set   e1   0.3
set   s2   68.3609963957275
set   e2   1
set   s3   68.3609963957275
set   e3   2 
#                           tag   s1p   e1p   s2p   e2p   s3p   e3p   s1n   e1n   s2n   e2n   s3n   e3n     px    py    d1    d2  beta
uniaxialMaterial Hysteretic  10   $s1   $e1   $s2   $e2   $s3   $e3  -$s1  -$e1  -$s2  -$e2  -$s3  -$e3   0.75   0.5   0.0   0.0   0.1
#
#  Combine them in parallel
#
uniaxialMaterial Parallel  9   504 10; #  Abutment Longitudinal  
#
#      Abutment No. 1 - Soil_Pile Springs
#                      tag  i-node j-node material               X
element zeroLength 7001 501 504  -mat 9 10 -dir 1 3
element zeroLength 7002 502 505  -mat 9 10 -dir 1 3
element zeroLength 7003 503 506  -mat 9 10 -dir 1 3
#
#      Abutment No. 2 - Soil_Pile Springs
#                      tag  i-node j-node material               X
element zeroLength 7004 519 522  -mat 9 10 -dir 1 3
element zeroLength 7005 520 523  -mat 9 10 -dir 1 3
element zeroLength 7006 521 524  -mat 9 10 -dir 1 3
#
#==========================================================================
#        GENERATE MATERIAL AND ELEMENTS FOR FOUNDATIONS
#==========================================================================
#
#
#   Foundation Springs - Translational and Rotationaln#
#				          tag       K       Fy       gap
# uniaxialMaterial  ElasticPPGap    701    474.8   -142.5    0.000
# uniaxialMaterial  ElasticPPGap    702     87.2    -61.1   -0.300
# uniaxialMaterial  ElasticPPGap    703    474.8    142.5    0.000
# uniaxialMaterial  ElasticPPGap    704     87.2     61.1    0.300

#   ***MODIFICATION*** Foundation Springs - Translational and Rotational HIGHLY STIFF#
#				          tag       K       Fy       gap
uniaxialMaterial  ElasticPPGap    701    474.8   -142.5    0.000
uniaxialMaterial  ElasticPPGap    702     87.2    -61.1   -0.300
uniaxialMaterial  ElasticPPGap    703    474.8    142.5    0.000
uniaxialMaterial  ElasticPPGap    704     87.2     61.1    0.300

#
#  Combine them in parallel
#
uniaxialMaterial Parallel 15   701 702 703 704; #  Foundation - Translational spring (k/in)
# Rotational stiffness
# uniaxialMaterial Elastic  16    6973275.42     ; # kip-in/rad
# ***MODIFICATION*** Rotational stiffness STIFF
uniaxialMaterial Elastic  16    6973275.42     ; # kip-in/rad
#
#      Bent No. 1 - Foundation Springs
#                      tag  i-node j-node material                       X   Z  Mx  Mz
element  zeroLength   8001  8001  8002    -mat   15  15  16  16   -dir   1   3   4   6
element  zeroLength   8002  8003  8004    -mat   15  15  16  16   -dir   1   3   4   6
#
#      Bent No. 2 - Foundation Springs
#                      tag  i-node j-node material                       X   Z  Mx  Mz
element  zeroLength   8003  8005  8006    -mat   15  15  16  16   -dir   1   3   4   6
element  zeroLength   8004  8007  8008    -mat   15  15  16  16   -dir   1   3   4   6
#
#
#==========================================================================
#                       END OF MODEL GENERATION
#==========================================================================
#
logFile MSC-Concrete_1/MSC-Concrete_1.log
#
#==========================================================================
#             DEFINE RECORDERS
#==========================================================================
#
	recorder EnvelopeElement -file MSC-Concrete_1/col_base.frc -ele 1057 1107 1157 1207 section $int force
	recorder EnvelopeElement -file MSC-Concrete_1/col_base.def -ele 1057 1107 1157 1207 section $int deformation
#
#
	recorder EnvelopeElement -file MSC-Concrete_1/col_top.frc  -ele 1051 1101 1151 1201 section 1 force
	recorder EnvelopeElement -file MSC-Concrete_1/col_top.def  -ele 1051 1101 1151 1201 section 1 deformation
#
#
	recorder EnvelopeElement -file    MSC-Concrete_1/abut.frc -eleRange 7001 7006  force
	recorder EnvelopeElement -file    MSC-Concrete_1/abut.def -eleRange 7001 7006  deformation
	recorder EnvelopeElement -file  MSC-Concrete_1/fxdbrg.frc -eleRange  501 509  force
	recorder EnvelopeElement -file  MSC-Concrete_1/fxdbrg.def -eleRange  501 509  deformation
	recorder EnvelopeElement -file  MSC-Concrete_1/expbrg.frc -eleRange  701 709  force
	recorder EnvelopeElement -file  MSC-Concrete_1/expbrg.def -eleRange  701 709  deformation
  recorder EnvelopeNode -file MSC-Concrete_1/inode.out -node 1057 1107 1157 1207 -dof 1 3 disp
  recorder EnvelopeNode -file MSC-Concrete_1/jnode.out -node 1051 1101 1151 1201 -dof 1 3 disp
recorder EnvelopeDrift -file MSC-Concrete_1/col_drift_l.out -iNode 1057 1107 1157 1207 -jNode 1051 1101 1151 1201 -dof 1 -perpDirn 2
recorder EnvelopeDrift -file MSC-Concrete_1/col_drift_t.out -iNode 1057 1107 1157 1207 -jNode 1051 1101 1151 1201 -dof 3 -perpDirn 2
	recorder EnvelopeElement -file    MSC-Concrete_1/girder.frc -eleRange 100001 100054  force
	recorder EnvelopeElement -file    MSC-Concrete_1/transverse.frc -eleRange 120001 120030  force
	recorder EnvelopeNode -file    MSC-Concrete_1/girder.out -nodeRange 10001 10054 -dof 1 2 3 4 5 6 disp
	recorder EnvelopeElement -file  MSC-Concrete_1/impact.frc -eleRange 14001 14012  force
	recorder EnvelopeElement -file  MSC-Concrete_1/impact.def -eleRange 14001 14012  deformation

	# ***MODIFICATION***
	# Record for plotting
	set title ColumnTopDisplacement
	recorder Node -file MSC-Concrete_1/plotTopNode1dof3.out -closeOnWrite -node 1051 -dof 3 disp
	recorder Node -file MSC-Concrete_1/plotTopNode1dof2.out -closeOnWrite -node 1051 -dof 2 disp
	recorder Element -file MSC-Concrete_1/colBottomSF.frc  -closeOnWrite -ele 1057 section 1 force
	recorder Node -file MSC-Concrete_1/plotTopNode2dof3.out -closeOnWrite -node 1151 -dof 3 disp
	recorder Node -file MSC-Concrete_1/plotTopNode2dof2.out -closeOnWrite -node 1151 -dof 2 disp
	recorder Element -file MSC-Concrete_1/CurvatureColBottom.out -closeOnWrite -ele 1057 section 1 deformation
	recorder Element -file MSC-Concrete_1/momentColBottom.out -closeOnWrite -ele 1057 section 1 force
	recorder Element -file MSC-Concrete_1/plasticRotColBottom.out -closeOnWrite -ele 1057 plasticDeformation
	recorder Element -file  MSC-Concrete_1/fxdBrgForce.out -closeOnWrite -ele  504  force
	recorder Element -file  MSC-Concrete_1/fxdBrgDisp.out -closeOnWrite -ele  504  deformation
	# recorder plot MSC-Concrete_1/plotTopNode.out $title 0 0 400 400 -columns 2 1
#
#==========================================================================
#                       DEFINE GRAVITY LOADS
#==========================================================================
#
recorder display "longitudinal view" 10 10 750 600 -wipe
prp 0 0 0;
vup  0  1 0
vpn  1  0 0;
viewWindow -202.20659999999998 202.20659999999998 -900 700
display 1 2 40
port -1 1 -1 1 # area of window that will be drawn into
fill 1 # fill mode
recorder display "Displacement view 2" 770 10 750 600 -wipe
prp 1181.103 0. 102.2066;
vup  0  1  0
vpn  0  0  1
viewWindow -1381.103 1381.103 -900 700
display 1 2 40
port -1 1 -1 1 # area of window that will be drawn into
fill 1 # fill mode
recorder display "Displacement view 3" 1650 10 1500 600 -wipe
prp 1181.103 236.22 0;
vup  0  0  1
vpn  0  1  0
viewWindow -1281.103 1281.103 -302.2066 302.2066
display 1 2 40
port -1 1 -1 1 # area of window that will be drawn into
fill 1 # fill mode
#
#==========================================================================
#                       DEFINE GRAVITY and TRUCK LOADS
#==========================================================================
#
#
pattern Plain 1 "Linear" {
#           Node     X   Y     Z   Mx   My   Mz
#======================================================================================
#              DECK WEIGHT
#======================================================================================
#       DECK NUMBER 1
load 10001 0.0 -24.25492862315935 0 0 0 0
load 10002 0.0 -24.25492862315935 0 0 0 0
load 10003 0.0 -24.25492862315935 0 0 0 0
load 10004 0.0 -24.25492862315935 0 0 0 0
load 10005 0.0 -24.25492862315935 0 0 0 0
load 10006 0.0 -24.25492862315935 0 0 0 0
load 10007 0.0 -24.25492862315935 0 0 0 0
load 10008 0.0 -24.25492862315935 0 0 0 0
load 10009 0.0 -24.25492862315935 0 0 0 0
load 10010 0.0 -24.25492862315935 0 0 0 0
load 10011 0.0 -24.25492862315935 0 0 0 0
load 10012 0.0 -24.25492862315935 0 0 0 0
load 10013 0.0 -24.25492862315935 0 0 0 0
load 10014 0.0 -24.25492862315935 0 0 0 0
load 10015 0.0 -24.25492862315935 0 0 0 0
#       DECK NUMBER 2
load 10016 0.0 -24.25492862315935 0 0 0 0
load 10017 0.0 -24.25492862315935 0 0 0 0
load 10018 0.0 -24.25492862315935 0 0 0 0
load 10019 0.0 -24.25492862315935 0 0 0 0
load 10020 0.0 -24.25492862315935 0 0 0 0
load 10021 0.0 -24.25492862315935 0 0 0 0
load 10022 0.0 -24.25492862315935 0 0 0 0
load 10023 0.0 -24.25492862315935 0 0 0 0
load 10024 0.0 -24.25492862315935 0 0 0 0
load 10025 0.0 -24.25492862315935 0 0 0 0
load 10026 0.0 -24.25492862315935 0 0 0 0
load 10027 0.0 -24.25492862315935 0 0 0 0
load 10028 0.0 -24.25492862315935 0 0 0 0
load 10029 0.0 -24.25492862315935 0 0 0 0
load 10030 0.0 -24.25492862315935 0 0 0 0
#       DECK NUMBER 3
load 10031 0.0 -24.25492862315935 0 0 0 0
load 10032 0.0 -24.25492862315935 0 0 0 0
load 10033 0.0 -24.25492862315935 0 0 0 0
load 10034 0.0 -24.25492862315935 0 0 0 0
load 10035 0.0 -24.25492862315935 0 0 0 0
load 10036 0.0 -24.25492862315935 0 0 0 0
load 10037 0.0 -24.25492862315935 0 0 0 0
load 10038 0.0 -24.25492862315935 0 0 0 0
load 10039 0.0 -24.25492862315935 0 0 0 0
load 10040 0.0 -24.25492862315935 0 0 0 0
load 10041 0.0 -24.25492862315935 0 0 0 0
load 10042 0.0 -24.25492862315935 0 0 0 0
load 10043 0.0 -24.25492862315935 0 0 0 0
load 10044 0.0 -24.25492862315935 0 0 0 0
load 10045 0.0 -24.25492862315935 0 0 0 0
#======================================================================================
#              BENT CAP WEIGHT
#======================================================================================
set  bcm   [expr -386.4*(102.2066/75.)*($bWidth*$bDepth)*0.03397/(3.5*4.0*144)]  ; # bent cap mass for 75 inch section (k-s^2/in)
set  bcm2   [expr $bcm/2.]
#
#          Bent No. 2
#       node X-mass   Y-mass   Z-mass   MX-mass  MY-mass  MZ-mass
load 510 0 $bcm2  0 0 0 0
load 511 0 $bcm  0 0 0 0
load 512 0 $bcm2  0 0 0 0
#
#          Bent No. 3
#       node X-mass   Y-mass   Z-mass   MX-mass  MY-mass  MZ-mass
load 516 0 $bcm2  0 0 0 0
load 517 0 $bcm  0 0 0 0
load 518 0 $bcm2  0 0 0 0
#======================================================================================
#              COLUMN WEIGHT
#======================================================================================
set  colm   -3.0502254285300956  ; # column mass for 78.74 inch section (k-s^2/in)
set  colm2   [expr $colm/2.]
#
#    Bent No. 1, Column No. 1
#       node X-mass   Y-mass   Z-mass   MX-mass  MY-mass  MZ-mass
load 1051 0 $colm2  0  0  0  0
load 1052 0 $colm  0  0  0  0
load 1053 0 $colm  0  0  0  0
load 1058 0 $colm2  0  0  0  0
#===================================================================
#
#    Bent No. 1, Column No. 2
#       node X-mass   Y-mass   Z-mass   MX-mass  MY-mass  MZ-mass
load 1101 0 $colm2  0  0  0  0
load 1102 0 $colm  0  0  0  0
load 1103 0 $colm  0  0  0  0
load 1108 0 $colm2  0  0  0  0
#===================================================================
#
#    Bent No. 2, Column No. 1
#       node X-mass   Y-mass   Z-mass   MX-mass  MY-mass  MZ-mass
load 1151 0 $colm2  0  0  0  0
load 1152 0 $colm  0  0  0  0
load 1153 0 $colm  0  0  0  0
load 1158 0 $colm2  0  0  0  0
#===================================================================
#
#    Bent No. 2, Column No. 2
#       node X-mass   Y-mass   Z-mass   MX-mass  MY-mass  MZ-mass
load 1201 0 $colm2  0  0  0  0
load 1202 0 $colm  0  0  0  0
load 1203 0 $colm  0  0  0  0
load 1208 0 $colm2  0  0  0  0
#===================================================================
}
#
#==========================================================================
#             START OF ANALYSIS GENERATION FOR GRAVITY ANALYSIS
#==========================================================================
#
# Create the convergence test
test NormDispIncr 1.0e-6    100     1
system SparseGEN
#
algorithm  NewtonLineSearch
#
integrator LoadControl   .2   1  .2   .2
#
numberer   RCM
#
constraints Plain
#
analysis Static
#
#==========================================================================
#             PERFORM GRAVITY LOAD ANALYSIS
#==========================================================================
#
set ok [analyze 5]
#
loadConst -time 0.0
#
puts "################################################"
puts "Gravity Analysis Complete"
puts "################################################"
set ok_file [open [concat $name/ok.out] w ]
puts $ok_file "$ok"
close $ok_file
set N  10
ModalAnalysis $N      $name
puts "here" 
#
loadConst -time 0.0
#
#  Set up the acceleration record ground motions.
#  ***MODIFICATION*** We have ground motion in gm_long.txt in m/sec2. Here it needs to be applied in inch/sec2.
set g 39.3701

set ground_motion_x "Series -dt $delta_t_gm -filePath [concat gm_long.txt]  -factor [expr 1.00*$g]"
set ground_motion_y "Series -dt $delta_t_gm -filePath [concat gm_vert.txt]  -factor [expr 1.00*$g]"
set ground_motion_z "Series -dt $delta_t_gm -filePath [concat gm_perp.txt]  -factor [expr 1.00*$g]"
#
#                          tag   dir   accel series arg
pattern UniformExcitation   2     1   -accel        $ground_motion_x
pattern UniformExcitation   3     3   -accel        $ground_motion_z
#
#===SET UP TRANSIENT ANALYSIS=========================================================
#
#                  Tol     Iter   Flag
test NormDispIncr 1.0e-5    100     3
#
#Create the solution algorithm
algorithm NewtonLineSearch
#
#Create damping
set ww [eigen 2]
set wi [expr sqrt([lindex $ww 0])]
set wj [expr sqrt([lindex $ww 1])]
set xi 0.0579; # damping coefficient in the first 2 modes
set alpha [expr $xi*(2*$wi*$wj)/($wi+$wj)]
set beta  [expr $xi*(2)/($wi+$wj)]
set f1 [expr $wi/(2*3.14)]
set f2 [expr $wj/(2*3.14)]
puts "f_1 = $f1 Hz"
puts "f_2 = $f2 Hz"
#         alpa_m   beta   beta_init
rayleigh  $alpha    0.0     $beta     0.0
puts "alpha = $alpha"
puts "init_beta = $beta"
puts "wi = $wi"
puts "wj = $wj"
#
# ***MODIFICATION*** Record the fundamental period
set periodFile [open [concat $name/fundamentalPeriod.out] w]
set funPeriod [expr 1/$f1]
puts $periodFile $funPeriod

#Create the system of equation storage and solver
system SparseGEN
#
# Create the constraint handler
constraints Plain
#
# Create integration scheme
integrator TRBDF2
#
# Create the DOF numberer

numberer RCM
#
#  Create the transient analysis
analysis Transient
#
#===END OF ANALYSIS GENERATION=========================================================
#
# ***MODIFICATION***
# The following variables are coming from Swanand's MAIN file. Hence they are commented out.
# set dt 0.05
# set record_length 3000

# ***MODIFICATION*** Printing curvature to a file
set curvatureFile [open [concat $name/curvatureColBottom01.out] w]
set momentFile [open [concat $name/momentColBottom01.out] w]
set forceFile [open [concat $name/forceColBottom01.out] w]

# ***MODIFICATION*** File for non-convergence
set nonConvergenceFile [open [concat $name/nonconvergenceFile.out] w]

set tFinal [expr  $record_length * $delta_t_gm]
set tFinal 32.0
set tCurrent [getTime]
set ok 0
#
# Perform the transient analysis
# puts "Analysis running. The time step is 0.05."
while {$ok == 0 && $tCurrent < $tFinal} {
 
    set ok [analyze 1 $dt]
    # puts [getTime]

    # ***MODIFICATION*** Printing curvature at each time step
    set a [sectionDeformation 1057 1 2]
    puts $curvatureFile $a

    set b [sectionForce 1057 1 2]
    puts $momentFile $b

    set c [sectionForce 1057 1]
    puts $forceFile $c

    puts $nonConvergenceFile $ok

    set tCurrent [getTime]


    }


# set afterShaking [open [concat $name/afterShakingPeriod.out] w]
# set N  1
# ModalAnalysis $N      $afterShaking 
ModalAnalysis $N      $name

# ***MODIFICATION*** Record the fundamental period after shaking

set ww [eigen 2]
set wi [expr sqrt([lindex $ww 0])]
set f1_af [expr $wi/(2*3.14)]
puts "f_1_af = $f1_af Hz"
set periodFile [open [concat $name/elongatedPeriod.out] w]
set funPeriod [expr 1/$f1_af]
puts $periodFile $funPeriod

close $curvatureFile
close $nonConvergenceFile

set endt [clock clicks -milliseconds]
set totaltime [expr ($endt-$begin)]
set totaltimem [expr ($endt-$begin)/60000.0]
 
puts "Time in hours: [expr $totaltimem/60.]"
puts "$totaltimem is the total time in minutes"

set a [sectionDeformation 1057 1 2]
puts "Curvature at the end is: $a"

puts "Run completed with column diameter: $parameterFEM1 inches."
