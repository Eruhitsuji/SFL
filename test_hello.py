import SFL

rs="""(
    prints,
    (
        (
            list,
            (
                (int,72),
                (int,101),
                (int,108),
                (int,108),
                (int,111),
                
                (int,44),
                (int,32),

                (int,119),
                (int,111),
                (int,114),
                (int,108),
                (int,100),

                (int,33),
                (int,10)
            )
        )    
    )
)"""
cp=SFL.CodeProcess(rs)
#print(cp.getStack())
#print(cp.getFuncList())
#print(cp.getVarList())
#print(cp.getResultStr())
