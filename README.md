# 使用

查询模式：

```
python search.py <word-you-want-to-search>
```

听写模式：

```
./word.sh
```

之后进入读取模式，输入单词，即开始查询、输出单词解释、播放伦敦腔读音。适合给娃听写。

**注意**，此时按下回车，继续上一个单词。

# 说明

`.dict/`下是缓存文件，保存查询过的单词解释和读音。比如：

```
ls -R .dict
bad

.dict/bad:
audio.mp3	content.txt
```