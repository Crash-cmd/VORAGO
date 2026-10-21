from customtkinter import *

def question_loader(parent,qset,qno=0):
    pra_q = parent
            correct = 0
            corrrect_answer = qset[qno].get("correct")
            def answer(btn):
                nonlocal qno
                nonlocal correct
                all_opt=[btn.master.grid_slaves(row=1,column=0),btn.master.grid_slaves(row=2,column=0),
                        btn.master.grid_slaves(row=3,column=0),btn.master.grid_slaves(row=4,column=0)]
                for opt in all_opt:
                    opt[0].configure(state=DISABLED)
                all_opt.remove(btn.master.grid_slaves(row=corrrect_answer+1,column=0))
                btn.master.grid_slaves(row=corrrect_answer+1,column=0)[0].configure(fg_color="green")
                for wrong_opt in all_opt:
                    wrong_opt[0].configure(fg_color="red",hover=FALSE)
                if btn.grid_info().get("row")-1 == corrrect_answer:
                    ans_l.configure(text="Your answer is correct ✅")
                    btn.configure(fg_color="green",hover = FALSE)
                    correct += 1
                elif btn.grid_info().get("row")-1 != corrrect_answer:
                    ans_l.configure(text="Your answer is wrong ❌,The correct answer is option no."+str(corrrect_answer)+")" +qset[qno].get("options")[corrrect_answer],wraplength=1000)
                    btn.configure(fg_color="red",hover=FALSE)
                print(correct)
                def check_procces():
                    nonlocal correct
                    nonlocal qno
                    qno +=1
                    nonlocal qset
                    nonlocal corrrect_answer
                    if qno < len(qset):
                        corrrect_answer = qset[qno].get("correct")
                        label.configure(text=qset[qno].get("question"))
                        b1.configure(text=qset[qno].get("options")[0],hover_color="green",hover=TRUE,fg_color="#3489eb",state=NORMAL)
                        b2.configure(text=qset[qno].get("options")[1],hover_color="green",hover=TRUE,fg_color="#3489eb",state=NORMAL)
                        b3.configure(text=qset[qno].get("options")[2],hover_color="green",hover=TRUE,fg_color="#3489eb",state=NORMAL)
                        b4.configure(text=qset[qno].get("options")[3],hover_color="green",hover=TRUE,fg_color="#3489eb",state=NORMAL)
                        qlimit.configure(text=str(qno+1)+"/15")
                        ans_l.configure(text="")
                    else:
                        for wid in btn.master.winfo_children():
                            wid.destroy()
                        l = CTkLabel(parent,text="You have completed this quiz",font=("Fira Sans Condensed",60))
                        l.grid(sticky="n",column=0,row=1)
                        l2 = CTkLabel(parent,text="Score:"+str(correct)+"/15",font=("Fira Sans Condensed",60))
                        l2.grid(sticky="n",column=0,row=2)
                        if correct == len(qset):
                            l3 = CTkLabel(parent,text="Congrats You have gotten all of it right 🎉",font=("Fira Sans Condensed",60))
                            l3.grid(sticky="n",column=0,row=3)

                pra_q.after(2000,check_procces)
                    
                    
            label = CTkLabel(parent,text=qset[qno].get("question"),font=("Fira Sans Condensed",40))
            label.grid(sticky="n",row=0,column=0,pady=30)
            b1 = CTkButton(parent,text=qset[qno].get("options")[0],font=("Fira Sans Condensed",20),height=50,width=75,hover_color="green",command=lambda:answer(b1),fg_color="#3489eb")
            b1.grid(sticky="n",row=1,column=0,pady=30)
            b2 = CTkButton(parent,text=qset[qno].get("options")[1],font=("Fira Sans Condensed",20),height=50,width=75,hover_color="green",command=lambda:answer(b2),fg_color="#3489eb")
            b2.grid(sticky="n",row=2,column=0,pady=30)
            b3 = CTkButton(parent,text=qset[qno].get("options")[2],font=("Fira Sans Condensed",20),height=50,width=75,hover_color="green",command=lambda:answer(b3),fg_color="#3489eb")
            b3.grid(sticky="n",row=3,column=0,pady=30)
            b4 = CTkButton(parent,text=qset[qno].get("options")[3],font=("Fira Sans Condensed",20),height=50,width=75,hover_color="green",command=lambda:answer(b4),fg_color="#3489eb")
            b4.grid(sticky="n",row=4,column=0,pady=30)
            qlimit = CTkLabel(pra_q,text=str(qno+1)+"/15",font=("Fira Sans Condensed",30),justify="left")
            qlimit.grid(column=0,row=0,sticky ="ne")
            ans_l =CTkLabel(parent,text="",font=("Fira Sans Condensed",40))
            ans_l.grid(sticky="s",row=5,column=0,pady=50)
