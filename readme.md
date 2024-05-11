# SFL

[SFL.py](SFL.py)をimportして使用してください．
サンプルコードは[sample](sample)です．

また，スクリプトファイルからの実行方法は次のとおりです．

```bash
python SFL.py script_path1 script_path2 ...
```

## 文法

### 関数定義

```SFL
(
    def,
    (
        関数名,
        引数,
        処理内容（戻り値）
    )
)
```

- 戻り値>None

#### "f(a,b)=a+b"の例

```SFL
(
    def,
    (
        f,
        (a,b),
        (
            add,
            (
                a,
                b
            )
        )
    )
)
```

### 関数呼び出し

```SFL
(
    関数名,
    引数
)
```

- 戻り値>関数の戻り値

#### "f(2,3)"の例

```SFL
(
    f,
    (
        (int,2),
        (int,3)
    )
)
```

### 変数定義

```SFL
(
    setvar,
    変数名,
    代入する値
)
```

- 戻り値>None

#### x=10の例

```SFL
(
    setvar,
    x,
    (int,10)
)
```

### 変数呼び出し

```SFL
(
    getvar,
    変数名
)
```

- 戻り値>変数の値

#### xの呼び出し

```SFL
(
    getvar,
    x
)
```

### if文

```SFL
(
    if,
    (
        条件文,
        True時の処理内容,
        False時の処理内容
    )
)
```

- 戻り値>True/False時の処理した結果
- 補足>ifの条件文はint型が0より大きい場合にTrueとなる．

#### "1>0ならば100を，そうでなければ200を出力する"例

```SFL
(
    if,
    (
        (int,1),
        (int,100),
        (int,200)
    )
)
```

### 標準出力

```SFL
(print,(data1,data2,...))
```

- 戻り値>None

#### int型65を表示する

```SFL
(print,((int,65)))
```

#### list型(65,66)を表示する

```SFL
(print,((list,(65,66))))
```

### 文字列に変換して標準出力

```SFL
(prints,(data1,data2,...))
```

- 戻り値>None

#### 'A'を表示する

```SFL
(prints,((int,65)))
```

#### "AB"を表示する

```SFL
(prints,((list,(65,66))))
```

### 標準入力

```SFL
(input)
```

- 戻り値>int型の入力された値

### int型の定義

```SFL
(int,数値)
```

- 戻り値>int型の値

#### int型で2を定義する

```SFL
(int,2)
```

### int型の加算

```SFL
(
    add,
    (
        i1,
        i2
    )
)
```

- 戻り値>加算した結果

#### 4+3の例

```SFL
(
    add,
    (
        (int,4),
        (int,3)
    )
)
```

### int型のNAND演算

```SFL
(
    nand,
    (
        i1,
        i2
    )
)
```

- 戻り値>NAND演算した結果

#### 4と3のNAND演算の例

```SFL
(
    nand,
    (
        (int,4),
        (int,3)
    )
)
```

### list型の定義

```SFL
(list,(data1,data2,...))
```

- 戻り値>list型のデータ

#### list型で(0,1,2)を定義する

```SFL
(list,(0,1,2))
```

### list型の結合

```SFL
(extend,(list1,list2))
```

- 戻り値>結合後のlist型のデータ
- 補足>元のlist型のデータには結合されない

#### list型(0,1,2)とlist型(3,4,5)を結合する

```SFL
(
    extend,
    (
        (list,(0,1,2)),
        (list,(3,4,5))
    )
)
```

### list型の末尾にデータ追加

```SFL
(append,(list,data))
```

- 戻り値>データ追加後のlist型のデータ
- 補足>元のlist型のデータには追加されない

#### list型(0,1,2)にint型3を追加する

```SFL
(
    append,
    (
        (list,(0,1,2)),
        (int,3)
    )
)
```

### list内の要素取得

```SFL
(getlist,(list,index))
```

- 戻り値>要素の値

#### list型(0,1,2)の0番目要素を取得する

```SFL
(
    getlist,
    (
        (list,(0,1,2)),
        (int,0)
    )
)
```

### list内の要素上書き

```SFL
(setlist,(list,index,data))
```

- 戻り値>上書き後のlist型のデータ
- 補足>元のlist型のデータには上書きされない

#### list型(0,1,2)の0番目要素をint型10に変更する

```SFL
(
    setlist,
    (
        (list,(0,1,2)),
        (int,0),
        (int,10)
    )
)
```
