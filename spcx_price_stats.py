import statistics

# date, open, high, low, close, volume
rows = [
("Jun12", 150.00, 176.52, 150.00, 161.00, 500000000),
("Jun15", 171.74, 193.00, 168.35, 192.50, 256226632),
("Jun16", 200.51, 225.64, 195.13, 201.80, 322149250),
("Jun17", 209.84, 213.80, 187.01, 191.82, 201719498),
("Jun18", 188.39, 190.00, 172.11, 185.00, 272126781),
("Jun22", 176.04, 176.75, 154.00, 154.60, 169183799),
("Jun23", 151.06, 165.50, 147.11, 156.11, 155848109),
("Jun24", 154.20, 159.86, 150.72, 154.54, 76101541),
("Jun25", 156.63, 160.65, 150.00, 153.00, 62212435),
("Jun26", 150.62, 158.40, 148.51, 153.23, 126932861),
("Jun29", 157.36, 166.17, 151.74, 164.19, 81443101),
("Jun30", 163.38, 172.40, 161.64, 170.86, 82047546),
("Jul01", 171.57, 171.74, 155.00, 157.54, 109317597),
("Jul02", 159.73, 162.16, 155.88, 162.00, 61257120),
("Jul06", 165.95, 167.90, 155.04, 160.42, 188831328),
("Jul07", 158.92, 159.30, 148.86, 149.47, 83779737),
("Jul08", 152.55, 152.93, 145.20, 148.30, 60720186),
("Jul09", 150.45, 153.50, 147.59, 152.16, 45943042),
]

prev_close = 135.00  # IPO price
up_vol, down_vol, up_days, down_days = 0,0,0,0
print(f"{'Date':<6}{'Close':>8}{'Chg%':>8}{'Volume':>14}  Dir")
for d,o,h,l,c,v in rows:
    chg = (c-prev_close)/prev_close*100
    direction = "UP" if c>=prev_close else "DOWN"
    if direction=="UP":
        up_vol+=v; up_days+=1
    else:
        down_vol+=v; down_days+=1
    print(f"{d:<6}{c:>8.2f}{chg:>7.1f}%{v:>14,}  {direction}")
    prev_close = c

print()
print(f"Up days: {up_days}, avg volume: {up_vol/up_days:,.0f}")
print(f"Down days: {down_days}, avg volume: {down_vol/down_days:,.0f}")
print(f"ATH: 225.64 (Jun16, day 4). ATL: 145.20 (Jul8, day ~19)")
print(f"Peak-to-trough drawdown from ATH to ATL: {(145.20-225.64)/225.64*100:.1f}%")
print(f"Close vs IPO price ($135) on Jul9: {(152.16-135)/135*100:.1f}%")
print(f"Close vs IPO open ($150) on Jul9: {(152.16-150)/150*100:.1f}%")

# correlate: rolling 5-day volume trend during rally June29-Jul2 into Nasdaq100 inclusion vs crash Jul7
rally_vol = [126932861,81443101,82047546,109317597,61257120]  # Jun26-Jul2
print(f"\nAvg volume during pre-inclusion rally (Jun26-Jul2): {sum(rally_vol)/len(rally_vol):,.0f}")
print(f"Volume on Nasdaq-100 inclusion day (Jul7, -6.8% day): {83779737:,}")
print(f"Volume day after (Jul8, new ATL): {60720186:,}")

print("\n--- Post-climax phase only (Jun22 onward, excluding IPO-week settlement noise) ---")
post = rows[5:]  # Jun22 onward
prev_close = 154.60  # close before Jun22... actually use Jun18 close as baseline
prev_close = 185.00
up_vol,down_vol,up_days,down_days=0,0,0,0
for d,o,h,l,c,v in post:
    direction = "UP" if c>=prev_close else "DOWN"
    if direction=="UP":
        up_vol+=v; up_days+=1
    else:
        down_vol+=v; down_days+=1
    prev_close=c
print(f"Up days: {up_days}, total vol: {up_vol:,}, avg: {up_vol/up_days:,.0f}")
print(f"Down days: {down_days}, total vol: {down_vol:,}, avg: {down_vol/down_days:,.0f}")
print(f"Down-day avg volume premium over up-day avg: {(down_vol/down_days)/(up_vol/up_days)*100-100:.1f}%")
