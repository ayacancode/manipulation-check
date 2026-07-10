rows = [
("Jun 12","150.00",161.00,500000000),
("Jun 15","171.74",192.50,256226632),
("Jun 16","200.51",201.80,322149250),
("Jun 17","209.84",191.82,201719498),
("Jun 18","188.39",185.00,272126781),
("Jun 22","176.04",154.60,169183799),
("Jun 23","151.06",156.11,155848109),
("Jun 24","154.20",154.54,76101541),
("Jun 25","156.63",153.00,62212435),
("Jun 26","150.62",153.23,126932861),
("Jun 29","157.36",164.19,81443101),
("Jun 30","163.38",170.86,82047546),
("Jul 1","171.57",157.54,109317597),
("Jul 2","159.73",162.00,61257120),
("Jul 6","165.95",160.42,188831328),
("Jul 7","158.92",149.47,83779737),
("Jul 8","152.55",148.30,60720186),
("Jul 9","150.45",152.16,45943042),
]

n = len(rows)
x0, x1 = 60, 980
def xf(i):
    return x0 + (x1-x0)*i/(n-1)

pmin, pmax = 140, 230
py0, py1 = 20, 300  # svg y for price panel (y1 is bottom)
def yf(p):
    return py0 + (pmax-p)/(pmax-pmin)*(py1-py0)

vmax = 520000000
vy0, vy1 = 330, 470
def vh(v):
    return v/vmax*(vy1-vy0)

# price line path
pts = [(xf(i), yf(c)) for i,(d,o,c,v) in enumerate(rows)]
path = "M " + " L ".join(f"{x:.1f},{y:.1f}" for x,y in pts)
print("PRICE PATH:")
print(path)

print("\nVOLUME BARS (x,y,width,height,close>=prevclose):")
prev = 135.00
bw = (x1-x0)/(n-1)*0.5
for i,(d,o,c,v) in enumerate(rows):
    up = c >= prev
    x = xf(i) - bw/2
    h = vh(v)
    y = vy1 - h
    print(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{h:.1f}" class="{"vol-up" if up else "vol-down"}"/>  <!-- {d} v={v:,} -->')
    prev = c

print("\nX-AXIS LABELS:")
for i,(d,o,c,v) in enumerate(rows):
    print(f'<text x="{xf(i):.1f}" y="490" class="axis-label">{d}</text>')

print("\nDOTS at key points (IPO price line, ATH, ATL, current):")
for i,(d,o,c,v) in enumerate(rows):
    print(f"{d}: x={xf(i):.1f} y={yf(c):.1f} close={c}")

print("\nY gridlines for price (140,160,180,200,220):")
for p in [140,160,180,200,220]:
    print(f'y={yf(p):.1f} for price {p}')

# IPO price reference line at 135
print(f"\nIPO price $135 line y={yf(135):.1f} (below chart min, note)")
print(f"IPO open $150 line y={yf(150):.1f}")
