"""Synthetic meeting transcripts for evaluating the meeting notes agent.

TRANSCRIPTS is a list of dicts: {"label": <str>, "transcript": <str>}.
Each entry is preceded by a comment identifying which scenario it covers.
"""

TRANSCRIPTS = [
    # 1. Standard product sync with clear owners
    {
        "label": "Standard product sync with clear owners",
        "transcript": """
Weekly Product Sync -- March 12, 2026

Attendees: Priya (Product Lead), Marcus (Eng Lead), Dana (Design), Tomas (QA)

Priya: Let's start with the onboarding flow redesign. Marcus, where are we on the backend work?

Marcus: The new signup API is done and deployed to staging. I still need to add rate limiting
before it goes to prod -- I'll get that done by Friday.

Priya: Great. Dana, how's the new onboarding screens looking?

Dana: Mostly done. I need one more round of feedback on the empty state illustrations. Priya,
can you review those by Wednesday?

Priya: Sure, I'll take a look Wednesday morning.

Marcus: One thing we need to decide -- are we launching the redesign to all users at once, or
doing a staged rollout?

Priya: Let's do a staged rollout. 10% of users in week one, then ramp up if there are no major
issues. Everyone good with that?

Dana: Agreed.

Tomas: Works for me, gives us time to catch bugs.

Priya: Okay, decided -- staged rollout starting at 10%.

Tomas: On the QA side, I ran the full regression suite against staging. Found two bugs -- one
where the "skip" button doesn't save state, and one where the illustration doesn't load on
slow connections. I'll file both today.

Marcus: Thanks, I'll pick up the skip button bug. Dana, the image loading one is probably yours?

Dana: Yeah, I'll fix the lazy-loading issue by end of week.

Priya: Alright, let's wrap up. Marcus -- rate limiting by Friday and the skip button bug. Dana --
illustration feedback loop and the lazy-load fix by end of week. Tomas -- file both bugs today.
I'll review the illustrations Wednesday. Thanks everyone.
""",
    },
    # 2. Meeting with no explicit decisions
    {
        "label": "Meeting with no explicit decisions",
        "transcript": """
Roadmap Discussion -- April 2, 2026

Attendees: Wei (Product), Alicia (Eng), Ben (Data Science)

Wei: I wanted to get everyone's take on whether we should prioritize the recommendation engine
rework or the search re-indexing project next quarter.

Alicia: They're both big lifts. The recommendation engine touches a lot of legacy code, so it
would probably take the whole quarter. Search re-indexing is more contained but the payoff is
less clear to me.

Ben: From a data science standpoint, the recommendation engine has more upside -- our current
model is stale and click-through has been flat for two quarters. But I don't have hard numbers
on how much a rework would move the needle.

Wei: That's fair. I think we'd want to see a rough impact estimate before committing either way.

Alicia: I could sketch out an estimate, but it'll take me a few days to get real numbers instead
of guessing.

Ben: I can pull the click-through data trend in the meantime, that might help frame it.

Wei: Let's keep talking about this. I don't think we're ready to commit to one or the other yet.

Alicia: Agreed, feels premature to lock it in today.

Ben: Yeah, let's revisit once we have more information.

Wei: Okay, we'll pick this back up. Nothing to finalize today I don't think.
""",
    },
    # 3. Very short meeting (5 minutes)
    {
        "label": "Very short meeting (5 minutes)",
        "transcript": """
Quick Sync -- April 5, 2026, 9:00am

Attendees: Sam, Nora

Sam: Hey, just wanted to confirm -- are we still good to ship the hotfix this afternoon?

Nora: Yep, tests passed overnight. I'll push it around 2pm.

Sam: Perfect, I'll let support know so they can watch for any tickets afterward.

Nora: Sounds good. That's all I had.

Sam: Same here. Talk later.
""",
    },
    # 4. Long meeting with many action items
    {
        "label": "Long meeting with many action items",
        "transcript": """
Quarterly Planning -- April 10, 2026

Attendees: Elena (VP Product), Raj (Eng Manager), Farah (Design Lead), Chris (Marketing),
Ingrid (Support Lead), Yusuf (Data)

Elena: Let's go around and capture what everyone needs to do before the Q3 kickoff.

Raj: Engineering needs to finish the migration off the old billing service. I'll assign that to
Priyanka, targeting end of month. I also owe the team a revised sprint capacity plan -- I'll have
that by next Monday.

Farah: Design owes updated brand guidelines for the new marketing site. I'll get a draft to
Chris by the 20th. I also need to run a usability session on the checkout redesign -- I'll
schedule that for next week.

Chris: On my end, I need to finalize the Q3 campaign brief and get it to Farah for review. I can
have that ready in three days. I also need someone to pull last quarter's conversion numbers so
we can benchmark -- Yusuf, could you own that?

Yusuf: Sure, I'll pull the conversion numbers by Friday. I also need to update the analytics
dashboard to track the new checkout funnel once it ships -- I'll start on that after Farah's
usability session wraps.

Ingrid: Support needs updated macros for the new checkout flow before it goes live. I'll draft
those once Farah's designs are finalized. I also want to run a training session for the support
team -- I'll schedule that for the week before launch.

Elena: Great, and I'll take ownership of communicating the timeline to leadership, and I'll
follow up with legal about the updated terms of service language for the new billing flow.

Raj: One more thing from me -- I need to circle back with the infra team about the database
migration window, I don't have a confirmed date yet.

Elena: Can you get that by Wednesday?

Raj: I'll try, I'll ping them today.

Farah: I also realized I need Chris's brand guideline feedback before I can finalize the design
system tokens -- so that's blocked on Chris's draft.

Chris: Got it, I'll prioritize getting you that draft first thing.

Elena: Okay, sounds like we have a lot moving. Let's reconvene next week to check progress.
""",
    },
    # 5. Meeting where nothing gets resolved
    {
        "label": "Meeting where nothing gets resolved",
        "transcript": """
Vendor Selection Discussion -- April 15, 2026

Attendees: Malik, Devon, Cara

Malik: So we still haven't picked between the two analytics vendors. Any strong opinions?

Devon: Honestly I go back and forth. Vendor A is cheaper but their support has been slow in the
demos. Vendor B costs more but seems more responsive.

Cara: I keep hearing mixed things about Vendor A's data accuracy too. But I haven't actually
tested either integration myself.

Malik: Same, I don't think any of us have hands-on experience with either platform yet.

Devon: Should we just try to get a trial account for both before deciding?

Cara: Maybe? Though I'm not sure who has bandwidth to run a proper trial this month.

Malik: Yeah, that's the issue. Everyone's slammed with the launch right now.

Devon: I don't think we can make a real decision without more information anyway.

Cara: Agreed. Let's not force it today.

Malik: Okay. I guess we just... keep sitting on this for now?

Devon: Seems like it. Let's see where things stand in a couple weeks.

Malik: Alright, nothing decided, we'll punt.
""",
    },
    # 6. Meeting with ambiguous ownership
    {
        "label": "Meeting with ambiguous ownership",
        "transcript": """
Incident Retro -- April 18, 2026

Attendees: Team channel sync (no names attached to most comments in the notes)

Facilitator: Okay, so the outage lasted 40 minutes. What do we need to do to make sure this
doesn't happen again?

Voice 1: Someone should really add alerting on that queue depth metric, we had no idea it was
backing up until customers started complaining.

Voice 2: Yeah, and somebody needs to update the runbook, it still references the old deploy
process.

Facilitator: Good points. Anything else?

Voice 3: We probably need better rollback tooling too. It took way too long to roll back
manually. Someone from infra should look into that.

Voice 1: Also, I think we should post a public postmortem, but I'm not sure whose job that
normally is.

Facilitator: Let's make sure these don't fall through the cracks. Can someone own the alerting
work?

Voice 2: I can maybe look at it, but I'm not officially on the infra rotation this week.

Facilitator: Okay... let's just say it needs to get picked up soon. Same with the runbook
update -- someone on the team should take that.

Voice 3: I'll mention the rollback tooling gap to the infra lead, but it's really their call who
works on it.

Facilitator: Alright, let's make sure all of this gets addressed even if we're light on names
right now.
""",
    },
    # 7. Meeting with lots of side discussion and off-topic content
    {
        "label": "Meeting with lots of side discussion and off-topic content",
        "transcript": """
Design Review -- April 22, 2026

Attendees: Jules, Petra, Omar

Jules: Okay, before we start -- did anyone see the game last night? That ending was insane.

Petra: I did not, I was up until 1am fixing a merge conflict. Never again.

Omar: Ha, rough. Okay should we get into it?

Jules: Yeah, sorry. So, the new settings page. I think the layout mostly works, but the toggle
switches feel inconsistent with the rest of the app.

Petra: Agreed, they look like they're from a different design system entirely.

Omar: Speaking of inconsistency, did we ever standardize on a color for destructive actions? I
feel like that's been an open thing forever.

Jules: Oh man, don't get me started, I brought that up like three months ago.

Petra: Let's not spiral into that today, we have limited time. Can we just fix the toggles for
now and revisit the color system separately?

Jules: Fine by me. I'll update the toggle component to match the rest of the design system by
Thursday.

Omar: Oh also, random, but did the office coffee machine get fixed? It's been broken for a week.

Petra: I heard someone submitted a ticket to facilities, no idea on timeline.

Jules: Okay, back to the settings page -- Petra, can you double check the spacing on the account
section? It looked a little cramped to me on smaller screens.

Petra: Sure, I'll check that today.

Omar: And I'll write up the destructive-action color question as a separate design debt item so
we don't lose track of it, since it clearly keeps coming up.

Jules: Perfect, let's leave it there for today.
""",
    },
    # 8. Technical engineering standup
    {
        "label": "Technical engineering standup",
        "transcript": """
Backend Team Standup -- April 24, 2026

Attendees: Hana, Victor, Leilani

Hana: Yesterday I finished the migration script for the user preferences table. Today I'm going
to run it against the staging replica to check timing before we schedule the prod run.

Victor: I got the new caching layer for the search service mostly working, but I'm seeing some
stale reads under load. I'll dig into the invalidation logic today -- probably a TTL issue.

Leilani: I merged the retry logic for the payment webhook handler yesterday. Today I want to add
metrics around retry counts so we can actually see if it's helping in prod.

Hana: Any blockers?

Victor: Kind of -- I need someone to review the caching PR before I can merge, it's been sitting
for two days. Hana, could you take a look after your migration test?

Hana: Yeah, I can review it this afternoon.

Leilani: I'm blocked on the metrics dashboard access, I put in a request but haven't heard back
from platform team.

Victor: I think Raj on platform handles those requests, might be worth pinging him directly.

Leilani: Good idea, I'll message him after standup.

Hana: One more thing -- we should decide if we're doing the prod migration Thursday or waiting
until next week given the caching issue is still open.

Victor: I'd lean toward waiting until the caching fix lands, don't want two risky changes at once.

Leilani: Agreed, let's push it to next week.

Hana: Okay, decided -- migration moves to next week instead of Thursday.
""",
    },
    # 9. Executive meeting with formal language
    {
        "label": "Executive meeting with formal language",
        "transcript": """
Executive Leadership Meeting -- April 28, 2026

Attendees: Ms. Whitfield (CEO), Mr. Abara (CFO), Dr. Lindqvist (CTO), Ms. Ferreira (COO)

Ms. Whitfield: Thank you all for joining. Let's begin with the quarterly financial review.
Mr. Abara, would you care to summarize?

Mr. Abara: Certainly. Revenue for the quarter exceeded projections by approximately four percent,
driven primarily by enterprise renewals. Operating expenses remained within the approved budget.
I would recommend we formally approve the proposed increase to the engineering headcount budget
for the coming fiscal year.

Ms. Whitfield: The board has expressed support for continued investment in engineering, so I am
prepared to approve that increase, contingent on Dr. Lindqvist providing a detailed hiring plan.

Dr. Lindqvist: Understood. I will prepare a comprehensive hiring plan, broken down by team and
quarter, and submit it for review within two weeks.

Ms. Ferreira: On the operations side, I want to raise the matter of our vendor consolidation
initiative. We have not yet reached consensus internally on which vendors to retain.

Ms. Whitfield: I would ask that Operations and Finance convene separately to finalize a
recommendation, given the budgetary implications. Mr. Abara, could you coordinate that session?

Mr. Abara: Yes, I will arrange a joint session with Ms. Ferreira's team within the next ten
business days.

Ms. Whitfield: Very well. It is my understanding, then, that we are formally approving the
engineering headcount increase, contingent on the hiring plan, and deferring the vendor
consolidation decision pending further review. Are there any objections?

Dr. Lindqvist: None from me.

Ms. Ferreira: None. That reflects my understanding as well.

Ms. Whitfield: Thank you all. This meeting is adjourned.
""",
    },
    # 10. Chaotic meeting where people talk over each other
    {
        "label": "Chaotic meeting where people talk over each other",
        "transcript": """
All-Hands Triage Call -- April 30, 2026 (partial transcript, overlapping speech)

Attendees: Theo, Nadia, Grigor, Ana, Beau

Theo: -- okay so the checkout is down for like fifteen percent of --

Nadia: -- wait is this the same issue as last week or a new --

Grigor: It's related but not the same, the last one was the payment gateway, this looks like
it's on our side --

Ana: -- can someone actually confirm that before we -- sorry go ahead --

Grigor: Yeah I'm fairly confident it's us, I'm seeing errors in our own logs, not gateway
timeouts.

Theo: Okay well regardless we need to communicate something to customers, Beau can you --

Beau: -- already drafting a status page update, give me five minutes --

Nadia: -- should we also roll back the deploy from this morning? That's when this started
right?

Grigor: Maybe, I haven't confirmed the timing lines up yet, someone should check the deploy
timestamp against when errors started.

Ana: I can check that real quick.

Theo: Okay -- Ana's checking the timing, Grigor's on the root cause, Beau's got the status
page -- Nadia can you get eyes on the rollback just in case we need it fast?

Nadia: On it, though I want to flag we haven't tested a rollback on this service in a while so
there's some risk there too.

Grigor: Noted, let's hope we don't need it.

Ana: Okay confirmed, errors started about six minutes after the deploy went out, timing lines
up.

Theo: Alright, given that -- Grigor, your call, root cause first or rollback first?

Grigor: Let's roll back, I can keep digging into root cause after service is stable.

Nadia: Okay, I'm kicking off the rollback now.

Beau: Status page updated, says we're investigating.

Theo: Good. Let's regroup in fifteen once the rollback finishes.
""",
    },
]
