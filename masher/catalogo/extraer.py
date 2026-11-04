import pdfplumber, subprocess, re, json, html, sys
SRC=sys.argv[1]
pdf=pdfplumber.open(SRC)
rows=[]
for i,pg in enumerate(pdf.pages):
    xml=subprocess.run(['pdftotext','-bbox','-f',str(i+1),'-l',str(i+1),SRC,'-'],capture_output=True,text=True).stdout
    words=[(float(a),float(b),float(c),float(d),html.unescape(w)) for a,b,c,d,w in re.findall(r'<word xMin="([\d.]+)" yMin="([\d.]+)" xMax="([\d.]+)" yMax="([\d.]+)">(.*?)</word>',xml)]
    tabs=pg.find_tables()
    for t in tabs:
        for r in t.rows:
            cells=[]
            for c in r.cells[:7]:
                if c is None: cells.append(''); continue
                x0,y0,x1,y1=c
                ws=[w[4] for w in words if x0-1<=(w[0]+w[2])/2<=x1+1 and y0-1<=(w[1]+w[3])/2<=y1+1]
                cells.append(' '.join(ws))
            # colour of status column: rects right of table
            y0,y1=r.bbox[1],r.bbox[3]
            cols=[tuple(round(v,2) for v in (rc.get('non_stroking_color') or ())) for rc in pg.rects if rc['x0']>370 and rc['x0']<380 and rc['top']<(y0+y1)/2<rc['bottom']]
            rows.append({'page':i+1,'cells':cells,'color':cols[:1],'y':(y0,y1)})
json.dump(rows,open('rows.json','w'),ensure_ascii=False,indent=1)
print(len(rows))
