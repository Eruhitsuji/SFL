import SFL

rs="""(
    (
        def,
        (
            f,
            (a,b,c),
            (
                add,
                (
                    (
                        add,
                        (a,b)
                    ),
                    c
                )
            )
        )
    ),
    (
        f,
        (
            (int,1),
            (int,2),
            (int,3)
        )
    ),

    (
        f,
        (
            (
                f,
                (    
                    (int,1),
                    (int,2),
                    (int,3)
                ),
            ),
            (int,4),
            (int,5)
        )
    ),

    
    (
        nand,
        (
            (int,2),
            (int,3)
        )
    ),

    
    (
        if,
        (
            (int,0),
            (int,100),
            (int,200)
        )
    ),

    
    (
        def,
        (
            g,
            (a,b),
            (
                (
                    add,
                    (a,b)
                ),
                (
                    add,
                    (
                        a,
                        (int,1)
                    )
                ),
                (
                    add,
                    (
                        b,
                        (int,1)
                    )
                )
            )
        )
    ),
    (
        g,
        (
            (int,2),
            (int,3)
        )
    ),

    
    (
        setvar,
        x,
        (int,2)
    ),
    (getvar,x),
    (
        setvar,
        x,
        (
            add,
            (
                (getvar,x),
                (int,2)
            )
        )
    ),
    (getvar,x),
    
    (
        setvar,
        l,
        (list,((int,0),(int,1)))
    ),
    (getvar,l),
    (
        setvar,
        l,
        (
            extend,
            (
                (getvar,l),
                (list,((int,2),(int,3)))
            )
        )
    ),
    (getvar,l),
    (
        setvar,
        l,
        (
            append,
            (
                (getvar,l),
                (int,4)
            )
        )
    ),
    (getvar,l),
    (
        getlist,
        (
            (getvar,l),
            (int,0)
        )
    ),
    (getvar,l),
    (
        setvar,
        l1,
        (
            setlist,
            (
                (getvar,l),
                (int,0),
                (int,10)
            )
        )
    ),
    (getvar,l),
    (getvar,l1),
    (
        setvar,
        l1,
        (
            setlist,
            (
                (getvar,l1),
                (int,0),
                (list,((list,((int,100),(int,101))),(int,11)))
            )
        )
    ),
    (getvar,l1),
    (
        setvar,
        l2,
        (
            list,
            (
                (int,65),
                (int,66),
                (
                    list,
                    (
                        (int,67),
                        (
                            list,
                            (
                                (int,68),
                                (int,69),
                            )
                        ),
                        (
                            list,
                            (
                                (int,70),
                                (int,71),
                                (int,72),
                            )
                        )
                    )
                )
            )
        )
    ),
    (getvar,l2),
    (
        print,
        (
            (getvar,x),
            (getvar,l1),
            (getvar,l2)
        )
    ),
    (prints,((int,10),(getvar,l2))),
    
)
"""
cp=SFL.CodeProcess(rs)
#print(cp.getStack())
#print(cp.getFuncList())
#print(cp.getVarList())
#print(cp.getResultStr())
