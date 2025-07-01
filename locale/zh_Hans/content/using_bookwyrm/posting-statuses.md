- - -
Title: Posting Statuses Date: 2025-05-26 Order: 4
- - -

在BookWyrm上发帖，要从一本书开始。 用户可以从“你的书”部分，或从一本书的登陆页面，对正在进行的或最近阅读的书籍进行评论。 从那里，用户可以对评论回复并开始对话。 BookWyrm帖子可以包括一些格式，如使用[Markdown](https://www.markdownguide.org/cheat-sheet/)的粗体、斜体和链接。

如果你熟悉[在Mastodon上发帖](https://docs.joinmastodon.org/user/posting/)，你会发现BookWyrm的状态有类似的可见性设置、内容警告和提醒。 然而，目前还暂不支持投票、自定义表情符号和附件。

## 状态类型

### 用户评论

用户可以直接对对应的书籍创建三种类型的帖子：观后感、评论和引言。 评论是针对一本书的一般方面，引言是针对具体的段落，而观后感则是针对书籍的整体。 用户还可以对状态进行回复。

| 组成部分 | 观后感 | 评论 | 引言 | 回复 |
| ---- | --- | -- | -- | -- |
| 文本字段 | ✔   | ✔  | ✔  | ✔  |
| 剧透警告 | ✔   | ✔  | ✔  | ✔  |
| 页码   |     | ✔  | ✔  |    |
| 引用   |     |    | ✔  |    |
| 评分   | ✔   |    |    |    |
| 标题字段 | ✔   |    |    |    |

#### Spoiler alerts

Spoiler alerts (also known as content warnings) are useful to give people a warning before they read a status that might spoil the plot of a book they want to read. Usually just putting "contains spoilers" or something similar is sufficient, but you can be more specific, especially if your status discusses potentially sensitive topics.

#### Star ratings

A star rating can be added to reviews, or added on its own by clicking the stars below a book. It is a 5-star scale, and half stars can be added by double clicking on the star. For example, if you want to rate 2.5 stars, you'd click on 3 stars then click again on the third star to make it half. When viewing a book or reviews, the star ratings are hidden until the user selects "Show rating".

### 阅读状态更新

当用户表示他们想要阅读、已经开始阅读或已经完成阅读一本书时，就会有对应的状态。

## 文本
文本可以包括：

- 提及用户（@user）
- URLs（`http(s)://` 不会显示）
- 一些 [Markdown 格式](https://www.markdownguide.org/cheat-sheet/)
    - 粗体
    - 斜体
    - 引用块
    - 符号列表
    - 链接

