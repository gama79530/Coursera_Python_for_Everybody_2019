str = 'X-DSPAM-Confidence:0.8475'
fp = float( str[ str.find(':')+1 : ] )
print( fp )