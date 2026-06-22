# Prefrontal Lab v6.1.4 - Daily Momentum Update

## Purpose

This document collects all ideas for the v6.1.4 Daily Momentum Update.

Workflow rule:

1. Discuss and update this document first.
2. Save the agreed scope.
3. Implement items one by one.
4. Push to test repo first for frontend changes.
5. Publish to production only after explicit approval.

## Current Local Implementation Status

Started locally on 2026-06-18. Not pushed to test or production yet.

Implemented in the local preview:

- Weekly Daily goal: 5 out of 7 days, with compact progress bar.
- Weekly reward state: reaching 5/7 keeps the progress system in the Daily green palette.
- Weekly progress motion: after completing Daily and returning home, the weekly goal bar animates from the previous count to the new count.
- Weekly goal celebration: if that completion reaches 5/5, the bar fills to 100% and triggers a short green confetti burst.
- Preview mode should stay static; progress motion is a completion reward, not a decoration every time users open Daily.
- Tomorrow preview: locked before completion, revealed after Daily completion.
- Save-progress cue is intentionally hidden for now to avoid implying cloud sync before login/sync exists.
- Daily completion result actions: primary `See you tomorrow`, secondary `Practice again`.
- Mobile scroll safety fix: Daily page can scroll on small screens so the CTA can sit above the bottom nav.

Still not implemented:

- Streak badge visual asset set.
- Shareable Daily result card.
- Schulte share card.
- Infinite mode discovery changes.
- Dedicated English first-screen optimization.
- Full account/login/sync.

## Version Theme

Daily Momentum turns Daily Challenge from "one more task card" into a small habit loop:

- Today has a clear challenge.
- Finishing feels rewarding.
- Tomorrow has a reason to come back.
- Progress feels worth saving.

## Data Signals Behind This Version

- Daily Challenge has meaningful usage: about 653 starts and 418 completions in the current cloud snapshot.
- Daily completion rate is about 64%, good enough to invest in retention design.
- Schulte is the strongest core task, with roughly 76% completion in both basic and advanced modes.
- Infinite mode has a high completion rate, but low starts, meaning discovery is weak.
- Mobile is the primary platform, so Daily v2 must stay compact and scroll-safe.
- English/browser-English users exist, but engagement is lighter than Chinese users; English entry needs clearer positioning.

## MVP Scope

These are the recommended items for the first v6.1.4 test build.

### 1. Weekly Goal

Add a clear weekly goal to Daily Challenge.

Recommended rule:

- Weekly target: light up 5 out of 7 days.
- This is more realistic than requiring 7 out of 7.
- It gives users a sense of progress without making missed days feel fatal.

Possible UI:

- `本周目标 2 / 5`
- `Weekly goal 2 / 5`
- A compact progress bar or a stronger week-dot row.
- When the user reaches 5 days: show a weekly badge state.

States:

- Not started: `本周目标 0 / 5`
- In progress: `本周目标 3 / 5`
- Completed: `本周专注徽章已点亮`

### 2. Tomorrow Preview

Add a small preview of tomorrow's Daily category.

Goal:

- Give users a reason to return tomorrow.
- Avoid making the card too long on small phones.

Possible rules:

- Before completion: show a locked teaser.
  - `完成今日挑战后查看明日预告`
  - `Finish today to reveal tomorrow`
- After completion: reveal category, not necessarily the exact task.
  - `明天：记忆类挑战`
  - `Tomorrow: memory challenge`

Possible categories:

- Visual search
- Reaction control
- Working memory
- Logic
- Counting

### 3. Stronger Completion Feedback

Daily completion should feel more rewarding.

Current issue:

- Completion is functional but not emotionally sticky enough.

Recommended result feedback:

- `今日已点亮`
- `连续 3 天`
- `本周 3 / 5`
- `明天回来保持火苗`

Result screen actions:

- Primary after completion: `明天见`
- Secondary: `再练一次`

Do not make users feel unfinished after they already completed Daily.

### 4. Daily Card Layout Cleanup

Daily card must stay mobile-safe.

Requirements:

- User must be able to scroll to the CTA above the bottom nav.
- Daily v2 cannot make the card too tall.
- Weekly goal and tomorrow preview should be compact.
- Avoid adding large decorative blocks.

Suggested order:

1. Daily hero: title, subtitle, task icon.
2. Today task box.
3. Weekly goal row.
4. Tomorrow preview row.
5. CTA.

### 5. Save Progress Entry, Not Full Login

Keep this as a product idea, but do not show it in the Daily card yet.

Reason:

- `Saved locally` can mislead players into thinking cross-device sync already exists.
- Bring this back only when the app has a real save/sync entry point.

Deferred wording:

- Do not add save-progress copy to the Daily card in v6.1.4.
- Revisit this when sync/login has a real entry point.

Purpose:

- Prepare the user mentally for account/sync later.
- Do not force login.
- Do not interrupt Daily completion.

Good placement:

- Settings data row.
- Daily card small footer.
- Daily result screen after the user has a streak.

## Optional Enhancements For v6.1.4

These are useful but should be added only if MVP is stable.

### 6. Streak Badge Visuals

Create a more satisfying streak badge set.

Possible milestones:

- 1 day
- 3 days
- 7 days
- 14 days
- 30 days
- Perfect week

Preferred style:

- Flat or lightly dimensional, not heavy 3D.
- Warm orange flame.
- Subtle brain/circuit details.
- Premium mobile UI, not childish.

### 7. Shareable Daily Result

Allow users to share a Daily result card.

Possible content:

- Daily title
- Score
- Streak
- Weekly goal progress
- `Prefrontal Lab`

Important:

- Start with copy/share text if image generation is too much.
- Image export can come later.

### 8. Schulte Share Card

Schulte is the best propagation task.

Possible content:

- Completion time
- Score
- Mode
- `Find 1-25 as fast as you can`
- Prefrontal Lab branding

Use case:

- Social sharing.
- SEO demo.
- Later leaderboard.

### 9. Infinite Mode Discovery

Make Infinite mode easier to find.

Data reason:

- Infinite completion is high, but starts are low.

Possible UI:

- Add a small secondary action on each task card.
- Keep main task card tap as normal training.
- Do not clutter the primary nav.

Possible wording:

- `无限练习`
- `Endless practice`

### 10. English First-Screen Optimization

Improve English entry for non-Chinese users.

Current concern:

- English users exist, but engagement is lighter.
- The product should not feel like a translated Chinese tool.

Possible English positioning:

- `Quick cognitive training games`
- `Train focus, memory, inhibition, and reasoning in 60 seconds`
- `Start with a 1-25 visual search challenge`

Possible rule:

- English first screen should push Schulte or Daily first, not the full app complexity.

## Later / Not v6.1.4

These ideas are intentionally deferred.

### Full Login

Do not make full login the next visible feature.

Better framing:

- `Save my progress`
- `Sync my streak`
- `Restore on another device`

Possible future path:

1. Anonymous cloud save.
2. Sync code.
3. Google / Apple / email magic link.

### Global Leaderboard

Requires:

- Anti-cheat assumptions.
- User identity.
- Score normalization.
- Privacy decisions.

Defer until the save/sync system is clearer.

### Complex Badge Economy

Avoid building too many badge layers before proving Daily v2 improves return behavior.

### Large Daily Task Pool

Do not expand the task pool heavily before measuring which Daily categories perform best.

## Candidate Copy

### Chinese

Daily not completed:

- `今日挑战`
- `完成后点亮今天，并推进本周目标`
- `本周目标 2 / 5`
- `完成今日挑战后查看明日预告`
- `开始今日挑战`

Daily completed:

- `今日已点亮`
- `连续 3 天`
- `本周 3 / 5`
- `明天：记忆类挑战`
- `明天见`
- `再练一次`

### English

Daily not completed:

- `Daily Challenge`
- `Finish today to light up your week`
- `Weekly goal 2 / 5`
- `Finish today to reveal tomorrow`
- `Start today's challenge`

Daily completed:

- `Today is lit`
- `3-day streak`
- `This week 3 / 5`
- `Tomorrow: memory challenge`
- `See you tomorrow`
- `Practice again`

## Success Metrics

After v6.1.4 test/prod release, watch:

- Daily starts
- Daily completion rate
- Daily repeat users
- D1 return rate
- Weekly active returners
- Share/copy clicks if added
- Infinite mode starts if discovery is changed
- English user start and completion rate

## Suggested Release Timing

Based on current traffic:

- Best day by users: Monday 2026-06-08.
- Strong weekday average: Wednesday, then Monday/Thursday.
- Recommended player-visible release window: Tuesday evening or Wednesday morning.
- Avoid large player-visible releases on Friday night.

For a future v6.1.4 frontend release, a good target window is:

- Tuesday evening or Wednesday morning.
