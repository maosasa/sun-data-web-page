# プログラムの内容
ビットコインの例を参考にし、日付に対しての黒点の数（換算値）をプロットするプログラムを作った。

## データ取得元
国立天文台 太陽観測科学プロジェクト 三鷹太陽地上観測
黒点相対数

https://solarwww.mtk.nao.ac.jp/jp/db_sunspot.html

## データの詳細
日付ベースのRの値を使用した。

R: the sunspot relative numbers 

R = k(10g + f) 

f: the number of sunspots 

g: the number of groups 

>Values of k-factor:
>     year                k
>--------------------------------
>     1929                0.85
>     1930                0.75
>     1931-1934           0.65
>     1935                0.70
>     1936                0.55
>     1937-1945 Mar       0.6
>     1945 Apr-1950       0.7
>     1951-1959           0.65
>     1960-1985           0.72
>     1986-1998 May       0.6
>     1998 June-present   1.0

[数値について](https://solarwww.mtk.nao.ac.jp/mitaka_solar1/data03/sunspots/number/Readme.txt)

# 工夫したところ
365日×80年分の大量のデータを処理する上で、元のデータを手作業で編集せず、自動で処理を行えるように工夫した。
ただ結局のところ何点かの例外の処理に困り、その部分だけ手で編集した。

演習を真似て、日付のボックスに対してchangeとkeyupの両方をトリガーにしてグラフの書き換えを行うようにした。

# 苦労した点
データがカンマ、タブ区切りでなく、スペースで列を揃えているだけで、データの無い部分も空白になっていたので、csvとして扱えず苦労した。txtファイルとして読み込んで、列ごとにスペース区切りでリストを作り右端のデータを取ることで、うまく扱ったが、使用するデータが右端にない場合はどうやっていいかわからないままだった。

そもそも１つのファイルに12ヶ月分のデータが入っていて、各月の間に月名やMonthly Meanの記述が挟まっているため、ファイル全体で一つの表になっていないものを、うまく切り分けるのが難しかった。初めのn行を削除したり、MonthlyMeanにぶつかるまでデータ取得することにしたりして対応したが、想定外の場所にスペースが紛れ込んでいたりして例外処理に苦労した。

欠損データの処理も難しかった。初めは0にしていたが、それだとグラフから読み取れる内容が大きく変わってしまうので、欠損部分の前後の点を直接つなぐようにした。

なぜか2月30日などの存在しない日付のデータが含まれていて困った。今回は無視することにした。

また、1929年ごろの計測方法は1日1回だったのに対し、80年間の間に約20時間に一回程度に変わっていて、同じ日付でデータが2つあるものが出てきて処理に困った。これは手で直接元のデータから余計なものを削除した。
 

# やり足りなかったこと
ほとんど先生のサンプルのまま、書き換えただけになってしまったが、もう少し自分で思い描いたWebサービスを形にできるようになりたかった。

HTMLももっと工夫して、綺麗なデザインのものをシンプルでいいので作りたかった。

# コメント
太陽の活動は11年周期だという話を聞いたことがあって、可視化して見てみたくて、黒点数のデータを扱った。しかし、11年周期ですねとわかっていたことが確認できただけだったので、苦労して可視化した割には味気なかった。地球の気候データと絡めてみたら面白かったかもしれないが、技術不足で断念した。