cum_income_shares = [0.1,0.3,0.6,1.0]

bin_pct = cum_income_shares / 1

bin_areas = {}

for i, cum_income_share in enumerate(cum_income_shares):
  if i == 0:
    prev_cum_income_share = 0
    
  else:
    prev_cum_income_share = cum_income_shares[i-1]
  
  bin_areas[i] = ((prev_cum_income_share + cum_income_share) / 2) * bin_pct

gini_coef = 0

for bin in bin_areas:
  gini_coef += bin_areas[bin]