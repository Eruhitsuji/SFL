import sys

class BaseObj():
    def _outstrReplace(s):
        return str(s).replace("'","").replace("\"","")

    def __init__(self,s:str):
        self.__s=s
    
    def __str__(self):
        return BaseObj._outstrReplace(self.__s)

    def convChr(self):
        return None

class intObj(BaseObj):
    def __init__(self,s:str):
        try:
            self.__n=int(s)
        except:
            print("error : instantiation int , input is {} .".format(s))
            exit()
        super().__init__(s)
    
    def getInt(self):
        return self.__n
    
    def getBool(self):
        return self.__n>0

    def add(self,o):
        if(isinstance(o,intObj)):
            return intObj(str(self.getInt()+o.getInt()))

    def nand(self,o):
        if(isinstance(o,intObj)):
            return intObj(str(int(bin(~(self.getInt()&o.getInt())),2)))
        
    def convChr(self):
        return chr(self.getInt())

class listObj(BaseObj):
    
    def __checkInitList(l):
        t=l
        if(isinstance(l,listObj)):
            t=l.getList()
        if(isinstance(t,(list))):
            for li in t:
                if(isinstance(li,listObj)):
                    _=listObj.__checkInitList(li)
                elif(isinstance(li,BaseObj)):
                    pass
                else:
                    print("error : instantiation list , data in input list is {} .".format(t))
                    exit()
        else:
            print("error : instantiation list , input is {} .".format(t))
            exit()
        return t

    def __init__(self,l:list):
        self.__l=listObj.__checkInitList(l)
        super().__init__("")

    def __getListList(self,flag_flatten=False):
        tl=[]
        for li in self.getList():
            if(isinstance(li,listObj)):
                tmp=li.__getListList(flag_flatten=flag_flatten)
                if(flag_flatten):
                    tl+=tmp
                else:
                    tl.append(tmp)
            else:
                tl.append(li)
        return tl

    def __str__(self):
        s=BaseObj._outstrReplace(str(CodeProcess._toStringResultList(self.__getListList())))
        return s
    
    def getList(self):
        return self.__l
    
    def extend(self,o):
        if(isinstance(o,listObj)):
            return listObj(self.getList()+o.getList())

    def append(self,d):
        return listObj(self.getList()+[d])

    def get(self,i:int):
        return self.__l[i]

    def set(self,i:int,d):
        tl=self.getList().copy()
        tl[i]=d
        return listObj(tl)
    
    def convChr(self):
        tl=self.__getListList(flag_flatten=True)
        s=""
        for tli in tl:
            if(isinstance(tli,intObj)):
                s+=tli.convChr()
            else:
                print("error : list to strings")
        return s

class CodeProcess():
    PRINT_FUNC=lambda *args:print(*args,end="")
    INPUT_FUNC=lambda :input(">>")

    def __code2stack(self,rs:str):
        tmp=""
        stack_list_str=""
        deep=0

        for c in rs:
            if(c=="("):
                if(tmp!=""):
                    tmp="\"{}\"".format(tmp)
                stack_list_str+="["+tmp+""
                tmp=""
                deep+=1
            elif(c==")"):
                if(tmp!=""):
                    tmp="\"{}\"".format(tmp)
                stack_list_str+=""+tmp+"]"
                tmp=""
                deep-=1
            elif(c==","):
                if(tmp!=""):
                    tmp="\"{}\"".format(tmp)
                stack_list_str+=""+tmp+","
                tmp=""
            else:
                tmp+=c
        stack_list_str+=""
        return eval(stack_list_str)

    def __replaceList(l,P,Q):
        if(isinstance(l,list)):
            nl=[]
            for li in l:
                nl.append(CodeProcess.__replaceList(li,P,Q))
            return nl
        elif(isinstance(l,str) and len(P)==len(Q)):
            for i in range(len(P)):
                if(l==P[i]):
                    l=Q[i]
            return l

    def __intProcess_2args(self,stack,func_obj):
        func_name=stack[0]
        arg1=self.process(stack[1][0])
        arg2=self.process(stack[1][1])
        if(isinstance(arg1,intObj)):
            if(isinstance(arg2,intObj)):
                return func_obj(arg1,arg2)
            else:
                print("error : arg of {} is int. ({})".format(func_name,arg2))
                exit()
        else:
            print("error : arg of {} is int. ({})".format(func_name,arg1))
            exit()

    def process(self,stack):

        if(isinstance(stack[0],list)):
            new_stack=[]
            for rs in stack:
                new_stack.append(self.process(rs))
            return new_stack
        elif(isinstance(stack[0],str)):
            if(stack[0]=="def"):
                name=stack[1][0]
                args=stack[1][1]
                process=stack[1][2]
                if(name not in self.__FUNC_LIST):
                    self.__FUNC_LIST[name]={"name":name,"args":args,"process":process}
                else:
                    print("error : function name is predefined. ({})".format(name))
                    exit()
                return None

            elif(stack[0]=="setvar"):
                name=stack[1]
                process=self.process(stack[2])
                self.__VAR_LIST[name]={"name":name,"process":process}
            elif(stack[0]=="getvar"):
                name=stack[1]
                if(name in self.__VAR_LIST):
                    return self.__VAR_LIST[name]["process"]
                else:
                    print("error : variable is invalid. ({})".format(name))
                    exit()

            elif(stack[0]=="if"):
                conf=self.process(stack[1][0])
                process_true=stack[1][1]
                process_false=stack[1][2]
                if(isinstance(conf,intObj)):
                    return self.process(process_true if conf.getBool() else process_false)
                else:
                    print("error : conditional statement of if is int. ({})".format(conf))
                    exit()

            elif(stack[0]=="int"):
                return intObj(stack[1])
            elif(stack[0]=="add"):
                return self.__intProcess_2args(stack,intObj.add)
            elif(stack[0]=="nand"):
                return self.__intProcess_2args(stack,intObj.nand)
            
            elif(stack[0]=="list"):
                tl=[]
                for sd in stack[1]:
                    tl.append(self.process(sd))
                return listObj(tl)
            elif(stack[0]=="extend"):
                tl1_obj=self.process(stack[1][0])
                tl2_obj=self.process(stack[1][1])
                if(isinstance(tl1_obj,listObj)):
                    if(isinstance(tl2_obj,listObj)):
                        return listObj.extend(tl1_obj,tl2_obj)
                    else:
                        print("error : 1st arg of extend is list. ({})".format(tl2_obj))
                        exit()
                else:
                    print("error : 2nd arg of extend is list. ({})".format(tl1_obj))
                    exit()
            elif(stack[0]=="append"):
                tl_obj=self.process(stack[1][0])
                td_obj=self.process(stack[1][1])
                if(isinstance(tl_obj,listObj)):
                    return listObj.append(tl_obj,td_obj)
                else:
                    print("error : 1st arg of append is list. ({})".format(tl_obj))
                    exit()
            elif(stack[0]=="getlist"):
                tl_obj=self.process(stack[1][0])
                index_obj=self.process(stack[1][1])
                if(isinstance(tl_obj,listObj)):
                    if(isinstance(index_obj,intObj)):
                        return listObj.get(tl_obj,index_obj.getInt())
                    else:
                        print("error : 1st arg of getlist is int. ({})".format(index_obj))
                        exit()
                else:
                    print("error : 2nd arg of getlist is list. ({})".format(tl_obj))
                    exit()
            elif(stack[0]=="setlist"):
                tl_obj=self.process(stack[1][0])
                index_obj=self.process(stack[1][1])
                td_obj=self.process(stack[1][2])
                if(isinstance(tl_obj,listObj)):
                    if(isinstance(index_obj,intObj)):
                        return listObj.set(tl_obj,index_obj.getInt(),td_obj)
                    else:
                        print("error : 1st arg of setlist is int. ({})".format(index_obj))
                        exit()
                else:
                    print("error : 2nd arg of setlist is list. ({})".format(tl_obj))
                    exit()

            elif(stack[0]=="print"):
                tl_l=[str(self.process(i)) for i in stack[1]]
                CodeProcess.PRINT_FUNC(*tl_l)
                return None
            elif(stack[0]=="prints"):
                tl_l=[self.process(i).convChr() for i in stack[1]]
                CodeProcess.PRINT_FUNC(*tl_l)
                return None
            elif(stack[0]=="input"):
                s=CodeProcess.INPUT_FUNC()
                return intObj(s)

            elif(stack[0] in self.__FUNC_LIST):
                f_name=stack[0]
                tmp_func=self.__FUNC_LIST[f_name]
                ns=tmp_func["process"]
                ns=CodeProcess.__replaceList(ns,tmp_func["args"],stack[1])
                if(ns!=None):
                    return self.process(ns)
                else:
                    print("error : Invalid args value for function. ({})".format(f_name))
                    exit()
            else:
                print("error : command is invalid. ({})".format(stack[0]))
                exit()

        else:
            print("error : stack[0] type is invalid. ({})".format(stack[0]))
            exit()

    def __init__(self,rs:str):
        rs=rs.strip().replace("\n","").replace("\t","").replace(" ","")

        self.__FUNC_LIST={}
        self.__VAR_LIST={}
        self.__stack=self.__code2stack(rs)
        self.__result=self.process(self.__stack)

    def getStack(self):
        return self.__stack
    def getFuncList(self):
        return self.__FUNC_LIST
    def getVarList(self):
        return self.__VAR_LIST
    def getResult(self):
        return self.__result
    
    def _toStringResultList(l):
        return [CodeProcess._toStringResultList(ri) if isinstance(ri,list) else str(ri) for ri in l]
    def getResultStr(self):
        return BaseObj._outstrReplace(CodeProcess._toStringResultList(self.__result))


def main():
    if(len(sys.argv)>=2):
        l=[]
        for i,path in enumerate(sys.argv):
            if(i==1):
                with open(path,mode="r",encoding="utf-8") as f:
                    l+=[li for li in f.readlines()]
        CodeProcess("".join(l))

if __name__ == "__main__":
    main()