#coding:l1
import json,os,sys,urllib.request as u,zlib
U=os.environ.get("MAKEFUN_ENV_URL") or sys.exit("MAKEFUN_ENV_URL is not set")
V=[0,100,320,330,500,900,0]
ND=[14,18,31,33,-14,-18,-31,-33]
KD=[1,15,16,17,-1,-15,-16,-17]
BD=[15,17,-15,-17]
RD=[1,16,-1,-16]
T='€€€€€€€€±Ãž¯¢¿‘z}ƒ œŒvy†ƒŠ‹†ˆtr}†ˆƒ…ss~~{znvtxŒ“u€€€€€€€€,SogžOxJ[k¤’‹Ÿƒwhž’ ªÀ¤–{ˆ‰š’¢‰‹y‚ˆ†Ž‰Š|t{†…‰ˆŒxqez~‰yvKucowrvtq‚Wmskƒ|sˆwy‰hx’•”‘™’~‚‰™’’ƒ}††‘†…‚€‡‡‡‡‰…‚‡ˆ€ƒŠ€o~yuyzlu•™Ÿ„•Ÿ¨¡–}‰’ˆ–žˆtzƒŒ‘|vnsz„|ƒtisxw€}ojxv{…}\\vy€ˆˆƒmsr€Ž†–•–tl}€xœŽ›ywƒ„Žœ—œrrxxˆ€{s{{~~yz}‡‚n|…„‡~€w{…xspg_‹ˆxdo†Žv||~mq{Œxvƒ‹uwvzrqsyngrlijofyyuijqxr€ƒ|`jx„„x’†e„rŒ‡€€€€€€€€ÙÖÏÃÉÂÒÝ¯²ª¡œš©ªŒ†‚‚ˆˆ†„~|||‚ƒ}€€}|†„„…†€|€€€€€€€€cmyrpr`Ns|s{stftv…„{vkw‹‹‹…„ww}ˆŒˆˆ‚wt~‡…~vukv{}vtjqftxuwg`yuz||{wt|~ƒz~y~y|€ƒ€‚~„†„‡…}†‰ƒ…~{z~„…†|xyw|‚{xrt{t}{x}w†…‰‡††„‚…††…~„ƒƒƒ‚‚~}~‚†€€‚„‚}}|z~€}|z|x}}€{{z~{}y‚v{‹‹‰…ŠwŠ”Œ€vƒ„˜—‘‰„‹Œ–œ”œ’wŽ‰—‘“‹xr‡ƒ„ˆ…‚utqxxtnporuj}pvk[nwwz‡‚wzˆ‡ˆˆ“‹……ˆ‹‡Š––†|‹Œw~ŠŒ‹„zv~…Š‹ˆƒ{rz‚†‡‚}weouzrytj'
MG=[0]+[T[i*64:(i+1)*64].encode('latin-1') for i in range(6)]
EG=[0]+[T[384+i*64:384+(i+1)*64].encode('latin-1') for i in range(6)]
MV=[0,82,337,365,477,1025,0]
EV=[0,94,281,297,512,936,0]
PH=[0,0,1,1,2,4,0]
B=[0]*128; W=1; C=0; E=-1; K=[4,116]
N=0; LIM=200000; TT={}
H=set()
MATE=100000
KIL=[[0,0] for _ in range(128)]
TB={1387844529:b'\r #\0\0\0',1733649890:b'\0\0\0\0\0\n\0\0\r$\0\0\0',1764038260:b'\0#.\0	\0\0\0\n	\0\0\n\0\0\0\0\0\0',2725208568:b'\0\0"$!\0"\0(\0\0 ',2887717486:b'\0"$#	\r )4\x005\0',3427167504:b'\0"\0\0&\0\'\0\0\r\0',3814251892:b'\0\r\0\r!!\0\r\0"\0\0\0\0\0\0\0\0\0',3960552000:b'\r\0\r"#\0'}
def post(p,b):
 r=u.Request(U+p,data=json.dumps(b).encode(),headers={"content-type":"application/json"})
 try:
  with u.urlopen(r) as s: return json.load(s)
 except Exception as e: sys.exit(str(e))
def parse(f):
 global B,W,C,E,K
 B=[0]*128
 q=f.split(); K=[-1,-1]
 for i,row in enumerate(q[0].split("/")):
  r=7-i; fl=0
  for ch in row:
   if ch.isdigit(): fl+=int(ch)
   else:
    s=r*16+fl
    B[s]=(1 if ch.isupper() else -1)*("PNBRQK".index(ch.upper())+1)
    if abs(B[s])==6: K[0 if B[s]>0 else 1]=s
    fl+=1
 W=1 if q[1]=="w" else -1
 C=0
 for ch in q[2]:
  if ch in "KQkq": C|=1<<"KQkq".index(ch)
 E=-1 if q[3]=="-" else (int(q[3][1])-1)*16+ord(q[3][0])-97
 H.add((tuple(B),W,C,E))
def att(s,by):
 d=-16*by
 for o in (d-1,d+1):
  x=s+o
  if not(x&0x88) and B[x]==by: return True
 for o in ND:
  x=s+o
  if not(x&0x88) and B[x]==by*2: return True
 for o in KD:
  x=s+o
  if not(x&0x88) and B[x]==by*6: return True
 for o in BD:
  x=s+o
  while not(x&0x88):
   v=B[x]
   if v:
    if v==by*3 or v==by*5: return True
    break
   x+=o
 for o in RD:
  x=s+o
  while not(x&0x88):
   v=B[x]
   if v:
    if v==by*4 or v==by*5: return True
    break
   x+=o
 return False
def gen(caps):
 ms=[]
 for s in range(128):
  if s&0x88: continue
  p=B[s]
  if not p or (p>0)!=(W>0): continue
  t=abs(p)
  if t==1:
   d=16*W; lr=7 if W>0 else 0; sr=1 if W>0 else 6
   to=s+d
   if not caps and not(to&0x88) and B[to]==0:
    if (to>>4)==lr:
     for pr in (5,4,3,2): ms.append(s|(to<<7)|(pr<<14))
    else:
     ms.append(s|(to<<7))
     if (s>>4)==sr and B[s+2*d]==0: ms.append(s|((s+2*d)<<7))
   for o in (d-1,d+1):
    to=s+o
    if to&0x88: continue
    v=B[to]
    if v and (v>0)!=(W>0) and abs(v)!=6:
     if (to>>4)==lr:
      for pr in (5,4,3,2): ms.append(s|(to<<7)|(pr<<14))
     else: ms.append(s|(to<<7))
    elif to==E and E>=0: ms.append(s|(to<<7))
  elif t==2 or t==6:
   for o in ND if t==2 else KD:
    to=s+o
    if to&0x88: continue
    v=B[to]
    if v==0:
     if not caps: ms.append(s|(to<<7))
    elif (v>0)!=(W>0) and abs(v)!=6: ms.append(s|(to<<7))
   if t==6 and not caps:
    if W>0:
     if C&1 and B[5]==0 and B[6]==0 and not att(4,-1) and not att(5,-1) and not att(6,-1): ms.append(4|(6<<7))
     if C&2 and B[3]==0 and B[2]==0 and B[1]==0 and not att(4,-1) and not att(3,-1) and not att(2,-1): ms.append(4|(2<<7))
    else:
     if C&4 and B[117]==0 and B[118]==0 and not att(116,1) and not att(117,1) and not att(118,1): ms.append(116|(118<<7))
     if C&8 and B[115]==0 and B[114]==0 and B[113]==0 and not att(116,1) and not att(115,1) and not att(114,1): ms.append(116|(114<<7))
  else:
   ds=BD if t==3 else RD if t==4 else BD+RD
   for o in ds:
    to=s+o
    while not(to&0x88):
     v=B[to]
     if v==0:
      if not caps: ms.append(s|(to<<7))
     else:
      if (v>0)!=(W>0) and abs(v)!=6: ms.append(s|(to<<7))
      break
     to+=o
 return ms
def make(m):
 global W,C,E
 f=m&127; t=(m>>7)&127; pr=(m>>14)&7
 p=B[f]; cap=B[t]; cs=-1; c0=C; e0=E; rk=(-1,-1)
 if abs(p)==1 and t==E and cap==0:
  cs=t-16*W; cap=B[cs]; B[cs]=0
 B[f]=0; B[t]=pr*(1 if p>0 else -1) if pr else p
 if abs(p)==6 and abs(f-t)==2:
  rk=(t+1,t-1) if t>f else (t-2,t+1)
  B[rk[1]]=B[rk[0]]; B[rk[0]]=0
 if abs(p)==6:
  K[0 if p>0 else 1]=t; C&=~(3 if p>0 else 12)
 if f==0: C&=~2
 elif f==7: C&=~1
 elif f==112: C&=~8
 elif f==119: C&=~4
 if t==0: C&=~2
 elif t==7: C&=~1
 elif t==112: C&=~8
 elif t==119: C&=~4
 E=f+16*W if abs(p)==1 and abs(t-f)==32 else -1
 W=-W
 return (m,cap,cs,c0,e0,rk)
def unmake(u):
 global W,C,E
 m,cap,cs,C0,E0,rk=u
 f=m&127; t=(m>>7)&127; pr=(m>>14)&7
 W=-W; C,E=C0,E0
 p=B[t]
 if pr: p=1 if p>0 else -1
 B[f]=p; B[t]=0
 if cs>=0: B[cs]=cap
 elif cap: B[t]=cap
 if rk[0]>=0:
  B[rk[0]]=B[rk[1]]; B[rk[1]]=0
 if abs(p)==6: K[0 if p>0 else 1]=f
def chk():
 return att(K[0] if W<0 else K[1],W)
def ev():
 mg=0; eg=0; ph=0
 for q in range(128):
  if q&0x88: continue
  p=B[q]
  if p:
   t=abs(p); r=q>>4; f=q&7
   if p>0:
    i=(7-r)*8+f
    mg+=MV[t]+(MG[t][i]-128)*2; eg+=EV[t]+(EG[t][i]-128)*2
   else:
    i=r*8+f
    mg-=MV[t]+(MG[t][i]-128)*2; eg-=EV[t]+(EG[t][i]-128)*2
   if t>1: ph+=PH[t]
 if ph>24: ph=24
 return ((mg*ph+eg*(24-ph))//24)*W
def mv(m):
 f=m&127; t=(m>>7)&127
 v=B[t]
 s=(V[abs(v)]*10-V[abs(B[f])]) if v else 0
 if (m>>14)&7: s+=900
 return s
class Done(Exception): pass
def qs(a,be,w,ply):
 global N
 N+=1
 if N>=LIM: raise Done
 inchk=att(K[0 if w>0 else 1],-w)
 if not inchk:
  s=ev()
  if s>=be: return be
  if s>a: a=s
 ms=gen(not inchk)
 ms.sort(key=mv,reverse=True)
 legal=False
 for m in ms:
  u=make(m)
  if chk(): unmake(u); continue
  legal=True
  v=-qs(-be,-a,-w,ply+1)
  unmake(u)
  if v>=be: return be
  if v>a: a=v
 if inchk and not legal: return -MATE+ply
 return a
def srch(d,a,be,w,ply):
 global N
 N+=1
 if N>=LIM: raise Done
 if d<=0: return qs(a,be,w,ply)
 key=(tuple(B),w,C,E)
 if key in H: return 0
 e=TT.get(key)
 if e and e[0]>=d:
  if e[2]==0: return e[1]
  if e[2]==1 and e[1]>=be: return e[1]
  if e[2]==2 and e[1]<=a: return e[1]
 ms=gen(False)
 tm=e[3] if e else 0
 ms.sort(key=lambda m: (m==tm)*100000+mv(m)+(m in KIL[ply])*500,reverse=True)
 best=0; bv=-MATE; oa=a
 ic=att(K[0 if w>0 else 1],-w) if d>2 else 0
 for i,m in enumerate(ms):
  t=(m>>7)&127; cp=B[t]; pr=(m>>14)&7
  u=make(m)
  if chk(): unmake(u); continue
  r=1 if i>3 and d>2 and not ic and not cp and not pr else 0
  if i==0: v=-srch(d-1,-be,-a,-w,ply+1)
  else:
   v=-srch(d-1-r,-a-1,-a,-w,ply+1)
   if v>a: v=-srch(d-1,-be,-a,-w,ply+1)
  unmake(u)
  if v>bv: bv=v; best=m
  if v>a: a=v
  if a>=be:
   if not cp:
    KIL[ply][1]=KIL[ply][0]; KIL[ply][0]=m
   break
 if best==0:
  return -MATE+ply if att(K[0 if w>0 else 1],-w) else 0
 TT[key]=(d,bv,2 if bv<=oa else 1 if bv>=be else 0,best)
 return bv
def uci(m):
 f=m&127; t=(m>>7)&127; pr=(m>>14)&7
 s="abcdefgh"[f&7]+str((f>>4)+1)+"abcdefgh"[t&7]+str((t>>4)+1)
 return s+("nbrq"[pr-2] if pr else "")
def think(legal):
 global N
 N=0; TT.clear()
 ms=gen(False)
 if not ms: return legal[0]
 lg=[]
 for m in ms:
  u=make(m)
  if not chk(): lg.append(m)
  unmake(u)
 if not lg: return legal[0]
 if len(lg)==1:
  u=uci(lg[0]); return u if u in legal else legal[0]
 ms=lg
 ms.sort(key=mv,reverse=True)
 r=TB.get(zlib.crc32((S[0]+"|"+S[1]+"|"+S[2]).encode()))
 if r:
  k=(S[3]-8)//2
  if 0<=k<len(r) and r[k]<len(ms):
   u=uci(ms[r[k]])
   if u in legal: return u
 best=ms[0]
 sc={m:0 for m in ms}
 for d in range(1,16):
  try:
   a=-MATE; be=MATE; bb=best
   for j,m in enumerate(ms):
    u=make(m)
    if chk(): unmake(u); continue
    if j==0: v=-srch(d-1,-be,-a,W,1)
    else:
     v=-srch(d-1,-a-1,-a,W,1)
     if v>a: v=-srch(d-1,-be,-a,W,1)
    unmake(u)
    sc[m]=v
    if v>a: a=v; bb=m
   best=bb
   ms.sort(key=lambda m: sc[m],reverse=True)
   if sc[best]>MATE-200: break
  except Done:
   break
 u=uci(best)
 return u if u in legal else legal[0]
if __name__=="__main__":
 cg=0
 while True:
  g=post("/game",{})
  if g["status"]=="done": break
  while g["status"]=="your_move":
   if g["game"]!=cg: H.clear(); cg=g["game"]
   parse(g["fen"])
   S=(g["opponent"],g["opening"]["id"],g["colour"],g["plies"])
   g=post("/move",{"game":g["game"],"move":think(g["legal_moves"])})
  print(f"game {g['game']}: {g['outcome']} by {g['reason']}",file=sys.stderr)
 print(f"done: {g.get('wins')} won, {g.get('draws')} drawn, {g.get('losses')} lost",file=sys.stderr)