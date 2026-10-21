from customtkinter import *
import practice_questions as pq

page_no = 1

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


def mtasks(mtask, maths, math_frame, heading, paragrah):
    page_no = 1
    def back(button_pressed):
        global page_no
        page_no-=1
        if page_no == 0:
            button_pressed.master.grid_forget()
            m1_pra.grid_forget()
            math_frame.grid(sticky="nswe",pady=5,row=0,column=0)
            page_no = 1
        elif page_no == 1 :
            math_frame.grid_forget()
            m1_intro.lift()
        elif page_no == 2 :
            math_frame.grid_forget()
            m1_pra.lift()

    def front(button_pressed):
        global page_no
        page_no+=1
        if page_no == 2 :
            math_frame.grid_forget()
            m1_pra.lift()
    math_frame.grid_forget()
    if mtask == 1:
            
            # math_sc_1 = CTkFrame(maths)
            # math_sc_1.grid(row=0,column=0,sticky="nswe") 
            # math_sc_1.grid_columnconfigure(0, weight=0)  # Back button column (fixed width)
            # math_sc_1.grid_columnconfigure(1, weight=1)  # Content column (EXPANDS to fill screen)
            # math_sc_1.grid_columnconfigure(2, weight=0)  # Front button column (fixed width)

            # back_b = CTkButton(math_sc_1, text="«", width=60, font=("Nasalization", 40), command=lambda: back(back_b))
            # back_b.grid(column=0, row=0, sticky="w", padx=3)

            # front_b = CTkButton(math_sc_1, text="»", font=("Nasalization", 40), width=60, command=lambda: front(front_b))
            # front_b.grid(column=2, row=0, sticky="e", padx=3)

            # m1_pra = CTkFrame(math_sc_1)
            # m1_pra.columnconfigure(0,weight=1)
            # m1_pra.rowconfigure(1,weight=1)
            # heading(m1_pra,"Practice Questions",0,0)
        
            # pra_q = CTkFrame(m1_pra)
            # pra_q.columnconfigure(0,weight=1)
        
            # question_loader(pra_q,pq.msc1_questions,0)
            # pra_q.grid(row=1,column=0,sticky="nsew",pady=5,padx=3.5)
            # m1_pra.grid(column=1, row=0, sticky="nswe")
            
            # #INTRODUCTION
            
            # m1_intro = CTkFrame(math_sc_1)
            # m1_intro.columnconfigure(0,weight=1)
            # heading(m1_intro, "Multiplying by 5", 0, 0)
            # heading(m1_intro, "Core Principle", 1, 1)
            # paragrah(m1_intro, "Multiplying by 5 is equivalent to multiplying by 10 and halving (since 5 = 10/2).", 2)
            # heading(m1_intro, "The Rule", 1, 3)
            # paragrah(m1_intro, "1. Multiply the number by 10 (shift the decimal one place right / append a zero).\n2. Divide the result by 2.", 4)
            # heading(m1_intro, "Examples", 1, 5)
            # paragrah(m1_intro, "1) 48 × 5 \n48 × 10= 480\n480 ÷ 2 = 240", 6)
            # paragrah(m1_intro, "2) 79 × 5 \n79 × 10= 790\n790 ÷ 2 = 395", 7)
            # heading(m1_intro, "Quick Application", 1, 8)
            # paragrah(m1_intro, " Financial modeling (quick tip/discount calculations)\nSoftware engineering (cheap integer scaling in embedded systems)\nEveryday estimation (splitting bills, quick unit conversions)", 9)
            # m1_intro.grid(column=1, row=0, sticky="nswe")    
            # math_sc_1.grid(sticky="nswe",row=0,column=0)
            question_loader(pra_q, pq.msc1_questions, 0)
    if mtask == 2:
            
            math_sc_1 = CTkFrame(maths)
            math_sc_1.grid(row=0,column=0,sticky="nswe") 
            math_sc_1.grid_columnconfigure(0, weight=0)  # Back button column (fixed width)
            math_sc_1.grid_columnconfigure(1, weight=1)  # Content column (EXPANDS to fill screen)
            math_sc_1.grid_columnconfigure(2, weight=0)  # Front button column (fixed width)

            back_b = CTkButton(math_sc_1, text="«", width=60, font=("Nasalization", 40), command=lambda: back(back_b))
            back_b.grid(column=0, row=0, sticky="w", padx=3)

            front_b = CTkButton(math_sc_1, text="»", font=("Nasalization", 40), width=60, command=lambda: front(front_b))
            front_b.grid(column=2, row=0, sticky="e", padx=3)

            m1_pra = CTkFrame(math_sc_1)
            m1_pra.columnconfigure(0,weight=1)
            m1_pra.rowconfigure(1,weight=1)
            heading(m1_pra,"Practice Questions",0,0)
        
            pra_q = CTkFrame(m1_pra)
            pra_q.columnconfigure(0,weight=1)
        
            question_loader(pra_q,pq.msc2_questions,0)
            pra_q.grid(row=1,column=0,sticky="nsew",pady=5,padx=3.5)
            m1_pra.grid(column=1, row=0, sticky="nswe")
            
            #INTRODUCTION
            
            m1_intro = CTkFrame(math_sc_1)
            m1_intro.columnconfigure(0,weight=1)
            heading(m1_intro, "Multiplying Numbers Near a Common Base", 0, 0)
            heading(m1_intro, "Core Principle", 1, 1)
            paragrah(m1_intro, "For numbers close to a base B (like 100), write each as B+x and B+y; then (B+x)(B+y) = B² + B(x+y) + xy, which is fast because B² and B(x+y) are simple base-shifts.", 2)
            heading(m1_intro, "The Rule", 1, 3)
            paragrah(m1_intro, "1. Choose base B (e.g., 100) and find each number's offset from B (x, y — can be negative).\n2. Compute the 'cross term' B + x + y for the leading part.\n3. Compute x×y for the trailing part and combine (append/add with carry).", 4)
            heading(m1_intro, "Examples", 1, 5)
            paragrah(m1_intro, "1) 97 × 94 (B=100, x=−3, y=−6) → leading: 100−3−6=91 → trailing: (−3)×(−6)=18 → **9118**", 6)
            paragrah(m1_intro, "2) 798 × 95 (B=100, x=−2, y=−5) → leading: 100−2−5=93 → trailing: (−2)×(−5)=10 → 9310", 7)
            heading(m1_intro, "Quick Application", 1, 8)
            paragrah(m1_intro, "-Software engineering: basis for fast multiplication algorithms (Karatsuba-style decomposition).\n- Financial modeling: quick estimates when prices cluster near round figures (e.g., ~$100 items).\n- Everyday estimation: shopping/retail quick math near round price points.", 9)
            m1_intro.grid(column=1, row=0, sticky="nswe")    
            math_sc_1.grid(sticky="nswe",row=0,column=0)
