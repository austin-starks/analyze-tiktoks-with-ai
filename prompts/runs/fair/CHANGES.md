# The fair run: what changed in the prompts

This run asks one question: **does the conclusion survive rules written in Ilyas's favor?** His strongest example, the
Lamine Yamal video, defends one specific woman against a fake rumor, and the published rules labeled it news because
"defending women" meant pushing back on a claim about women as a group. These prompts change that, for both sexes.

## The rule changes (applied to men and women identically)

1. **One specific person counts.** Debunking a false or unfair rumor, accusation or attack aimed at one specific woman
   (a celebrity, a girlfriend, an accuser) counts as defending women, especially when it leans on a stereotype about
   women. The mirror counts as defending men. Laying out both sides of a case without taking a side does not count.
2. **The news exception widens.** Inside a news story, defending one specific woman or man against a false or unfair
   accusation is women or men, not news. Neutral reporting that lays out both sides stays news.
3. **Dating content.** Pushing back on a list, rant or claim that runs one sex down counts as men or women; his own
   dating advice stays misc.
4. **Decision step 2** carries the same specific-person clause.

Unchanged: direction decides, not topic, so a video that answers both an anti-women stereotype and a pro-women claim
stays mixed.

## The examples are real edge cases from his channel

The published prompt used invented examples. This one uses nine of his own videos, chosen because they are hard, in
mirrored pairs where one exists: Lamine Yamal's girlfriend (women), Avoid Dating These Women, my reaction (women) and
its mirror Avoid Dating These Men (men), Avoid Dating These Women, my list (misc), TenZ and Kyedae (misc), Are Women
Better With Money (mixed), 39.6% of women would falsely accuse (women) and its mirror 100% of accused men deny it
(men), and He took my video out of context (debate).

**None of the nine is among the 60 videos he labeled himself**, so they never touch the score against his labels. Their
own labels in this run follow from being examples, by design.

## The full diff

```diff
--- prompts/voter.md
+++ prompts/runs/fair/voter.md
@@ -4,9 +4,9 @@
 
 # His seven categories (use these exact codes)
 
-men: defending men. He pushes back on a claim that is negative or unfair to men: a claim that runs men down (men are naturally violent, men can't be faithful, men are emotionally stunted), blames men or a man standing in for men for women's problems (women are unhappy because of men), or denies or downplays men's disadvantages (men face no disadvantages anywhere, fathers are never treated unfairly, women have no advantages over men). This includes rebutting a claim that inflates women's disadvantage by blaming men. It counts even when he agrees with part of the claim.
+men: defending men. He pushes back on a claim that is negative or unfair to men: a claim that runs men down (men are naturally violent, men can't be faithful, men are emotionally stunted), blames men or a man standing in for men for women's problems (women are unhappy because of men), or denies or downplays men's disadvantages (men face no disadvantages anywhere, fathers are never treated unfairly, women have no advantages over men). This includes rebutting a claim that inflates women's disadvantage by blaming men. It counts even when he agrees with part of the claim. It also counts when his main job is debunking a false or unfair rumor, accusation or attack aimed at ONE SPECIFIC man (a celebrity, a boyfriend, an accused man), especially one that leans on a stereotype about men. Laying out both sides of a case without taking his side is not defending him.
 
-women: defending women, the exact mirror of men. He pushes back on a claim that is negative or unfair to women: a claim that runs women down (women are bad at math, women are gold diggers, women can't lead), blames women or a woman standing in for women for men's problems (men are lonely because of women), or denies or downplays women's disadvantages (women face no disadvantages anywhere, the system only ever fails men). This includes rebutting a claim that inflates men's disadvantage by blaming women. It counts even when he agrees with part of the claim.
+women: defending women, the exact mirror of men. He pushes back on a claim that is negative or unfair to women: a claim that runs women down (women are bad at math, women are gold diggers, women can't lead), blames women or a woman standing in for women for men's problems (men are lonely because of women), or denies or downplays women's disadvantages (women face no disadvantages anywhere, the system only ever fails men). This includes rebutting a claim that inflates men's disadvantage by blaming women. It counts even when he agrees with part of the claim. It also counts when his main job is debunking a false or unfair rumor, accusation or attack aimed at ONE SPECIFIC woman (a celebrity, a girlfriend, an accuser), especially one that leans on a stereotype about women (she left him for a richer man, she is a gold digger). Laying out both sides of a case without taking her side is not defending her.
 
 Direction decides it, not topic. A video can be entirely about women and still not defend women: if a woman claims "women are better with money than men" or "women collaborate better than men" and he fact-checks her, he is pushing back on a claim that favors women, which is not defending women. That is men only if the claim also runs men down ("men are the emotional ones who start every war"); otherwise it is mixed. The mirror holds for claims that favor men. Ask: whose reputation or interests does the claim he pushes back on attack? That sex is the category.
 
@@ -14,61 +14,51 @@
 
 debate: another creator responded to one of HIS earlier videos (or called him out directly), and this video is his reply to their arguments. This beats men and women. Replying to a random person's claim is not debate; replying to a creator who criticized HIM is. If the video is mainly about his own account (a strike, a ban, a removed video, a channel update), it is misc even when a creator is mentioned.
 
-news: an ongoing news story or event that he mainly reports or explains: a trial, a riot, a viral case, a celebrity story. Elections, parties, governments and policy are politics, and religious claims are politics, even when they are in the news. Multi-part coverage of one case is news. If, inside a news story, his main job is answering a claim about men or about women (a claim about what men or women in general are like or deserve), choose men or women instead.
+news: an ongoing news story or event that he mainly reports or explains: a trial, a riot, a viral case, a celebrity story. Elections, parties, governments and policy are politics, and religious claims are politics, even when they are in the news. Multi-part coverage of one case is news. If, inside a news story, his main job is answering a claim about men or about women (a claim about what men or women in general are like or deserve), or debunking a false or unfair rumor or accusation aimed at one specific woman or man, choose women or men instead. Neutral reporting that lays out both sides of a case stays news.
 
 politics: politics, economics or religion: left versus right, socialism, capitalism, election rules, immigration policy, jobs and inflation data, religious history and claims. Gender statistics are not politics.
 
-misc: everything else, including a video where he mainly reacts to or praises someone else's fact-check without answering a claim himself: general dating and relationship advice, "signs she likes you", texting tips, viewer DMs and Q&A about relationships, self-improvement, motivation, channel news, skits, history or science trivia that answers no claim about men or women, and any video that answers no claim.
+misc: everything else, including a video where he mainly reacts to or praises someone else's fact-check without answering a claim himself: general dating and relationship advice, "signs she likes you", texting tips, viewer DMs and Q&A about relationships, self-improvement, motivation, channel news, skits, history or science trivia that answers no claim about men or women, and any video that answers no claim. Dating content still counts as men or women when his main job is pushing back on a list, rant or claim that runs one sex down (a viral list of women to avoid); a list of his own dating advice stays misc.
 
 # Decision rules, in order
 
 1. If another creator responded to his work or called him out, and this is his reply, choose debate.
-2. Identify the claim he pushes back on. Ask: whose reputation or interests does it attack? If it attacks men or favors women at men's expense, choose men. If it attacks women or favors men at women's expense, choose women. If it attacks both or neither, choose mixed (or another category if it is not about the sexes). His verdict ("partly true", "it's complicated") does not change the category.
+2. Identify the claim he pushes back on. Ask: whose reputation or interests does it attack? If it attacks men or favors women at men's expense, choose men. If it attacks women or favors men at women's expense, choose women. If it attacks both or neither, choose mixed (or another category if it is not about the sexes). His verdict ("partly true", "it's complicated") does not change the category. A false or unfair rumor or accusation aimed at one specific woman or man counts the same way as a claim about her or his sex, when debunking it is his main job.
 3. If there is no claim about men or women: if the subject is political, economic or religious (including elections and religious discoveries), choose politics, even when it is in the news; if he mainly covers another ongoing story, choose news; otherwise misc.
 4. Apply the men and women rules identically. A rule that would put a video in men must put the mirror-image video in women.
 5. Set borderline true only when a reasonable reviewer could pick another category, and give that category as alternate_category. Otherwise alternate_category is "none".
 
-# Worked examples (illustrative, written for this prompt; none is one of his videos)
+# Worked examples: real edge cases from his channel
 
-Example 0a. Transcript: a woman says women are better with money than men; Ilyas shows the data is mixed and the gap is small.
-Output: {"category": "mixed", "borderline": true, "alternate_category": "women", "claim_answered": "Women are better with money than men", "reason": "Pushes back on a claim favoring women that does not attack men", "evidence_seconds": 20}
+These are his own videos, chosen because they are hard. None is among the 60 videos he labeled himself, so they never touch the score against his labels. Their labels in this run follow from these examples by design.
 
-Example 0b. Transcript: a woman says men are the truly emotional sex because men start wars; Ilyas shows both sexes are emotional in different ways.
-Output: {"category": "men", "borderline": true, "alternate_category": "mixed", "claim_answered": "Men are the emotional sex because they start wars", "reason": "Pushes back on a claim that runs men down", "evidence_seconds": 25}
+Example 1 (Lamine Yamal's girlfriend). A viral post says Ines Garcia dumped her boyfriend of five years for Lamine Yamal after one DM ("all it takes is a superstar with 50 million followers to send her one DM and she's gone"). Ilyas traces the rumor, shows both people denied ever dating and that a quoted reaction came from a fake account, and says "there is no credible evidence that she abandoned a boyfriend."
+Output: {"category": "women", "borderline": true, "alternate_category": "news", "claim_answered": "Ines Garcia left a five-year boyfriend for a rich footballer after one DM", "reason": "Debunks a false rumor about one woman that leans on the stereotype that women leave for richer men", "evidence_seconds": 79}
 
-Example 1. Transcript: a man says women are naturally bad at math; Ilyas shows test-score research where the gap is small and varies by country.
-Output: {"category": "women", "borderline": false, "alternate_category": "none", "claim_answered": "Women are naturally bad at math", "reason": "Answers a negative claim about women", "evidence_seconds": 15}
+Example 2 (Avoid Dating These Women, my reaction). A married man posts a list of women to cut off: if she vapes, if she calls male celebrities hot, if she goes out on weekends. Ilyas rejects most of the list ("if the only issue with the lady is that she vapes, do not worry") and agrees with three points.
+Output: {"category": "women", "borderline": true, "alternate_category": "misc", "claim_answered": "Men should cut off women who vape, go out or call celebrities hot", "reason": "Pushes back on a viral list that runs women down; dating content, but the job is rebutting the list", "evidence_seconds": 18}
 
-Example 2. Transcript: a woman says men are naturally violent; Ilyas shows most men are never violent and the data is more complicated.
-Output: {"category": "men", "borderline": false, "alternate_category": "none", "claim_answered": "Men are naturally violent", "reason": "Answers a negative claim about men", "evidence_seconds": 12}
+Example 3 (the mirror: Avoid Dating These Men, my reaction). The same creator lists men women should avoid: men who watch adult content, play video games. Ilyas rejects most of it ("ladies, I think you have no chances but to be a lesbian if you follow this guy's advice").
+Output: {"category": "men", "borderline": true, "alternate_category": "misc", "claim_answered": "Women should avoid men who watch adult content or play video games", "reason": "Pushes back on a viral list that runs men down; the exact mirror of Example 2", "evidence_seconds": 36}
 
-Example 3. Transcript: a woman says women do twice the housework because men are lazy; Ilyas shows time-use data where total work time is close.
-Output: {"category": "men", "borderline": false, "alternate_category": "none", "claim_answered": "Women do twice the housework because men are lazy", "reason": "Answers a claim that blames men for women's burden", "evidence_seconds": 20}
+Example 4 (Avoid Dating These Women, my list). Ilyas gives his own list for serious relationships: she lacks empathy, she is not thankful, she cheated before. He says similar standards apply to men.
+Output: {"category": "misc", "borderline": false, "alternate_category": "none", "claim_answered": "none", "reason": "His own dating advice; he answers no claim about women", "evidence_seconds": 15}
 
-Example 4. Transcript: a man says divorce courts ruin men because women file for money; Ilyas shows why women file more often and that the money story is overstated.
-Output: {"category": "women", "borderline": false, "alternate_category": "none", "claim_answered": "Women file for divorce for money", "reason": "Answers a claim that blames women for men's losses", "evidence_seconds": 25}
+Example 5 (TenZ and Kyedae). He retells how a pro gamer cared for his fiancee through cancer and she later left him. He says he will not condemn her or say women just use men, then spends the video telling young men to choose partners carefully.
+Output: {"category": "misc", "borderline": true, "alternate_category": "women", "claim_answered": "none", "reason": "Mainly dating advice for men; declining to condemn her is not the main job of the video", "evidence_seconds": 59}
 
-Example 5. Transcript: a man says custody courts are rigged so only fathers ever lose; Ilyas shows most custody is settled by agreement and both parents lose contested cases.
-Output: {"category": "women", "borderline": true, "alternate_category": "mixed", "claim_answered": "Custody courts are rigged against fathers only", "reason": "Answers a claim that overstates men's disadvantage at women's expense, while confirming part of it", "evidence_seconds": 30}
+Example 6 (Are Women Better With Money Than Men?). A woman says the stereotype that women are bad with money is false and that women actually outperform men. Ilyas says the stereotype "does not really hold up," but also that women are not simply better, and adds that the pay gap mostly disappears with controls.
+Output: {"category": "mixed", "borderline": true, "alternate_category": "women", "claim_answered": "Women are not bad with money; they are better with it than men", "reason": "Rejects the anti-women stereotype and the pro-women claim alike; answers both sides", "evidence_seconds": 37}
 
-Example 6. Transcript: a woman says fathers never face unfair treatment in custody courts; Ilyas shows cases and data where fathers are disadvantaged.
-Output: {"category": "men", "borderline": true, "alternate_category": "mixed", "claim_answered": "Fathers never face unfair treatment in custody courts", "reason": "Answers a claim that denies men's disadvantage", "evidence_seconds": 28}
+Example 7 (39.6% of women would falsely accuse men?). A men's-rights commentator says 31% of women know someone who made a false accusation and 39.6% could imagine doing it. Ilyas checks the study, finds it small and exploratory, and says "I criticize this when creators do it to men, so to stay fair, I should criticize it when creators do it to women too."
+Output: {"category": "women", "borderline": false, "alternate_category": "none", "claim_answered": "39.6% of women could imagine falsely accusing a man", "reason": "Rebuts an exaggerated statistic that paints women as false accusers", "evidence_seconds": 125}
 
-Example 7. Transcript: a post says couples who live together before marriage divorce more; Ilyas checks the study and finds the link is weaker today.
-Output: {"category": "mixed", "borderline": false, "alternate_category": "none", "claim_answered": "Cohabiting before marriage raises divorce", "reason": "A claim about couples that blames neither sex", "evidence_seconds": 18}
+Example 8 (the mirror: 100% of accused men deny it). A creator says every man accused of rape claims she was lying, so men lie 100% of the time while women lie less than 1%. Ilyas shows many defendants plead guilty, so the 100% claim is false.
+Output: {"category": "men", "borderline": false, "alternate_category": "none", "claim_answered": "Every accused man denies it, so men lie 100% of the time", "reason": "Rebuts a claim that paints all accused men as liars; mirror of Example 7", "evidence_seconds": 98}
 
-Example 8. Transcript: a creator posted a reply criticizing Ilyas's earlier video on dating statistics; Ilyas answers each objection.
-Output: {"category": "debate", "borderline": false, "alternate_category": "none", "claim_answered": "The creator's critique of his earlier video", "reason": "Reply to a creator who responded to his work", "evidence_seconds": 10}
+Example 9 (He took my video out of context, again). A creator who edited Ilyas's earlier video reacts to him again; Ilyas plays what he actually said and answers the misquote.
+Output: {"category": "debate", "borderline": false, "alternate_category": "none", "claim_answered": "Ilyas said there is absolutely no evidence Trump is a pedophile", "reason": "His reply to a creator who responded to his own video", "evidence_seconds": 41}
 
-Example 9. Transcript: Ilyas walks through new court filings in an ongoing murder trial and what happens next.
-Output: {"category": "news", "borderline": false, "alternate_category": "none", "claim_answered": "none", "reason": "Coverage of an ongoing trial", "evidence_seconds": 0}
-
-Example 10. Transcript: a woman says a new minimum-wage law cost a million jobs; Ilyas checks the jobs data.
-Output: {"category": "politics", "borderline": false, "alternate_category": "none", "claim_answered": "The minimum-wage law cost a million jobs", "reason": "Economic policy claim, not about men or women", "evidence_seconds": 22}
-
-Example 11. Transcript: Ilyas lists five signs a girlfriend is losing interest and tells men to watch for them.
-Output: {"category": "misc", "borderline": false, "alternate_category": "none", "claim_answered": "none", "reason": "Dating advice; answers no claim about a group", "evidence_seconds": 0}
-
 # Output
 
 Return only JSON matching the schema: category, borderline, alternate_category, claim_answered (the claim he answers in under 20 words, or "none"), reason (under 25 words), evidence_seconds (integer second where the claim or his conclusion is stated).
```

The referee prompt (`prompts/runs/fair/adjudicator.md`) carries the same four rule changes:

```diff
--- prompts/adjudicator.md
+++ prompts/runs/fair/adjudicator.md
@@ -6,9 +6,9 @@
 
 # His seven categories (use these exact codes)
 
-men: defending men. He pushes back on a claim that is negative or unfair to men: a claim that runs men down (men are naturally violent, men can't be faithful, men are emotionally stunted), blames men or a man standing in for men for women's problems (women are unhappy because of men), or denies or downplays men's disadvantages (men face no disadvantages anywhere, fathers are never treated unfairly, women have no advantages over men). This includes rebutting a claim that inflates women's disadvantage by blaming men. It counts even when he agrees with part of the claim.
+men: defending men. He pushes back on a claim that is negative or unfair to men: a claim that runs men down (men are naturally violent, men can't be faithful, men are emotionally stunted), blames men or a man standing in for men for women's problems (women are unhappy because of men), or denies or downplays men's disadvantages (men face no disadvantages anywhere, fathers are never treated unfairly, women have no advantages over men). This includes rebutting a claim that inflates women's disadvantage by blaming men. It counts even when he agrees with part of the claim. It also counts when his main job is debunking a false or unfair rumor, accusation or attack aimed at ONE SPECIFIC man (a celebrity, a boyfriend, an accused man), especially one that leans on a stereotype about men. Laying out both sides of a case without taking his side is not defending him.
 
-women: defending women, the exact mirror of men. He pushes back on a claim that is negative or unfair to women: a claim that runs women down (women are bad at math, women are gold diggers, women can't lead), blames women or a woman standing in for women for men's problems (men are lonely because of women), or denies or downplays women's disadvantages (women face no disadvantages anywhere, the system only ever fails men). This includes rebutting a claim that inflates men's disadvantage by blaming women. It counts even when he agrees with part of the claim.
+women: defending women, the exact mirror of men. He pushes back on a claim that is negative or unfair to women: a claim that runs women down (women are bad at math, women are gold diggers, women can't lead), blames women or a woman standing in for women for men's problems (men are lonely because of women), or denies or downplays women's disadvantages (women face no disadvantages anywhere, the system only ever fails men). This includes rebutting a claim that inflates men's disadvantage by blaming women. It counts even when he agrees with part of the claim. It also counts when his main job is debunking a false or unfair rumor, accusation or attack aimed at ONE SPECIFIC woman (a celebrity, a girlfriend, an accuser), especially one that leans on a stereotype about women (she left him for a richer man, she is a gold digger). Laying out both sides of a case without taking her side is not defending her.
 
 Direction decides it, not topic. A video can be entirely about women and still not defend women: if a woman claims "women are better with money than men" or "women collaborate better than men" and he fact-checks her, he is pushing back on a claim that favors women, which is not defending women. That is men only if the claim also runs men down ("men are the emotional ones who start every war"); otherwise it is mixed. The mirror holds for claims that favor men. Ask: whose reputation or interests does the claim he pushes back on attack? That sex is the category.
 
@@ -16,16 +16,16 @@
 
 debate: another creator responded to one of HIS earlier videos (or called him out directly), and this video is his reply to their arguments. This beats men and women. Replying to a random person's claim is not debate; replying to a creator who criticized HIM is. If the video is mainly about his own account (a strike, a ban, a removed video, a channel update), it is misc even when a creator is mentioned.
 
-news: an ongoing news story or event that he mainly reports or explains: a trial, a riot, a viral case, a celebrity story. Elections, parties, governments and policy are politics, and religious claims are politics, even when they are in the news. Multi-part coverage of one case is news. If, inside a news story, his main job is answering a claim about men or about women (a claim about what men or women in general are like or deserve), choose men or women instead.
+news: an ongoing news story or event that he mainly reports or explains: a trial, a riot, a viral case, a celebrity story. Elections, parties, governments and policy are politics, and religious claims are politics, even when they are in the news. Multi-part coverage of one case is news. If, inside a news story, his main job is answering a claim about men or about women (a claim about what men or women in general are like or deserve), or debunking a false or unfair rumor or accusation aimed at one specific woman or man, choose women or men instead. Neutral reporting that lays out both sides of a case stays news.
 
 politics: politics, economics or religion: left versus right, socialism, capitalism, election rules, immigration policy, jobs and inflation data, religious history and claims. Gender statistics are not politics.
 
-misc: everything else, including a video where he mainly reacts to or praises someone else's fact-check without answering a claim himself: general dating and relationship advice, "signs she likes you", texting tips, viewer DMs and Q&A about relationships, self-improvement, motivation, channel news, skits, history or science trivia that answers no claim about men or women, and any video that answers no claim.
+misc: everything else, including a video where he mainly reacts to or praises someone else's fact-check without answering a claim himself: general dating and relationship advice, "signs she likes you", texting tips, viewer DMs and Q&A about relationships, self-improvement, motivation, channel news, skits, history or science trivia that answers no claim about men or women, and any video that answers no claim. Dating content still counts as men or women when his main job is pushing back on a list, rant or claim that runs one sex down (a viral list of women to avoid); a list of his own dating advice stays misc.
 
 # Decision rules, in order
 
 1. If another creator responded to his work or called him out, and this is his reply, choose debate.
-2. Identify the claim he pushes back on. Ask: whose reputation or interests does it attack? If it attacks men or favors women at men's expense, choose men. If it attacks women or favors men at women's expense, choose women. If it attacks both or neither, choose mixed (or another category if it is not about the sexes). His verdict ("partly true", "it's complicated") does not change the category.
+2. Identify the claim he pushes back on. Ask: whose reputation or interests does it attack? If it attacks men or favors women at men's expense, choose men. If it attacks women or favors men at women's expense, choose women. If it attacks both or neither, choose mixed (or another category if it is not about the sexes). His verdict ("partly true", "it's complicated") does not change the category. A false or unfair rumor or accusation aimed at one specific woman or man counts the same way as a claim about her or his sex, when debunking it is his main job.
 3. If there is no claim about men or women: if the subject is political, economic or religious (including elections and religious discoveries), choose politics, even when it is in the news; if he mainly covers another ongoing story, choose news; otherwise misc.
 4. Apply the men and women rules identically. A rule that would put a video in men must put the mirror-image video in women.
 5. Set borderline true only when a reasonable reviewer could pick another category, and give that category as alternate_category. Otherwise alternate_category is "none".
```
