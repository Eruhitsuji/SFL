import SFL

rs="""(
    (
        def,
        (
            mult,
            (a,b),
            (
                if,
                (
                    (
                        add,
                        (
                            b,
                            (int,-1)
                        )
                    ),
                    (
                        add,
                        (
                            a,
                            (
                                mult,
                                (
                                    a,
                                    (
                                        add,
                                        (
                                            b,
                                            (int,-1)
                                        )
                                    )
                                )
                            )
                        )
                    ),
                    a
                )
            )
        )
    ),
    (
        print,
        (
            (
                mult,
                (
                    (int,2),
                    (int,3)
                )
            ),
            (
                mult,
                (
                    (int,-2),
                    (int,3)
                )
            ),
            (
                mult,
                (
                    (
                        mult,
                        (
                            (int,2),
                            (int,3)
                        )
                    ),
                    (int,10)
                )
            )
        )
    )
)"""
cp=SFL.CodeProcess(rs)
#print(cp.getStack())
#print(cp.getFuncList())
#print(cp.getVarList())
#print(cp.getResultStr())
