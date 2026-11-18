"""CPU Scheduling Visualizer. Run with: streamlit run app.py"""
from collections import deque
import pandas as pd
import streamlit as st

st.set_page_config(page_title="CPU Scheduling Visualizer", page_icon="⚙️", layout="wide")

def add_segment(schedule, pid, start, end):
    if end <= start: return
    if schedule and schedule[-1]["process"] == pid and schedule[-1]["end"] == start:
        schedule[-1]["end"] = end
    else: schedule.append({"process": pid, "start": start, "end": end})

def fcfs(ps):
    schedule=[]; first={}; completion={}; t=0
    for p in sorted(ps,key=lambda x:(x["arrival"],x["order"])):
        if t<p["arrival"]: add_segment(schedule,"Idle",t,p["arrival"]); t=p["arrival"]
        first[p["id"]]=t; end=t+p["burst"]; add_segment(schedule,p["id"],t,end); t=end; completion[p["id"]]=t
    return schedule,first,completion

def choice_schedule(ps, key):
    rem={p["id"]:p.copy() for p in ps}; schedule=[]; first={}; completion={}; t=0
    while rem:
        ready=[p for p in rem.values() if p["arrival"]<=t]
        if not ready:
            n=min(p["arrival"] for p in rem.values()); add_segment(schedule,"Idle",t,n); t=n; continue
        p=min(ready,key=lambda x:(key(x),x["arrival"],x["order"])); first[p["id"]]=t
        end=t+p["burst"]; add_segment(schedule,p["id"],t,end); t=end; completion[p["id"]]=t; del rem[p["id"]]
    return schedule,first,completion

def rr(ps,q):
    ordered=sorted((p.copy() for p in ps),key=lambda x:(x["arrival"],x["order"])); rem={p["id"]:p["burst"] for p in ordered}
    schedule=[]; first={}; completion={}; ready=deque(); t=0; i=0
    while len(completion)<len(ordered):
        while i<len(ordered) and ordered[i]["arrival"]<=t: ready.append(ordered[i]); i+=1
        if not ready:
            n=ordered[i]["arrival"]; add_segment(schedule,"Idle",t,n); t=n; continue
        p=ready.popleft(); pid=p["id"]; first.setdefault(pid,t); run=min(q,rem[pid]); end=t+run
        add_segment(schedule,pid,t,end); t=end; rem[pid]-=run
        while i<len(ordered) and ordered[i]["arrival"]<=t: ready.append(ordered[i]); i+=1
        if rem[pid]: ready.append(p)
        else: completion[pid]=t
    return schedule,first,completion

def result(ps, alg, q):
    if alg=="FCFS": s,f,c=fcfs(ps)
    elif alg=="SJF (non-preemptive)": s,f,c=choice_schedule(ps,lambda p:p["burst"])
    elif alg=="Priority (non-preemptive)": s,f,c=choice_schedule(ps,lambda p:p["priority"])
    else: s,f,c=rr(ps,q)
    rows=[]
    for p in ps:
        pid=p["id"]; tat=c[pid]-p["arrival"]
        rows.append({"Process":pid,"Arrival":p["arrival"],"Burst":p["burst"],"Priority":p["priority"],"Completion":c[pid],"Waiting":tat-p["burst"],"Turnaround":tat,"Response":f[pid]-p["arrival"]})
    return s,pd.DataFrame(rows)

st.title("⚙️ CPU Scheduling Visualizer & Performance Analyzer")
st.caption("Enter processes, then compare FCFS, non-preemptive SJF, non-preemptive Priority, and Round Robin.")
with st.sidebar:
    st.header("Settings")
    count=st.number_input("Number of processes",1,12,4,1)
    quantum=st.number_input("Round Robin time quantum",1,100,2,1)
    st.caption("Smaller priority number means higher priority. Ties use arrival order.")
    if st.button("Load sample data"):
        st.session_state.process_data=pd.DataFrame([
            {"Process":"P1","Arrival Time":0,"Burst Time":5,"Priority":2},
            {"Process":"P2","Arrival Time":1,"Burst Time":3,"Priority":1},
            {"Process":"P3","Arrival Time":2,"Burst Time":1,"Priority":3},
            {"Process":"P4","Arrival Time":4,"Burst Time":2,"Priority":2},])

if "process_data" not in st.session_state:
    st.session_state.process_data=pd.DataFrame([{"Process":f"P{i+1}","Arrival Time":0,"Burst Time":1,"Priority":1} for i in range(count)])
data=st.session_state.process_data
if len(data)!=count:
    data=pd.DataFrame([{"Process":f"P{i+1}","Arrival Time":0,"Burst Time":1,"Priority":1} for i in range(count)])
st.subheader("Process input")
edited=st.data_editor(data,num_rows="fixed",hide_index=True,use_container_width=True,
    column_config={"Process":st.column_config.TextColumn(disabled=True),"Arrival Time":st.column_config.NumberColumn(min_value=0,step=1),"Burst Time":st.column_config.NumberColumn(min_value=1,step=1),"Priority":st.column_config.NumberColumn(step=1)})
st.session_state.process_data=edited

if st.button("Run comparison",type="primary",use_container_width=True):
    try:
        if edited[["Arrival Time","Burst Time","Priority"]].isna().any().any(): raise ValueError("Fill in every numeric field.")
        ps=[]
        for i,row in edited.iterrows():
            a,b,pr=(int(row[c]) for c in ("Arrival Time","Burst Time","Priority"))
            if a<0 or b<=0: raise ValueError("Arrival times must be nonnegative and burst times must be positive.")
            ps.append({"id":str(row["Process"]),"arrival":a,"burst":b,"priority":pr,"order":i})
        st.session_state.results={}
        for alg in ("FCFS","SJF (non-preemptive)","Priority (non-preemptive)","Round Robin"):
            st.session_state.results[alg]=result(ps,alg,int(quantum))
        st.session_state.ran=True
    except (ValueError,TypeError) as e: st.error(str(e))

if st.session_state.get("ran"):
    results=st.session_state.results
    comparison=[]
    for alg,(segments,table) in results.items():
        st.subheader(alg)
        chart=pd.DataFrame([{"Process":x["process"],"Start":x["start"],"Duration":x["end"]-x["start"]} for x in segments])
        st.bar_chart(chart.set_index("Start")["Duration"],color="#4F46E5")
        st.caption("Timeline: " + "  →  ".join(f'{x["start"]} | {x["process"]} | {x["end"]}' for x in segments))
        st.dataframe(table,hide_index=True,use_container_width=True)
        comparison.append({"Algorithm":alg,"Average waiting":table.Waiting.mean(),"Average turnaround":table.Turnaround.mean(),"Average response":table.Response.mean()})
    st.subheader("Algorithm comparison")
    st.dataframe(pd.DataFrame(comparison).round(2),hide_index=True,use_container_width=True)
    st.bar_chart(pd.DataFrame(comparison).set_index("Algorithm"))
