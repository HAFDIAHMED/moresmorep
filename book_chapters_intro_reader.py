"""Chapter content: Introduction and Chapters 1-3"""
from reportlab.platypus import PageBreak, Paragraph, Spacer, Image
from generate_book import (Mark, VSpace as SP, Rule as HR, callout, theorem_box,
                           epigraph, chapter_opener, part_page, P, fig_to_image,
                           fig_exponential_cascade, fig_cascade_tree, fig_godel_timeline,
                           fig_p_vs_np, fig_windows_complexity)
import matplotlib.pyplot as plt
import numpy as np

def preface(S):
    story = []
    story += [Mark(chapter='Preface')]
    story += chapter_opener('Preface',
        'A Note on Origins',
        'How this book came to be written, and why now', S)
    story += [SP(12)]

    story.append(P(
        'This book began with a question that seemed almost too simple to be '
        'interesting: why is it that when we solve problems, we so reliably '
        'create new ones? I had noticed the pattern in the abstract for years, '
        'in the way news cycles seemed to circle the same crises with new '
        'names, in the way every public-policy fix appeared to seed the next '
        'one. But the moment the question crystallised, and the moment this '
        'book really started, came at work.',
        S['preface']))
    story.append(SP(12))
    story.append(P(
        'I was on a team tracking down a difficult bug in a large software '
        'system. The bug had surfaced in a corner of the codebase none of us '
        'had touched in months. My manager at the time, <b>Mariam Roussafi</b>, '
        'said something almost in passing — something to the effect that '
        '<i>every time someone adds a new feature, it ripples through the '
        'rest of the system; we fix one thing and three new things break</i>. '
        'It was the kind of observation any working engineer has made on a '
        'difficult day. But that day it landed differently. The pattern she '
        'had described — of solutions silently generating new problems in '
        'the parts of the system they were never meant to touch — was not '
        'just an engineering inconvenience. It was, I came to believe, a '
        'general feature of complex systems everywhere: from software to '
        'medicine, from finance to public policy.',
        S['preface']))
    story.append(SP(12))
    story.append(P(
        'A few weeks later, the second formative conversation arrived from '
        'a different direction. My friend <b>Badreddine Otky</b> — a chief '
        'technology officer with more than twenty years building and breaking '
        'large systems for a living — and I were talking about a wave of '
        'cascading outages that had been hitting the industry that year. He '
        'made the point, with the easy confidence of someone who had seen it '
        'play out a hundred times, that the architecture and incentives of '
        'modern systems make this kind of cascade not the exception but the '
        'rule: the more layers you add to keep things working, the more '
        'surfaces you create on which they can break. What Mariam had '
        'noticed inside a single codebase, Badreddine had been watching '
        'across a career\'s worth of organisations. Two independent '
        'observations, separated by context, converging on the same shape. '
        'The book that follows is what happened when I started looking for '
        'that same shape outside both codebases and CTO offices.',
        S['preface']))
    story.append(SP(12))
    story.append(P(
        'What began as a software-engineering observation quickly became a '
        'comparative question. Were Mariam\'s and Badreddine\'s remarks a '
        'feature of large software systems specifically, or were they '
        'specific instances of a more general pattern? Antibiotic resistance, '
        'foreseen by Fleming as early as 1945 '
        'and documented by microbiologists in the 1950s, had been deployed into '
        'the world anyway: the cascade was the most completely foreseeable '
        'medical crisis in history, and it had still happened. The 2008 '
        'financial crisis had generated extensive literature documenting that '
        'its cascade was similarly foreseeable. The sociologist Robert Merton '
        'had identified the general pattern of "unanticipated consequences of '
        'purposive social action" in 1936, but his framework remained '
        'qualitative and sociological, without the mathematical structure that '
        'would allow quantitative prediction. The systems theorist Donella '
        'Meadows had documented the feedback structures of complex systems '
        'with extraordinary insight but had not fully formalised the '
        'exponential dynamics of cascade generation. The pattern was '
        'well-known. The formal theory was not.',
        S['preface']))
    story.append(SP(12))

    story.append(P(
        '<b>A note on this edition.</b> This is the <i>Reader\'s Edition</i> of '
        '<i>More Solutions = More Problems</i>. It is intended to be read by '
        'anyone, regardless of mathematical background. The figures, callouts, '
        'case studies, and historical evidence of the original have all been '
        'preserved. Everything else has been rewritten in plain language — no '
        'formulas, no Greek symbols, no formal proofs. The complete mathematical '
        'framework, in symbolic form with every theorem stated, proved, and '
        'empirically calibrated, is in the underlying research paper by the '
        'present author, <i>"From Cascade Chaos to Ecosystem Harmony: A Complete '
        'Mathematical Framework for Understanding and Solving the '
        'Solution-Problem Paradox"</i>, accessible at '
        '<link href="https://www.researchgate.net/publication/395720779"><font color="#0033AA"><u>'
        'researchgate.net/publication/395720779</u></font></link>. Readers who '
        'want the formal treatment should consult that paper alongside this '
        'book; readers who want the argument and the evidence in narrative form '
        'will find them complete in the pages that follow.',
        S['preface']))
    story.append(SP(12))
    story.append(P(
        'The structure of the book is described in the Introduction. A reader '
        'who wants the conceptual argument in full should read Chapters 1, '
        '10, and 11 first, then return to the historical evidence of Chapters '
        '3-9 as illustrations of a pattern already understood. A reader who '
        'wants the evidence first should proceed directly from the Introduction '
        'to Chapters 3-9, using the non-technical summaries at the beginning '
        'of Chapters 10 and 11 as signposts. A reader who wants only the '
        'practical implications should proceed to Chapters 12 and 13 after '
        'the Introduction. The book is designed to be navigable by all three '
        'types of reader, and to reward the reader who takes all three routes.',
        S['preface']))
    story.append(SP(12))
    story += epigraph(
        'Every science begins as philosophy and ends as art.',
        'Will Durant, <i>The Story of Philosophy</i> (1926)',
        S)
    story.append(SP(12))
    story.append(P(
        '<b>AHMED HAFDI</b><br/><i>Kenitra, Spring 2025</i>',
        S['epig_attr']))
    story.append(PageBreak())
    return story


def read_this_first(S):
    """A one-page executive summary placed between the Preface and the
    Introduction. Designed for the airport-bookstore skim-reader: the whole
    thesis stated in roughly 250 words, plus a one-line route map for the rest
    of the book. The page that converts browsers into buyers."""
    story = []
    story += [Mark(chapter='Read This First')]
    story += chapter_opener('Read This First',
        'The Whole Book on One Page',
        'For the reader who has thirty seconds and wants to know what they are buying', S)
    story += [SP(8)]

    story.append(P('The Argument', S['section']))
    story.append(P(
        'Every solution, released into a connected system, generates problems faster '
        'than the system can absorb them — and the more connected the system, the '
        'wider the gap. This is true of policies, drugs, products, regulations, code, '
        'and ideas. It is not a moral failing of the people who design solutions. It '
        'is a structural property of complex systems. The book calls this <i>the '
        'cascade</i>, and it argues that the cascade can be measured, anticipated, '
        'and managed — but never eliminated.',
        S['body0']))

    story.append(SP(8))
    story.append(P('The Tool', S['section']))
    story.append(P(
        'The book builds a single practical instrument for estimating cascade risk '
        'before deployment. It is called <b>the Cobra Score</b> — formally, the '
        'Cascade Risk Index. It is a number between 0 and 1. It combines four '
        'ingredients: how readily a solution turns into new problems, how complex '
        'the solution is, how wide its reach, and how strongly it interacts with the '
        'solutions already in the ecosystem. A score below 0.3 is low risk. Between '
        '0.3 and 0.6 demands enhanced monitoring. Above 0.6 demands redesign before '
        'shipping. The number is not magical. The discipline of computing it is.',
        S['body']))

    story.append(SP(8))
    story.append(P('The Five Signals', S['section']))
    story.append(P(
        'If you read only one chapter, read Chapter Fifteen. It lists the five '
        'signals that tell you, in any meeting, that you are looking at a cascade in '
        'the making. <b>Reach without back-pressure. An incentive measured by a '
        'proxy. Irreversibility. A confident projection with no monitoring plan. '
        'Everyone in the room is a beneficiary.</b> When three of these light up, '
        'you are no longer deciding whether to deploy a solution. You are deciding '
        'whether to accept a cascade.',
        S['body']))

    story.append(SP(8))
    story.append(P('How to Read the Rest', S['section']))
    story.append(P(
        '<b>Chapters 1–2</b> are the theory. <b>Chapters 3–9</b> are seven '
        'independent bodies of evidence — mathematics, physics, computer science, '
        'economics, medicine, politics, society. <b>Chapter 10</b> ties them '
        'together into the framework. <b>Chapter 11</b> is the Cobra Score in '
        'practice. <b>Chapters 12–13</b> are the constructive response — what '
        'cascade-aware design looks like. <b>Chapter 14</b> is the case against this '
        'book, stated as honestly as possible. <b>Chapter 15</b> is the practical '
        'handle. <b>Chapter 16</b> applies the whole framework to artificial '
        'intelligence — the live cascade you are living through right now.',
        S['body']))

    story.append(SP(10))
    story.append(callout(
        '<b>The book in one sentence.</b> The harder we work to solve problems in '
        'connected systems, the faster new problems arrive — and the difference '
        'between societies that manage this and societies that do not is not effort '
        'or intelligence, but design.', S))

    story.append(PageBreak())
    return story


def intro_chapter(S):
    story = []
    story += [Mark(chapter='Introduction: The Great Paradox')]
    story += chapter_opener('Introduction', 'The Great Paradox',
        'Why every fix contains the seed of the next problem', S)
    story += epigraph(
        'The road to hell is paved with good intentions.',
        'Saint Bernard of Clairvaux, 12th century', S)
    story += [SP(12)]

    body = [
        ('section', 'The Day Britain Created More Snakes'),
        ('body0', """Delhi, the 1880s. The British administration has a problem: too many
cobras. People are dying. So the colonial government does what any rational government
would do — it offers a bounty. A rupee for every dead snake. The logic is impeccable.
Citizens hunt the cobras, the population falls, the city becomes safer."""),
        ('body', """That is not what happens."""),
        ('body', """Within months, the people of Delhi discover something the administrators
have not anticipated. It is much easier to <i>breed</i> cobras than to hunt them. Cobra
farms appear across the city. Dead snakes arrive at the colonial offices by the basketful.
The bounty payments flow. The administrators, watching their numbers climb, congratulate
themselves on the program's success."""),
        ('body', """When the government finally realises what is happening and cancels the
bounty, the farmers are left with thousands of suddenly worthless snakes. They do the
rational thing. They release them. Delhi ends up with more cobras than when it started."""),
        ('body', """This is the Cobra Effect. It is not a story about stupidity. The
administrators were not fools; they were applying standard incentive theory, which was and
remains perfectly sound. The failure was not in the people. It was in the architecture of
the solution. They were thinking linearly in a world that responds non-linearly. They were
solving the problem as if it existed in isolation, when it existed inside a web of
incentives, actors, and feedback loops that immediately reorganised itself around their
intervention."""),
        ('body', """That web is what this book is about. The bounty failed not because the
British were stupid but because every solution, once released into a complex system, sets
off a second story the designers did not write. Sometimes the second story is small.
Sometimes it is larger than the first."""),

        ('section', 'It Happens Everywhere'),
        ('body0', """The Cobra Effect is entertaining because it is exotic. Cobras, colonial
India, bounty hunters — the story has the feel of a folk parable. But the pattern is not
exotic at all. It is everywhere. The interesting question is not whether you can find it
in colonial Delhi. It is whether you can find a domain of modern life where it is
<i>absent</i>."""),
        ('body', """The automobile solved the problem of slow, expensive horse-based
transport. It created traffic congestion, urban sprawl that has consumed billions of acres
of farmland, an estimated 4.2 million annual deaths from air pollution (WHO, 2023), and a
global dependency on fossil fuels that now threatens the climate."""),
        ('body', """The internet solved the problem of expensive, slow information exchange.
It created surveillance capitalism, cybercrime costing the global economy roughly $8
trillion a year (Cybersecurity Ventures, 2023), industrial-scale misinformation, and
digital addiction affecting an estimated 400 million people worldwide."""),
        ('body', """Antibiotics solved the problem of bacterial infection. They created
antibiotic-resistant superbugs that now directly kill an estimated 1.27 million people a
year (and contribute to nearly 5 million more) — a toll one widely cited British government
review projects could reach 10 million annually by 2050."""),
        ('body', """In every case, the solution worked. The automobile really did enable
mobility. The internet really did democratise information. Antibiotics really did save
hundreds of millions of lives. The point of this book is not that these innovations were
mistakes. They were not. The point is that each of them entered a complex system, and the
system answered back. That answer is the cascade."""),

        ('section', 'What This Book Argues'),
        ('body0', """The argument of this book is simple, and the rest of the book is the
evidence for it. Solutions in complex systems do not just solve. They <i>also</i> create.
What they create grows faster than what they solve. This is not a moral failing of the
people who design solutions. It is a structural property of the systems they design
into."""),
        ('body', """Three things follow from that one claim, and each gets its own
treatment in the chapters to come. First, the cascade is structural — which is why
Chapter 10 will show that the number of potential side-effects roughly doubles every time
a new solution is added, by ordinary counting, regardless of how smart the designer is.
Second, we don't see the cascade coming, even when we should — which is why Chapter 2
will show that the temporal and cognitive gap between a solution's benefit and its
cascade is not a bug in human thinking but a feature of it. Third, the cascade can be
<i>managed</i>, even if it cannot be eliminated — which is why Part IV will show how
the rare societies and institutions that have done so actually pulled it off."""),

        ('section', 'How to Read This Book'),
        ('body0', """The book is designed to be read front to back, but each part can stand alone.
Readers primarily interested in a specific domain: medicine, economics, computer science
— can begin with the relevant chapter in Part II and follow the cross-references. Readers
who want the mathematical framework first will find it in Chapters 10 and 11; the
historical evidence in Part II then serves as illustration rather than argument. Readers
who are primarily interested in the practical implications can jump to Part IV after
reading the Introduction and Chapter 1."""),
        ('body', """A word on the figures. The book uses two visual styles on purpose.
Conceptual diagrams — cascade trees, timelines, concept maps — are drawn in a loose,
hand-sketched style to signal that they are schematic ideas, not measurements. Charts
that plot numbers use a plain, sober style instead. Where such a chart shows real data,
its caption names the source; where it merely illustrates a shape or an order of
magnitude, it says so, and the invented coordinates should not be read as measurements.
In cascade thinking what matters is the shape of the curve — linear, quadratic,
compounding — not its exact coefficients."""),
        ('body', """One more note: this is not a pessimistic book. The cascade problem is real,
and the evidence assembled here is sobering. But the authors of every genuine intellectual
advance (from Gödel to Fleming, from Keynes to Turing) understood that the map of
ignorance is not a cause for despair but a guide to the next question. The cascade is
not a wall. It is a terrain. This book is a map."""),
    ]

    for kind, text in body:
        story.append(P(' '.join(text.split()), S[kind if kind!='section' else 'section']))
        if kind == 'section':
            pass
        elif kind == 'body0':
            pass

    # ── EXTENDED INTRODUCTION CONTENT ─────────────────────────────────────────

    story.append(SP(18))
    story.append(P("The Cobra Effect Recurs Everywhere", S['section']))
    story.append(P("The Delhi debacle was not a one-off. The same structure recurs in complete institutional isolation across a century and across continents: Hanoi 1902 (a French rat-tail bounty that produced fields of tailless, still-breeding rats — documented by the historian Michael Vann); Prague in the early 1900s (a dog-tail bounty that collapsed once authorities noticed tails arriving faster than the stray-dog population could possibly produce); Cambodia in the early 2010s (a UXO reward programme in which villagers, facing transformative sums in a region of subsistence incomes, re-presented already-cleared ordnance for repeat payments, polluting the country's clearance data). Chapter 6 returns to these cases in detail and lays out their structural variants. What matters here is the cross-cultural point: none of these administrators knew of the others. The cascade recurred not because bad information spread, but because the architecture of an incentive-based solution is always and everywhere exploitable in the same way. The fault is not in the administrators. It is in the architecture of the solution.", S['body']))
    story.append(callout("<b>The Cobra Effect Template:</b> A genuine problem. A rational incentive-based solution. An agent population that optimises for the incentive rather than the underlying goal. Cancellation of the incentive. A problem larger than the original. This five-step template repeats with remarkable consistency across cultures, centuries, and domains.", S))

    story.append(SP(18))
    story.append(P("The Argument, in One Sentence", S['section']))
    story.append(P(
        "Every solution, once released into a connected system, creates problems faster "
        "than the system can absorb them — and the more connected the system, the wider "
        "the gap. That is the argument, the whole argument, and nothing else this book "
        "says will contradict it.", S['body0']))
    story.append(P(
        "You have felt this before. The new feature that broke three other things. The "
        "regulation that bred the loophole industry. The medication that needed a second "
        "medication to manage its side effects. The road that was meant to relieve traffic "
        "and made it worse. The fix that became the next thing your team had to fix. The "
        "sense that the harder we work, the further behind we fall — that is not a feeling. "
        "It is arithmetic. And it is the arithmetic this book will spend the next thirteen "
        "chapters making visible.", S['body']))
    story.append(P(
        "Two consequences come with that one sentence, and both run through the rest of "
        "the book. The first is that the cascade does not care what the solution is. A "
        "policy, a drug, a product feature, a regulation, a piece of code, a mathematical "
        "axiom — every one of them enters the same kind of connected system and triggers "
        "the same kind of response. The mechanism is structural, not moral. The second "
        "consequence is that the cascade is not destiny. Some systems contain it; most "
        "do not. The difference between the two is not effort. It is design. Knowing the "
        "difference is the practical payoff of this book.", S['body']))

    story.append(SP(18))
    story.append(P("Why This Book Is Different", S['section']))
    story.append(P("There is a crowded genre of books about complexity, unintended consequences, and the limits of human foresight. This book belongs to that genre, but it departs from the genre in several ways that the reader deserves to understand upfront. First, and most importantly, this is not a pessimistic book about the impossibility of progress. The cobra effect is real, but so is penicillin. The cascade from the internet is real, but so is the democratisation of knowledge that the internet represents. This book is not arguing that solutions are bad or that we should stop innovating. It is arguing that the accounting of solutions is systematically incomplete.", S['body0']))
    story.append(P("The analogy with environmental externalities is precise and worth dwelling on. For the first 150 years of industrialisation, carbon dioxide emissions were treated as an externality of combustion, a cost that was real and measurable but was not included in the price of the energy produced. The externality was not invisible in a literal sense; the chemistry of the greenhouse effect was described by Fourier in 1824 and quantified by Arrhenius in 1896. It was invisible in an accounting sense: the price of coal, oil, and gas reflected only the cost of extraction and delivery, not the cost of the atmospheric perturbation created by burning them. We are now living through a period in which the cost of the externality, measured in sea level rise, extreme weather events, agricultural disruption, and ecosystem collapse is beginning to exceed the benefit of the energy that generated it. The externality was always there. We chose not to price it.", S['body']))
    story.append(P("The cascade is the externality of problem-solving. Every solution generates cascade costs (new problems, new complexities, new interaction effects) that are as real as carbon emissions but are equally absent from our accounting frameworks. We measure the primary benefit of a solution (the problem it solves, the value it creates, the lives it saves) and we ignore the cascade costs, just as we ignored carbon emissions. The solutions look profitable and benign in our incomplete accounting, just as coal looked cheap and clean in 1850. The argument of this book is not that we should stop burning coal. It is that we should price the externality properly, and that proper pricing would change which solutions we choose and how we design them. Cascade-aware innovation is not pessimism. It is honest accounting.", S['body']))
    story.append(P("The second distinguishing feature of this book is its insistence on mathematical foundations. Many books in this genre argue by analogy and accumulate examples. This book does that too, the evidence in Part II is extensive. But the argument also has a mathematical backbone, developed in Chapters 10 and 11. The aim is not to place the claim beyond dispute — no claim about systems this complex can be — but to make its core mechanism precise enough to test, to quantify, and to argue about honestly. The claim that problem-generation in complex systems can grow combinatorially while solution-generation grows linearly is a structural claim about counting and connectivity, and it deserves to be examined on those terms rather than dismissed as mere pessimism.", S['body']))
    story.append(P("That last point deserves a commitment most books in this genre avoid: a claim worth taking seriously must be able to lose. So, stated plainly, this book's central claim would be refuted by a domain that deployed solutions for decades, grew steadily more interconnected, and still showed a flat or falling rate of new interaction-problems — or by a finding that a field's problem-to-solution ratio has nothing to do with how connected it is. Chapter 14 sets out these tests in full and assembles the strongest case against everything argued here, on the principle that an argument which has not survived its best critics has not yet earned the reader's assent.", S['body']))

    story.append(SP(18))
    story.append(P("A Map of the Book", S['section']))
    story.append(P("The book is organised in four parts. Part I establishes the theoretical foundations, the mathematical and psychological architecture of the cascade problem. Part II presents the evidence across seven independent domains. Part III develops the framework: how the cascade works, and how its risk can be measured and anticipated before deployment. Part IV offers the constructive response: what cascade-aware design looks like in practice, and what institutional changes would be required to implement it at scale.", S['body0']))
    story.append(P("<b>Chapter 1 (The Logic of Cascade Problems)</b> develops the central argument. It introduces the three mechanisms of cascade generation: individual complexity, interaction effects, and network amplification, and shows how together they can produce explosive problem growth. It states the core claim and discusses its relationship to Murphy's Law, Merton's unintended consequences, Jevons Paradox, and Goodhart's Law. Readers who want the quantitative version of the argument can proceed to Chapter 10 after Chapter 1; the evidence chapters in Part II then function as illustrations of a pattern already laid out.", S['body']))
    story.append(P("<b>Chapter 2 (Why We Always Repeat the Mistake)</b> examines the psychology and sociology of cascade blindness, why the cascade is systematically invisible to the people generating it. It covers temporal discounting and hyperbolic discounting, scope insensitivity and psychic numbing, the planning fallacy, and the Dunning-Kruger effect as applied to innovation cycles. It also examines the institutional incentive structures that suppress cascade information even when individuals perceive it. This chapter is, in some ways, the most disturbing in the book: it suggests that the problem is not lack of knowledge but structural features of human cognition and institutional design that make cascade awareness genuinely difficult to achieve.", S['body']))
    story.append(P("<b>Chapter 3 (Mathematics — The Original Cascade)</b> opens Part II with the evidence from the domain where human reasoning is most rigorous: pure mathematics. This chapter argues that the mathematical foundations crisis of the late nineteenth and early twentieth century: Cantor's set theory, Russell's Paradox, Hilbert's Programme, Gödel's incompleteness theorems, Turing's halting problem, and the P versus NP problem is the purest and most transparent instance of the cascade in all of human knowledge. The cascade is visible here with a clarity impossible in the social sciences precisely because the chain of solution-to-problem is mediated only by logic, not by economics, psychology, or politics.", S['body']))
    story.append(P("<b>Chapters 4 through 9</b> present the evidence from physics (the unresolved foundations of the quantum world and the cosmos), computer science (software complexity and security), economics (perverse incentives, efficiency, and financial crisis), medicine (antibiotics, opioids, and the treatment cascade), politics (the policy boomerang), and the social and ecological systems that store and amplify our interventions. Each chapter follows the same structure: a major celebrated solution, the cascade it generated, the cascade of the cascade, and the current state of the problem-solution ratio in that domain. The chapters are designed to be read independently, but the cumulative effect of reading them in sequence is significant: by Chapter 9, the reader should find the cascade less surprising and more clearly patterned, which is exactly the cognitive shift this book is designed to produce.", S['body']))
    story.append(P("<b>Chapters 10 and 11</b> develop the framework. Chapter 10 sets out, in plain language, why interacting solutions tend to generate problems faster than solutions can be deployed, and where that reasoning comes from. Chapter 11 turns the argument into a practical tool — the Cascade Risk Index — and examines the empirical patterns and early-warning signals consistent with it. Neither chapter requires mathematics beyond basic counting; the formal derivations live in the source research paper referenced in the Preface.", S['body']))
    story.append(P("<b>Chapter 12 (Cascade-Aware Design)</b> opens Part IV, the constructive response. It presents the principles of designing solutions that create fewer problems than they solve: pre-mortem analysis, interaction auditing, modularity and reversibility, staged deployment, sunset provisions, and reference-class forecasting to calibrate optimism about new solutions — illustrated with cases such as the Montreal Protocol, smallpox eradication, and the EU's REACH regulation, where cascades were genuinely contained.", S['body']))
    story.append(P("<b>Chapter 13 (A New Philosophy of Innovation)</b> closes Part IV by examining the institutional and educational changes — in government, industry, academia, and professional practice — that would be required to embed cascade awareness in decision-making at the scale at which the problem operates. <b>Chapter 14 (The Case Against This Book)</b> then turns the argument on itself, stating the strongest objections to the cascade thesis — selection bias, the overwhelmingly positive ledger of progress, unfalsifiability, and the risk that cascade thinking licenses harmful inaction — and judging honestly how much of the book survives them. <b>Chapter 15 (How to Spot a Cascade Before It Hits You)</b> hands the framework over to the reader: the five signals you can read in any room, the five questions to ask before adopting anything new, and a short personal cascade audit. <b>Chapter 16 (The AI Cascade)</b> then applies that framework to the technology every reader will be living with for the rest of the decade — the foundation models, generative systems, and large language models whose deployment is the central live cascade of our moment. A Conclusion and a set of appendices (a taxonomy of cascade types, worked case studies, checklists, and a glossary) complete the book. The cascade is among the most consequential and least recognised challenges of our era, and meeting it would require not new technology or new resources, only a more honest accounting of the costs of what we already do.", S['body']))

    story.append(SP(16))
    story.append(fig_to_image(fig_historical_timeline_local(), w=5.5*72, h=4.5*72))
    story.append(P('Figure I.1: A selection of major solution→problem pairs from 1800 to the present. '
                   'In every era, the leading innovations of the age generated new crises that '
                   'subsequent generations would spend decades managing.', S['caption']))
    story.append(PageBreak())
    return story

def fig_historical_timeline_local():
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    with plt.xkcd():
        fig,ax=plt.subplots(figsize=(7,5.2))
        ax.set_xlim(0,10); ax.set_ylim(0,12); ax.axis('off')
        ax.set_title('Selected Solution -> Problem Pairs in History', fontsize=11, fontweight='bold')
        rows=[
            ('1880s','Cobra bounty (safety)','More cobras (Cobra Effect)'),
            ('1900s','Automobile (mobility)','Pollution, sprawl, 1.35M deaths/yr'),
            ('1928','Penicillin (infection)','Antibiotic resistance'),
            ('1945','Nuclear fission (energy)','Chernobyl, 90,000-yr waste problem'),
            ('1950s','Pesticides (food)','Ecosystem collapse, Carson\'s Silent Spring'),
            ('1962','Green Revolution (hunger)','Soil degradation, monoculture fragility'),
            ('1989','World Wide Web (info)','Cybercrime, misinformation, surveillance'),
            ('1995','OxyContin (chronic pain)','500,000+ overdose deaths in USA'),
            ('2004','Social media (connection)','Polarisation, teen mental health crisis'),
            ('2022','Generative AI (productivity)','Alignment problem, deepfakes, job loss'),
        ]
        y=11
        ax.text(0.2,y+0.3,'Era',fontsize=8.5,fontweight='bold')
        ax.text(2.8,y+0.3,'The Solution',fontsize=8.5,fontweight='bold')
        ax.text(6.5,y+0.3,'The Problem It Created',fontsize=8.5,fontweight='bold')
        ax.axhline(y+0.1,color='black',lw=0.8)
        for era,sol,prob in rows:
            y-=1
            ax.text(0.2,y+0.15,era,fontsize=8,va='center')
            ax.text(2.8,y+0.15,sol,fontsize=7.8,va='center')
            ax.text(6.5,y+0.15,prob,fontsize=7.8,va='center',color='#444444')
            ax.axhline(y-0.3,color='lightgray',lw=0.4)
        fig.tight_layout()
    return fig


def fig_solution_problem_race():
    """Solutions vs Problems race: log-scale, shows the widening gap."""
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.5, 3.8))
        years = np.array([1900, 1920, 1940, 1960, 1980, 2000, 2010, 2020, 2024])
        solutions = np.array([1, 3, 8, 22, 60, 180, 320, 540, 700])
        problems  = np.array([1, 4, 14, 55, 210, 980, 2800, 7200, 12000])
        ax.semilogy(years, solutions, 'k-',  lw=2.5, marker='o', ms=5, label='Cumulative solutions deployed')
        ax.semilogy(years, problems,  'k--', lw=2.0, marker='s', ms=5, label='Cascade problems generated')
        ax.fill_between(years, solutions, problems, alpha=0.08, color='black')
        ax.set_xlabel('Year')
        ax.set_ylabel('Relative scale (log)')
        ax.set_title('The Widening Gap: Solutions vs. Cascade Problems (1900–2024)')
        ax.legend(loc='upper left', fontsize=8)
        ax.set_xlim(1895, 2030)
        ax.text(0.98, 0.03, 'ILLUSTRATIVE DATA, relative orders of magnitude, not precise counts',
                transform=ax.transAxes, fontsize=6, ha='right', va='bottom',
                style='italic', color='#555555')
        fig.tight_layout()
    return fig


def chapter1(S):
    story = []
    # Part I divider goes here, before the first chapter of the part.
    story += part_page('I', 'The Theory',
        'Two chapters establishing the mathematical and psychological foundations '
        'of the cascade problem, before the evidence makes it irrefutable.', S)

    story += chapter_opener('Chapter One',
        'The Logic of Cascade Problems',
        'How every solution carries within it the seeds of the next crisis', S)
    story += epigraph(
        'For every complex problem there is an answer that is clear, simple, and wrong.',
        'H. L. Mencken', S)
    story += [SP(12)]

    paras = [
        ('section', 'Three Mechanisms'),
        ('body0', """The argument of the last chapter was the <i>what</i>. This one is the
<i>how</i>. Three mechanisms — complexity, interaction, network — together make the
cascade. On their own, each is manageable. Combined, and in complex systems they
are always combined, they produce the kind of compounding problem growth that no
amount of well-intentioned fixing can outrun."""),

        ('body', """The first mechanism is <b>complexity</b>. Every solution adds new
moving parts to whatever it is deployed into. A new drug brings a production chain,
a regulatory pathway, prescribing guidelines, pharmacist training, monitoring
protocols, and a new entry in every drug-interaction database. A new software feature
brings documentation, test cases, edge-case handling, security review, and
compatibility checks with everything already there. A new regulation brings
enforcement, reporting, legal interpretation, and a new layer of bureaucracy. Each of
those additions is its own surface for things to go wrong."""),

        ('body', """This is not a design failure. It is the nature of a solution. A
solution that adds zero complexity is a solution that does nothing. Complexity is the
mechanism by which solutions <i>work</i>. The price of that mechanism is that complexity
is a two-sided ledger: it enables the intended function, and it opens up failure
modes that did not exist before the solution arrived."""),

        ('body', """The second mechanism is <b>interactions</b>. Solutions never sit
alone. They sit next to other solutions. Drop a new drug into a system that already
contains a thousand approved medications and you have not added one new thing — you
have added the new drug, plus a thousand new pairs of drugs, plus the three-way
combinations, and so on. Most of those interactions are harmless. But complex systems
guarantee that a small fraction will not be. A small fraction of a number that
grows by doubling is, very quickly, a large absolute number of real problems."""),

        ('body', """The US National Library of Medicine tracks interactions across more
than fourteen hundred approved medications. The number of possible pairwise drug
interactions is already close to a million. The number of three-way interactions is
over four hundred million. No physician can hold that space in their head. No clinical
trial can test it. And every new drug approval makes it bigger. This is the
interaction mechanism at full scale."""),

        ('body', """The third mechanism is <b>network reach</b>. Modern solutions sit
on top of networks — biological, social, digital, economic — that move things fast and
far. A financial instrument designed in a single Manhattan bank triggers, eighteen
months later, a crisis on every continent. An algorithm change made by an engineer
in Menlo Park shifts the political discourse of dozens of countries in a few weeks.
A new respiratory virus emerging in one market shuts down every economy on earth in
four months."""),

        ('body', """Reach means that the problems a solution creates do not stay where
the solution was deployed. They travel. The automobile was a transport solution; its
cascades reached urban planning, atmospheric chemistry, geopolitics, public health,
and the climate of the entire planet. The internet was an information-exchange
solution; its cascades reach into democracy, mental health, criminal justice, national
security, and the economics of attention. This is not metaphor. It follows the same
mathematics that describes how a virus spreads on a network: the more connected the
network, the further the cascade travels and the faster it gets there."""),

        ('section', 'Murphy\'s Law Is Not a Joke'),
        ('body0', """Most people treat Murphy's Law — <i>anything that can go wrong, will
go wrong</i> — as a sardonic joke, folk wisdom too cynical to take seriously in an age
of precision engineering. They are wrong. Murphy's Law is a mathematical observation
disguised as a joke. And it is the cascade in its most compact form."""),

        ('body', """Edward Murphy Jr. coined the law in 1949 during US Air Force
deceleration experiments. A technician had connected a set of sensors in the only
possible wrong configuration. Murphy's observation: in a system with enough
components, every possible failure mode will eventually be realised, because the
probability of at least one failure approaches certainty as the components multiply.
This is not pessimism. It is probability theory."""),

        ('body', """Here is the arithmetic. If every component of a system has even a
small chance of failure, and the components fail independently, then the probability
that the whole system works perfectly drops sharply as components are added. A system
of a hundred components, each with a 1% failure rate, has under a 40% chance of working
perfectly at any moment. A system of a thousand components has effectively no chance
at all. Adding solutions means adding components, and adding components escapes none
of this. Every new solution makes the failure surface larger."""),

        ('body', """The same logic runs through social systems, except the "components"
are incentives, actors, and feedback loops rather than mechanical parts. When the
British administrators added the cobra bounty to Delhi, they introduced a new
incentive into a system that already contained the entrepreneurial instincts of the
city, the economics of animal husbandry, and the physical distance between government
offices and the street. The new incentive interacted with all of them in ways the
administrators had not modelled. The failure was not in their competence. It was in
the combinatorial complexity of the system they were stepping into."""),

        ('section', 'The Exponential Trap'),
        ('body0', """The point of this chapter — the one worth carrying out of it — is
not that cascade problems exist. Every thoughtful reader already suspects they do. The
point is how quickly the <i>ways</i> they can arise pile up. Linear growth is
manageable. Quadratic growth is uncomfortable. The near-doubling growth of possible
interactions is the kind that overwhelms — and even a small, fixed fraction of it
turning harmful is enough to outrun our fixes."""),
    ]

    for kind, text in paras:
        story.append(P(' '.join(text.split()), S[kind]))

    story.append(SP(14))
    story.append(fig_to_image(fig_exponential_cascade(), w=5.5*72, h=3.6*72))
    story.append(P('Figure 1.1: The gap between the number of solutions added (which grows linearly) '
                   'and the number of problems generated (which doubles with each new solution). '
                   'At 10 solutions, there are already over 1,000 potential interaction effects. '
                   'At 20 solutions, over one million. The dashed curve shows the pairwise interactions '
                   'alone, which themselves dwarf the linear solution count but are swamped by the '
                   'higher-order terms representing all the ways the solutions can combine.',
                   S['caption']))

    more_paras = [
        ('body0', """Why does the growth accelerate rather than merely add up? The
answer has nothing to do with the particular field — it has to do with how complex
systems are wired. Picture a system: a city, a codebase, a body, an economy. It already
contains some number of moving parts. Now imagine adding one more. The new arrival
brings, by itself, a small amount of trouble. It also interacts with each existing part
on its own, then with every pair of existing parts, then with every triple, every group
of four, and so on, all the way up to interacting with all of them at once."""),

        ('body', """The number of these possible interaction patterns roughly doubles with
every new part added. Most of the patterns are harmless. But complex systems guarantee
that a non-trivial fraction will not be — and a small fraction of
a doubling-with-each-step number is, very quickly, a large number of real problems. This is the structural
reason why complex systems get worse faster than they get bigger."""),

        ('body', """This is not theory. Software engineers know it as <i>integration
complexity</i>. Every time a feature is added to a large codebase, the testing burden
grows not just by one but by the number of ways the new feature can combine with every
feature already there. This is why large software projects routinely spend more on
testing than on building, and why the count of bugs in any mature codebase never
quite reaches zero."""),

        ('body', """Physicians know it as <i>polypharmacy</i>. The combinations of drugs
that can interact with each other multiply with every new prescription. A patient on
ten medications has hundreds of possible drug-drug interactions to monitor; a patient
on twenty, many thousands. This is why elderly patients, who tend to be on the most
medications, are the most vulnerable to adverse drug reactions, and why medication
reconciliation — the careful review of a patient\'s complete drug list — is among
the highest-risk activities in clinical medicine."""),

        ('body', """Economists know it as <i>systemic risk</i>. A financial system with
many institutions and instruments has dramatically more channels for contagion than a
simpler one. The 2008 crisis was, at its structural core, an interaction-cascade problem:
complex instruments created complex interdependencies, and when one component failed,
the failure spread through every connection at once. The bailout programmes that
followed added more complexity, creating new interactions that are still being managed
today."""),

        ('section', 'Murphy, Merton, Jevons, Streisand'),
        ('body0', """The cascade is not a new observation. Pieces of it have been written
about for a century and a half, under different names, by people who saw their own
corner of the problem clearly. Three are worth meeting briefly, because each captures
something the cascade framework owes a debt to — and shows what the framework adds
that none of them, on their own, do."""),

        ('body', """<b>Merton's unintended consequences (1936).</b> The American
sociologist Robert K. Merton was the first to put a name on the pattern. In a
landmark paper in the <i>American Sociological Review</i>, he identified five reasons
human action produces results no one wanted: ignorance, error, short-term thinking,
values that compel action regardless of cost, and self-defeating prophecy. His
framework is <i>sociological</i> — it explains the human factors that make unintended
consequences likely. The cascade framework is structural. It explains why those
consequences are not merely likely but extremely hard to avoid, even when the people
involved are competent, well-informed, and honest."""),

        ('body', """<b>Jevons' paradox (1865).</b> William Stanley Jevons noticed that
improving the efficiency of coal-burning engines did not reduce coal consumption — it
increased it. Cheaper operation made coal-based industry more profitable, which
expanded the market. This is the cascade in miniature: the solution (efficiency)
creates a problem (more demand) that swamps the benefit. The pattern holds wherever
efficiency lowers the cost of an activity, which is most places. Chapter 6 returns to
Jevons in full."""),

        ('body', """<b>The Streisand Effect (2003).</b> The singer sued a photographer
to suppress aerial photographs of her Malibu home. Before the lawsuit, the photograph
had been downloaded six times. After the lawsuit drew worldwide attention to it, it
was downloaded over 420,000 times in a month. The Streisand Effect is the cascade in
the domain of information: the solution (suppression) amplifies the very thing it was
designed to suppress. Network reach makes that outcome predictable, not surprising."""),

        ('body', """What ties these three together — and what every chapter in this
book will return to — is a single structural fact: the solution creates new problems
through <i>the same mechanism that makes the solution work</i>. Antibiotics kill
bacteria by disrupting cell-wall synthesis, and that exact selective pressure
breeds resistant strains. The cobra bounty rewards killing cobras, and that exact
reward makes cobra breeding profitable. Efficiency makes coal cheaper to use, and that
exact cheapness expands the market for coal. The cascade is not a bug bolted onto the
solution after the fact. It is built into the solution at the level of the mechanism
itself."""),

        ('section', 'A Brief Taxonomy of Cascade Types'),
        ('body0', """Not all cascades are alike. Before proceeding to the evidence in Part II,
it is useful to introduce a preliminary taxonomy of cascade types. This taxonomy is
elaborated in detail in Appendix B; here we sketch only the broad categories."""),

        ('body', """<b>Type I — Direct Complexity Cascade:</b> The solution introduces new
components, processes, or dependencies that themselves become sources of failure. Example:
adding a new government department to administer a social program creates an
administrative apparatus that requires its own support systems, generates its own
bureaucratic pathologies, and becomes a vested interest resistant to the program's
reform or elimination. """),

        ('body', """<b>Type II — Incentive Cascade:</b> The solution modifies the incentive
landscape in a way that produces unintended behaviour. Example: the cobra bounty. The
incentive (money for dead cobras) is fully rational; it produces the unintended
behaviour (cobra farming) because it fails to account for the full response space of
the agents it affects. """),

        ('body', """<b>Type III — Interaction Cascade:</b> The solution creates new
interactions with existing solutions that generate emergent problems. Example: a new
drug that interacts adversely with an existing medication. Neither drug is harmful in
isolation; their combination creates a new problem that exists only at the intersection.
"""),

        ('body', """<b>Type IV — Network Cascade:</b> The solution propagates problems across
network connections to adjacent domains. Example: the 2008 financial crisis, in which
problems in the US mortgage market propagated through financial networks to produce
sovereign debt crises in Europe, unemployment spikes in Asia, and commodity price
collapses in Africa. The cascade crossed every domain boundary because the network
connected them all. """),

        ('body', """<b>Type V — Rebound Cascade:</b> The solution reduces the cost or
friction of the original problem activity, causing it to expand. Example: Jevons
Paradox. The efficiency improvement is real, but it triggers a demand expansion that
swamps the efficiency gain. Related examples include faster roads that induce more
driving, cheaper flights that induce more flying, and more powerful search engines that
induce more information consumption (with less comprehension per unit). """),
    ]

    for kind, text in more_paras:
        story.append(P(' '.join(text.split()), S[kind]))

    story.append(SP(14))
    story.append(fig_to_image(fig_cascade_tree(), w=5.5*72, h=4.0*72))
    story.append(P('Figure 1.2: The cascade tree. Each solution generates problems. '
                   'Each fix to those problems generates further problems. The branching '
                   'is not linear; it is combinatorial. The tree never stops growing; '
                   'it only changes shape.', S['caption']))

    story.append(SP(16))
    story.append(callout(
        '"The map is not the territory. But the cascade is in the territory whether or not it is on the map."',
        S))
    story.append(SP(16))

    more_body = [
        ('body0', """The taxonomy above is not exhaustive, and real-world cascades routinely
combine multiple types simultaneously. The opioid crisis (examined in Chapter 7)
combines a Type I cascade (the regulatory framework that approved OxyContin failed to
account for its addiction profile), a Type II cascade (the incentive structure of the
pharmaceutical industry and prescribing physicians made over-prescription rational at
the individual level), and a Type IV cascade (the problem propagated from prescription
drug abuse to heroin to fentanyl to a nationwide epidemic that crossed every
demographic boundary). Understanding which types of cascade are active in a given
system is the first step toward managing them."""),

        ('body', """The chapters that follow will show these cascade types operating
across every domain of human knowledge. The evidence is overwhelming and
consistent. But before we examine the evidence, we must understand why we are so
constitutionally ill-suited to seeing it, even when it unfolds in slow motion,
in public, over decades."""),
    ]
    for kind, text in more_body:
        story.append(P(' '.join(text.split()), S[kind]))
    story.append(SP(14))

    story.append(SP(22))
    story.append(P('What the Cascade Framework Adds', S['section']))
    story.append(SP(14))
    story.append(P(
        'There are three older bodies of work that look, at a glance, as if they '
        'have already done this job: systems dynamics, complexity theory, and risk '
        'management. They have not. Each captures one slice of the cascade. Each '
        'leaves out the slice that matters most.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        '<b>Systems dynamics</b> — Jay Forrester at MIT in the 1950s, made famous '
        'by the Club of Rome\'s <i>Limits to Growth</i> in 1972 — models complex '
        'systems as networks of stocks, flows, and feedback loops. It is right that '
        'interventions in complex systems generate surprises through feedback. But '
        'it takes the structure of the system as given and asks how policies move '
        'inside that structure. The cascade framework asks the question one floor '
        'down: what happens to the structure itself as the number of solutions '
        'sitting on top of it grows? Systems dynamics watches the dynamics. Cascade '
        'thinking watches the architecture changing under them.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        '<b>Complexity theory</b> — Stuart Kauffman, W. Brian Arthur, and the rest '
        'of the Santa Fe tradition — studies complex adaptive systems and the '
        'emergent properties that arise when their components interact. It is right '
        'that the behaviour of these systems cannot be predicted from the behaviour '
        'of their parts. But complexity theory tends to be descriptive: it tells '
        'you emergence is real, sometimes surprising, sometimes orderly, sometimes '
        'chaotic. Cascade thinking is narrower and more committal. It says: there '
        'is a specific kind of emergent property — cascade problems — that grows '
        'combinatorially with the number of solutions in the system, and you can '
        'estimate the rate before deployment.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        '<b>Risk management</b> — financial economics, engineering reliability, '
        'fault-tree analysis, value-at-risk — quantifies the chance and the size of '
        'bad outcomes. It is right that bad outcomes deserve to be planned for. Its '
        'limit is its scope. It assesses the risk of a system as designed, not the '
        'risks generated by that system colliding with everything already around '
        'it. A drug\'s risk-management dossier estimates adverse events in treated '
        'patients. It does not estimate the chance that the drug\'s prescribing '
        'incentive structure produces an epidemic. The cascade framework pushes '
        'the boundary outward: from the system to the ecosystem.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'What the cascade framework actually adds is the combination of three '
        'things no earlier framework provides at once: a structural argument for '
        'why cascade problems grow far faster than the solutions that generate '
        'them; a single risk score (the Cobra Score, formally the CRI) that can '
        'be estimated before deployment; and an explicit treatment of the '
        'ecosystem — every existing solution and every interaction — as the '
        'determinant of how bad the cascade gets. Together, those three move the '
        'question from "will this solution fail?" to "how far and how fast will '
        'the failure spread, and what is the smallest version of the deployment '
        'that finds out?"',
        S['body']))
    story.append(SP(14))

    story.append(PageBreak())
    return story


def chapter2(S):
    story = []
    story += chapter_opener('Chapter Two',
        'Why We Always Repeat the Mistake',
        'The psychology and sociology of cascade blindness', S)
    story += epigraph(
        'We do not learn from experience. We learn from reflecting on experience.',
        'John Dewey', S)
    story += [SP(12)]

    paras = [
        ('section', 'The Bias of Now'),
        ('body0', """If the cascade is always there, why don't we see it? The answer is not
that we are stupid. The answer is that the human brain is wired with a handful of biases
that served us beautifully in the environments where we evolved, and serve us
catastrophically badly in the complex systems we now build. We do not have a cascade
problem because we lack the right people. We have a cascade problem because the people
we have run on cognitive hardware that was never designed for this."""),

        ('body', """The most basic of those biases is <b>temporal discounting</b> — the
tendency to value immediate benefits more than equivalent future benefits, and to
discount future costs against equivalent present costs. This is not irrational in
evolutionary terms. If you might not live to see next month, prioritising the food on
the table over the food you could grow in spring is the right move. But in a world
where a policy decision may take a decade to fully play out, and where the consequences
land on people who are not yet born, the same wiring is a recipe for systematic error."""),

        ('body', """The classic demonstration is the marshmallow test: children offered one
marshmallow now or two marshmallows in fifteen minutes show strong preferences for
immediate reward. Adults show the same preference in economic contexts. A study by
Loewenstein and Thaler (1989) found that people valued rewards offered immediately
at roughly twice the rate of equivalent rewards offered in one year. Policy decisions
that produce immediate visible benefits but diffuse future costs are therefore
systematically over-chosen, regardless of their net present value. The cobra bounty
offered immediate, certain revenue. Its costs (more cobras) arrived later, less
visibly, and were psychologically attributed to the snakes rather than to the policy."""),

        ('body', """The second major bias is <b>scope insensitivity</b>: the inability to
perceive differences in scale when numbers become large. Studies by Desvousges and
colleagues (1993) and replicated by Kahneman and Knetsch (1992) found that people
would pay approximately the same amount to save 2,000 birds from oil spill deaths as
to save 200,000 birds. The psychological impact of the number did not scale with the
number. This has direct implications for cascade thinking: when the new problems
created by a solution number in the dozens or hundreds — scattered across different
domains, affecting different populations at different times; they do not register as
"200,000 birds." They register as a diffuse background of complications, individually
manageable, collectively catastrophic."""),

        ('body', """<b>Attribution error</b> further compounds the problem. When a solution
produces its primary benefit, we attribute the benefit to the solution. When the
cascade problems arrive, we attribute them to new causes, the incompetence of the
next implementer, changing external conditions, unforeseen bad luck, rather than to
the original intervention. The US opioid epidemic was originally attributed to patient
non-compliance, addiction-prone personalities, and street drug supply, before extensive
epidemiological research established its direct causal link to aggressive pharmaceutical
marketing and over-prescription. By that point, the cascade had been running for
twenty years."""),

        ('section', 'The Dunning-Kruger Effect in Innovation'),
        ('body0', """In 1999, David Dunning and Justin Kruger published a study showing
something that should have been more unsettling than it was. Incompetent people
systematically overestimate their own competence. Highly competent people systematically
underestimate theirs. The mechanism is elegant. Accurate self-assessment requires the
same cognitive skills as the activity being assessed. If you lack those skills, you also
lack the ability to perceive that you lack them. This is the Dunning-Kruger effect, and
it maps with uncomfortable precision onto the pattern of innovation cascades."""),

        ('body', """The innovator who introduces a solution to a complex system must, to
accurately assess its cascade risks, understand the system into which the solution is
being introduced at a level of detail comparable to an expert in every domain the
cascade will touch. The pharmacologist who designs a new drug must understand, to
anticipate its cascade, the economics of prescribing behaviour, the sociology of
addiction, the epidemiology of drug misuse, the regulatory politics of drug approval,
and the molecular biology of tolerance development. No single person understands all
of these things at expert level. The Dunning-Kruger effect means that specialists
in each domain are confident about their piece of the puzzle and unaware of the pieces
they cannot see."""),

        ('body', """This is not an accusation of individual incompetence. It is a structural
observation about the limits of specialised expertise in interconnected systems. The
pharmaceutical chemists who developed OxyContin were genuinely brilliant. The
clinical pharmacologists who studied its pain-relief properties were genuinely rigorous.
The marketing executives who positioned it as "less addictive" were genuinely wrong —
but wrong in a way that required understanding the sociology of addiction, not chemistry,
to anticipate. The system that produced the opioid crisis was assembled from components
that each made sense within its own domain. The catastrophe emerged from the
interactions between domains, exactly where the Dunning-Kruger effect is most
dangerous."""),

        ('section', 'Institutions That Pay People to Look Away'),
        ('body0', """Even when individuals do see the cascade coming, the institutions they
work inside routinely punish them for saying so. This is the third layer of cascade
blindness, and in many ways the most important — because it is the layer that explains
why the same mistakes keep being made across institutions, across generations, across
continents. It is not that no one knew. It is that the people who knew were not the
people who got rewarded for knowing."""),

        ('body', """Consider the incentive structure of pharmaceutical drug development.
A company invests billions of dollars in a new compound over a decade of development.
At the end of that process, the regulatory approval is a binary event: the drug is
approved or it is not. The financial return depends almost entirely on reaching
approval. The institutional incentive is therefore to maximise the evidence of
benefit and minimise the visibility of risk, not through outright fraud (though this
does occur) but through entirely legal practices: designing trials to measure short-term
efficacy rather than long-term safety, selecting comparison groups that maximise
relative efficacy, publishing positive results and suppressing negative ones. The
cascade risks that manifest over years or decades of real-world use are structurally
invisible to a system designed to evaluate drugs over months of controlled trials."""),

        ('body', """The same structure applies in technology. A software product that ships
features quickly generates revenue quickly. A software product that ships slowly while
carefully auditing cascade interactions delays revenue and may lose market position to
faster competitors. The institutional incentive is for speed, which means shipping
features without exhaustive interaction testing. The cascade debt accumulates silently
in the codebase until, years later, it becomes the legacy system that everyone
recognises as broken but nobody can afford to fix."""),

        ('body', """In government, the incentive structure is even more distorted. Politicians
face election cycles of four to six years. The benefits of a policy decision are most
visible (and most attributable) within the election cycle. The cascade costs often
materialise a decade or more later, at which point they are attributed to the policies
of whichever government happens to be in office when they arrive. The politician who
introduces a cascade-generating policy is rewarded at the polls. The politician who
inherits the cascade is punished for it. The system selects for cascade generation."""),

        ('section', 'What Systems Thinking Offers'),
        ('body0', """The antidote to cascade blindness is not more intelligence. It is a
different kind of thinking: the discipline of systems thinking, developed in the
second half of the twentieth century by Jay Forrester, Donella Meadows, Peter Senge,
and others. Systems thinking begins from the premise that complex systems have
properties that cannot be inferred from the properties of their components, that the
whole is genuinely different from the sum of its parts, and that understanding the
parts gives you very little insight into the system's dynamic behaviour."""),

        ('body', """Donella Meadows, in her landmark 2008 book <i>Thinking in Systems</i>,
identified a set of leverage points — places within a system where a small shift can
produce large changes in behaviour. Critically, she noted that the most obvious and
commonly exploited leverage points (adjusting numbers, sizes, and rates) are often
the least effective, while the most powerful leverage points (changing the rules,
goals, and paradigms of a system) are the most counterintuitive and the least
commonly addressed. This is a precise description of the cascade dynamic: we
habitually intervene at the symptom level (numbers and rates), generating cascades,
when the most durable interventions would target the structural level (rules and
goals), which the cascade cannot easily propagate through."""),

        ('body', """The challenge is that systems thinking is genuinely difficult — not
because the concepts are technically complex, but because they require resisting the
deeply human impulse to attribute effects to proximate causes, to treat change as
linear, and to believe that we understand a system well enough to predict its
response to intervention. The evidence in Part II of this book is intended, among
other things, as a corrective to that impulse: a demonstration, domain by domain, that
even the most rigorous and well-intentioned interventions consistently generate
cascades that the intervenors did not anticipate and could not have anticipated with
the level of systemic understanding they possessed at the time of intervention."""),
    ]

    for kind, text in paras:
        story.append(P(' '.join(text.split()), S[kind]))

    story.append(SP(18))
    story.append(P('Historical Blindness: Celebrating the Solution, Ignoring the Cascade', S['section']))
    story.append(P('Perhaps the most powerful cognitive mechanism driving cascade repetition is what we might call historical blindness: the systematic way in which institutions, cultures, and social memory celebrate the solution and ignore the cascade. We name diseases after their discoverers, not after the discoverers\' victims. We celebrate Neil Armstrong for landing on the moon, not the 3.5% of NASA\'s budget that went to the moon program instead of, say, the research programs that might have produced early antibiotic resistance interventions. We build monuments to Borlaug for the Green Revolution, not to the billions of dollars of ecological and social capital that the Green Revolution\'s monoculture approach consumed. This is not malicious. It is the natural consequence of the way human attention, narrative, and institutional reward structures work: they are calibrated to celebrate the moment of solution and to attribute subsequent difficulties to subsequent actors.', S['body0']))
    story.append(P('The classic demonstration of historical blindness in the context of pharmaceutical cascades is the Sackler family\u2019s philanthropic reputation. Richard, Mortimer, and Raymond Sackler were, for decades, among the most celebrated philanthropists in American and British academic medicine. The Sackler School of Medicine at NYU, the Sackler Centre for Arts Education at the V&A, the Sackler Wing of the Metropolitan Museum of Art, the Sackler Gallery at the Smithsonian — these names represented the pinnacle of philanthropic achievement. The cascade that the Sackler family\u2019s company, Purdue Pharma, generated through the aggressive marketing of OxyContin was simultaneously building through the 1990s and 2000s, invisible in the narrative of philanthropic success. It was not until 2017 that major cultural institutions began removing the Sackler name, and not until 2021 that the legal and financial consequences of the opioid cascade resulted in Purdue Pharma\u2019s bankruptcy and a settlement of $4.5 billion, a fraction of the estimated $57 billion in economic costs of the opioid epidemic annually. The celebration preceded the reckoning by two decades. Historical blindness is not merely a private cognitive bias; it is an institutional dynamic that determines which information receives attention and which recedes into the background.', S['body']))
    story.append(P('The institutional manifestation of historical blindness is the citation structure of scientific literature. Papers that introduce novel solutions receive far more citations than papers that document the cascade effects of those solutions. A 2021 analysis of citation patterns in biomedical literature found that papers reporting positive clinical results (solutions working as intended) received an average of 4.7 times more citations than papers reporting adverse effects or cascade complications of the same solutions. This asymmetry in scientific attention is not simply a matter of novelty: the citation gap persists even when adverse effect papers are published in higher-impact journals and are methodologically superior to the positive papers they reference. The citation asymmetry means that the scientific infrastructure that guides clinical practice, regulatory decisions, and subsequent research is systematically skewed toward the benefit side of the cost-benefit ledger. The cascade is documented in the literature; it is simply cited less, read less, and acted upon less than the evidence of benefit.', S['body']))
    story.append(callout('<b>The Four Layers of Cascade Blindness:</b> (1) Temporal discounting; we value immediate benefits over distant costs. (2) Scope insensitivity; we cannot perceive the scale of diffuse cascade damage. (3) Attribution error; we attribute cascade effects to proximate causes rather than the original solution. (4) Historical blindness — our institutions celebrate solutions and minimise cascade documentation. Each layer independently generates cascade blindness; together they constitute a systematic cognitive and institutional architecture for ignoring the cascade even when its evidence is in front of us.', S))
    story.append(SP(14))

    # ── Chapter 2 extended ─────────────────────────────────────────────────
    story.append(SP(18))
    story.append(P('The Narrative Fallacy and Cascade Invisibility', S['section']))
    story.append(P(
        'Nassim Nicholas Taleb\'s concept of the "narrative fallacy", the '
        'human tendency to impose coherent stories on sequences of events that '
        'are, in reality, driven by complex causal webs is directly relevant '
        'to cascade blindness. Cascades are, by definition, stories with a '
        'twist: the solution was supposed to solve the problem, and instead it '
        'generated a new one. This twist violates the narrative structure that '
        'human cognition most readily constructs around technological and '
        'policy interventions. We prefer stories of heroes solving problems '
        'to stories of heroes solving problems while inadvertently creating '
        'new ones. The hero-who-causes-a-worse-problem is a villain in '
        'conventional narrative structure, and cognitive dissonance theory '
        'predicts that we will resist framing celebrated innovators as '
        'unintentional villains, even when the cascade evidence is clear.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The narrative fallacy generates a specific form of cascade blindness: '
        'the attribution of cascade problems to a different cause than the '
        'solution that generated them. The opioid epidemic was, for years, '
        'attributed to individual moral weakness of addicted patients, '
        'to the failures of regulatory oversight, and to the criminal '
        'behaviour of a single company (Purdue Pharma) rather than to '
        'the fundamental cascade generated by the widespread prescription '
        'of powerful opioids for chronic pain. This attribution allowed '
        'the underlying solution (opioid prescribing) to continue largely '
        'unchanged while the narrative focused on individual and institutional '
        'failures. The attribution error is not random; it systematically '
        'protects the solution from cascade accountability by directing '
        'attention toward individual agents rather than systemic structures.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'Kahneman\'s distinction between System 1 (fast, intuitive, narrative) '
        'and System 2 (slow, deliberative, analytical) thinking provides a '
        'cognitive architecture for understanding cascade blindness. Cascade '
        'assessment requires System 2 thinking: it requires tracing causal '
        'chains across multiple steps, considering counterfactuals, modelling '
        'the responses of multiple agents, and maintaining uncertainty about '
        'complex dynamic systems. System 1 thinking, which dominates most '
        'everyday cognition and most organisational decision-making under '
        'time pressure, generates quick, confident assessments of proximate '
        'causes and visible benefits. System 1 is precisely the cognitive '
        'mode that the innovation environment rewards: it produces rapid '
        'decisions, clear narratives, and confident projections. The '
        'institutional incentive to accelerate innovation by shortening '
        'decision cycles is simultaneously an incentive to suppress System '
        '2 cascade thinking by reducing the time available for it.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The research on expert overconfidence is particularly relevant to '
        'cascade blindness. Philip Tetlock\'s decades-long study of expert '
        'political and economic forecasting, summarised in "Superforecasting" '
        '(2015), found that experts perform only slightly better than chance '
        'at predicting the outcomes of complex social and political processes. '
        'More relevant to the cascade problem, Tetlock found that the most '
        'prominent experts. Those most often consulted, most publicly '
        'confident, with the most coherent and articulate theories — performed '
        'worse than experts with more tentative, eclectic, and uncertainty-'
        'acknowledging perspectives. The "hedgehog" experts, who explain '
        'complex phenomena through a single big idea, consistently outperformed '
        'by "fox" experts who reason from multiple models and hold their '
        'views with explicit uncertainty. Cascade awareness is, in Tetlock\'s '
        'typology, a fox virtue: it requires simultaneous attention to multiple '
        'causal channels, explicit acknowledgment of uncertainty, and resistance '
        'to the seductive narrative coherence of the hedgehog.',
        S['body']))
    story.append(SP(14))
    story.append(callout(
        '<b>The Cascade Visibility Paradox:</b> The institutional environments '
        'most likely to generate large cascades: fast-moving, high-confidence, '
        'innovation-driven organisations are precisely the environments '
        'most hostile to the slow, uncertain, multi-model thinking required '
        'to detect cascade risks. Cascade blindness is not a random failure; '
        'it is a systematic consequence of the cognitive and institutional '
        'conditions that produce successful innovation.',
        S))
    story.append(SP(14))

    story.append(SP(18))
    story.append(P('The Innovator\'s Blindspot: Why Creators Miss Cascades', S['section']))
    story.append(P(
        'Among the most consistent findings in the history of '
        'cascade generation is that the creators of solutions '
        'are among the least likely to anticipate their '
        'cascades. The pattern is not random; it reflects '
        'a systematic relationship between creative investment, '
        'cognitive commitment, and cascade blindness.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'Innovators are, by definition, deeply invested in the '
        'success of their solutions. This investment: financial, '
        'reputational, intellectual, emotional — creates the '
        'motivational conditions for confirmation bias: '
        'the tendency to seek and interpret information '
        'in ways that confirm prior beliefs. An innovator '
        'who has spent years developing a solution is '
        'cognitively committed to its value; they will '
        'naturally weight evidence of success more heavily '
        'than evidence of cascade. This is not dishonesty '
        '— it is the predictable operation of a brain '
        'designed to protect its investment of time and '
        'identity. The scientist who discovers a new compound, '
        'the engineer who designs a new system, the '
        'entrepreneur who builds a new platform, all '
        'have the deepest expertise in the solution\'s '
        'mechanism and the strongest motivation to '
        'discount its risks.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The sociologist of science Bruno Latour documented '
        'a related phenomenon in his studies of laboratory '
        'practice: scientists construct facts through '
        'networks of allies: instruments, colleagues, '
        'funding bodies, publications, and defend '
        'those facts against challenges by mobilising '
        'the network. A challenge to a scientific finding '
        'is therefore a challenge to an entire network '
        'of alliances, not merely to a single claim. '
        'The resistance to Ignaz Semmelweis\'s germ '
        'theory, the Vienna physician who demonstrated '
        'in 1847 that handwashing could prevent puerperal '
        'fever, and who was dismissed, ridiculed, and '
        'eventually committed to a mental institution '
        '— was not simply individual stubbornness. '
        'It was the resistance of an established medical '
        'network to evidence that would have required '
        'the network\'s members to acknowledge that '
        'they had been killing their patients. '
        'The cascade, from the solution of '
        'modern medical practice to the problem '
        'of infection spread by unwashed physician '
        'hands was invisible to its generators '
        'because acknowledging it would have been '
        'existentially threatening to their '
        'professional identity.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'Thomas Kuhn\'s concept of the paradigm provides '
        'the theoretical framework for this phenomenon. '
        'Scientific communities work within paradigms '
        '— frameworks of assumptions, methods, and '
        'exemplary problems that define what counts '
        'as a legitimate question and what counts '
        'as a valid answer. Cascade problems that arise '
        'within a paradigm are difficult to see from '
        'within the paradigm, because the paradigm '
        'defines the categories of analysis. CFCs '
        'were not a problem within the paradigm '
        'of chemical engineering; they were a '
        'solution. The ozone depletion cascade '
        'was visible only from within atmospheric '
        'chemistry, a different paradigm with '
        'different measurement tools and different '
        'categories of concern. The detection '
        'of cascade problems systematically requires '
        'perspectives from outside the generating '
        'paradigm. This is why effective cascade '
        'management requires genuine disciplinary '
        'diversity, not the superficial diversity '
        'of multiple engineers from different '
        'companies looking at the same system '
        'through the same conceptual framework.',
        S['body']))
    story.append(SP(14))
    story += epigraph(
        'The significant problems we face cannot be solved at the same level '
        'of thinking we were at when we created them.',
        'Albert Einstein',
        S)
    story.append(SP(14))

    story.append(SP(18))
    story.append(P('Chapter 2 Synthesis: Redesigning Human Reasoning for a Cascade World', S['section']))
    story.append(P(
        'The cognitive and institutional barriers to cascade awareness '
        'documented in this chapter are not incidental features '
        'of human psychology; they are deep adaptations to the '
        'ancestral environment. Temporal discounting was rational '
        'in environments where the future was radically uncertain; '
        'statistical discounting was adaptive when statistical '
        'information did not exist; professional specialisation '
        'enabled the division of labour that built civilisation. '
        'The problem is not that these adaptations are maladaptive '
        'in general; it is that they are specifically '
        'maladaptive for the task of cascade anticipation '
        'in complex technological systems.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The solution is not to change human psychology; it is '
        'to design institutions that compensate for its '
        'systematic biases. This is the project of Part IV '
        'of this book. But the foundation for that project '
        'is the recognition, argued in this chapter, '
        'that cascade blindness is not a failure of '
        'individual intelligence or integrity. The most '
        'brilliant scientists, the most experienced '
        'policymakers, the most sophisticated financial '
        'analysts have all failed to anticipate cascades '
        'that seem obvious in retrospect. This is not '
        'because they were stupid or careless; it is '
        'because cascade anticipation requires cognitive '
        'and institutional capabilities that evolution, '
        'culture, and professional training have not '
        'historically equipped us to deploy.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The practical implication is humility. The argument '
        'of cascade theory is not that we should stop '
        'deploying solutions; it is that we should '
        'deploy them with the institutional equivalent '
        'of peripheral vision: structures and processes '
        'that look beyond the solution\'s intended '
        'effects to its lateral and downstream '
        'interactions. This is not a call for '
        'paralysis; it is a call for the '
        'kind of second-order thinking that '
        'distinguishes the statesman from '
        'the politician, the engineer '
        'from the inventor, the physician '
        'from the pharmacologist.',
        S['body']))
    story.append(PageBreak())
    return story


def chapter3(S):
    story = []
    # Part II divider — Part II = Chapters 3 through 9.
    story += part_page('II', 'The Evidence',
        'Seven domains. Seven independent bodies of research. One conclusion: '
        'the cascade is not an accident. It is the rule.', S)

    story += chapter_opener('Chapter Three',
        'Mathematics — The Original Cascade',
        'Where humanity first discovered that solving a problem always opens another', S)
    story += epigraph(
        'God exists since mathematics is consistent, and the Devil exists since '
        'we cannot prove it.',
        'André Weil', S)
    story += [SP(12)]

    paras = [
        ('section', 'Hilbert\'s Dream'),
        ('body0', """In the summer of 1900, the German mathematician David Hilbert stood before
the Second International Congress of Mathematicians in Paris and presented twenty-three
unsolved problems that he believed would define the future of mathematics. The list was
an extraordinary document, the most influential research agenda in the history of
science. But it was also something more: it was an expression of a fundamental belief
about the nature of mathematics itself."""),

        ('body', """Hilbert believed, with the confidence of a man who had transformed
geometry, analysis, and number theory, that mathematics was, in principle, solvable.
That every well-posed mathematical question had a definite answer, either true or false.
That given enough time and enough talent, the mathematical community could, in
principle, answer every question it could formulate. This belief, known as Hilbert's
Programme, was the intellectual equivalent of a policy initiative: a systematic
approach to solving all the foundational problems of mathematics once and for all.
It was the ultimate mathematical solution."""),

        ('body', """The cascade arrived in 1931. A twenty-five-year-old Austrian
logician named Kurt Gödel published a paper titled "On Formally Undecidable
Propositions of Principia Mathematica and Related Systems." In two incompleteness
theorems, Gödel proved something that Hilbert's Programme had implicitly assumed
was impossible: that in any consistent formal system powerful enough to express
arithmetic, there exist true statements that cannot be proved within that system.
Mathematics was, by its very nature, incomplete. The attempt to solve all of
mathematics had proved, with mathematical precision, that mathematics could
never be fully solved."""),

        ('body', """Hilbert's reaction, by all accounts, was one of disbelief and then
despair. He had spent his career building the edifice that Gödel had just shown
could never be completed. But Gödel's theorems were not a refutation of mathematics —
they were a profound deepening of it. They opened entirely new fields: mathematical
logic, proof theory, computability theory. The cascade of new mathematics generated
by Gödel's "problem" for Hilbert's Programme dwarfs in richness and difficulty anything
that Hilbert's Programme had hoped to systematise."""),

        ('section', 'Russell\'s Paradox and Its Descendants'),
        ('body0', """Gödel's incompleteness theorems did not appear from nowhere. They were
the culmination of a cascade that had begun three decades earlier with a simpler but
equally devastating discovery. In 1901, Bertrand Russell, working through Georg
Cantor's newly developed theory of infinite sets, encountered a paradox that would
force the complete reconstruction of the logical foundations of mathematics."""),

        ('body', """Cantor had developed set theory in the 1870s and 1880s as a way to
handle the mathematics of the infinite, a problem that had bedevilled mathematicians
since ancient Greece. His solution was breathtaking in its audacity and power: treat
different sizes of infinity as mathematical objects, define operations between them,
and prove precise theorems about their relationships. The German mathematician David
Hilbert called Cantor's work "a paradise from which no one shall expel us." It seemed
to provide exactly the rigorous foundation that mathematics needed."""),

        ('body', """Russell's Paradox shattered the paradise. Consider the set R of all
sets that do not contain themselves. Does R contain itself? If it does, then by
definition it doesn't. If it doesn't, then by definition it does. The paradox is not
a mathematical curiosity; it is a logical contradiction that demonstrates that
Cantor's naive set theory was inconsistent. A mathematics built on an inconsistent
foundation could prove anything, including false statements. The solution had to
be dismantled and rebuilt."""),

        ('body', """The reconstruction effort took decades and spawned three competing
approaches: Type Theory (Russell and Whitehead), Zermelo-Fraenkel Set Theory
(Zermelo, Fraenkel, and others), and Intuitionism (Brouwer), each of which solved
the consistency problem and each of which created substantial new problems of its own.
Type Theory was cumbersome and difficult to use. ZF set theory required the Axiom of
Choice, which implied the Banach-Tarski paradox (a sphere can be decomposed and
reassembled into two spheres of the same size, a result so counterintuitive that it
permanently disrupted mathematical intuitions about volume and measure). Intuitionism
rejected the law of the excluded middle, making it impossible to use
proof-by-contradiction, the most powerful tool in the mathematical toolkit."""),

        ('body', """Each fix generated new problems. Each new axiomatic system turned
out to have independent statements — questions that could not be answered either
way within the system. Paul Cohen proved in 1963 that the Continuum Hypothesis —
whether there is an infinite set "between" the size of the natural numbers and the
size of the real numbers was independent of ZF set theory. It was neither provable
nor disprovable from the axioms. The problem of finding the right axioms to "fix"
mathematics had itself generated an infinite regress of foundational questions that
no finite set of axioms could close."""),

        ('section', 'The Halting Problem: When Computation Discovers Its Own Limits'),
        ('body0', """In 1936, Alan Turing: working independently of, but in parallel with,
the logician Alonzo Church, proved a result that would define the limits of
computation a full decade before computers existed in any practical form. The Halting
Problem asks: is there a general algorithm that, given any program P and any input I,
can correctly determine whether P will halt (finish execution) or run forever?"""),

        ('body', """Turing proved, using a now-famous diagonal argument, that no such
algorithm can exist. The proof is by contradiction: assume such an algorithm H exists.
Construct a new program Q that uses H to determine what H predicts Q will do, and
then does the opposite. Q's behaviour defeats H's prediction by definition, contradicting
the assumption that H works for all programs. The Halting Problem is undecidable —
not merely unsolved, but provably beyond the reach of any algorithmic solution."""),

        ('body', """The implications cascaded through computer science for the next eighty
years. The undecidability of the Halting Problem implies the undecidability of virtually
every interesting question about programs: Does this program contain a bug? Will this
program ever produce a security vulnerability? Will this program terminate before the
heat death of the universe? All of these questions are, in the general case, as
undecidable as the Halting Problem. Every antivirus scanner, every static analysis
tool, every formal verification system is an approximation to a problem that is
provably impossible to solve exactly."""),

        ('body', """Computer security offers the most concrete cascade from the Halting
Problem. Because general program analysis is undecidable, every security analysis
tool must make approximations, and those approximations necessarily leave gaps.
Malware authors exploit the gaps. Security researchers patch the gaps. New malware
exploits the patches. The arms race between security and malware is a direct
consequence of the mathematical impossibility of perfect program analysis. The
original cascade: Hilbert's question about decidability, solved by Turing's
undecidability proof has been running for nearly ninety years and shows no
sign of converging."""),

        ('section', 'P versus NP: The $1 Million Question'),
        ('body0', """In 1971, the computer scientist Stephen Cook published a paper that
transformed theoretical computer science and created what is now widely considered
the most important open problem in mathematics: Does P equal NP?"""),

        ('body', """The P versus NP problem asks whether problems whose solutions can be
quickly verified (NP problems) can also be quickly solved (P problems). The intuition
is that verification seems easier than solution; it is easy to check that a proposed
solution to a jigsaw puzzle is correct, but hard to find the solution in the first
place. Cook's paper showed that there is a class of problems — NP-complete problems —
for which, if any one of them could be efficiently solved, then all of them could be.
The existence of this class transformed the P versus NP question from a technical
curiosity into a question with trillion-dollar implications for cryptography, artificial
intelligence, logistics, biology, and economics."""),

        ('body', """The cascade from this question has been spectacular. Over 3,000 problems
have been proved NP-complete since 1971, meaning that the difficulty of solving them
is equivalent to solving P versus NP. The question spawned computational complexity
theory, which is now one of the richest areas of theoretical computer science.
It motivated the development of approximation algorithms, heuristics, and probabilistic
computation as ways of managing problems that cannot be solved exactly. It inspired
the development of public-key cryptography, which depends on the practical
intractability of certain NP-hard problems. The entire security infrastructure of
the modern internet: SSL/TLS certificates, bank transactions, password hashing —
rests on the assumption that P ≠ NP, an assumption that has not been proved after
fifty years of concentrated effort by the world's best mathematicians."""),

        ('body', """The problem that started as "let's understand the nature of efficient
computation" has generated an entire civilisation's worth of open questions. This is
the mathematical cascade in its purest form: a precisely stated question, a rigorous
partial answer, and a resulting frontier of new and deeper questions that has expanded
faster than it has been explored for over half a century."""),
    ]

    for kind, text in paras:
        story.append(P(' '.join(text.split()), S[kind]))

    story.append(SP(14))
    story.append(fig_to_image(fig_godel_timeline(), w=5.5*72, h=3.6*72))
    story.append(P('Figure 3.1: The mathematics cascade from Cantor to the Halting Problem. '
                   'Each landmark result solved one foundational problem and immediately '
                   'generated deeper, harder problems. The cascade has not stopped — current '
                   'open problems in foundations include the Continuum Hypothesis, the '
                   'consistency of large cardinal axioms, and P versus NP.', S['caption']))

    story.append(SP(10))
    story.append(fig_to_image(fig_p_vs_np(), w=5.5*72, h=3.6*72))
    story.append(P('Figure 3.2: The direct lineage from Hilbert\'s decidability question (1928) '
                   'to the P vs NP problem (1971). Each answer revealed a deeper question. '
                   'The Clay Mathematics Institute now offers $1,000,000 for a solution, '
                   'a sum that has sat unclaimed for over two decades.', S['caption']))

    more = [
        ('section', 'What Mathematics Teaches Us'),
        ('body0', """Mathematics is the domain where human reasoning is most rigorous, where
the standards of proof are highest, where the cascade has the least opportunity to
hide behind ambiguity or interpretive flexibility. And yet mathematics is the domain
where the cascade is most perfectly visible. Every foundational crisis — Russell's
Paradox, Gödel's Incompleteness, Turing's Undecidability was a direct consequence
of rigorous, successful mathematical work. The problems were not created by sloppiness.
They were created by precision."""),

        ('body', """This is the deepest lesson of the mathematical cascade: it is not a
consequence of doing things wrong. It is a consequence of doing things right. The
better the mathematics, the more clearly it reveals the territory of what cannot be
proved. Hilbert's Programme failed not because Hilbert was wrong to pursue it, but
because he was right enough to make Gödel's proof possible. The attempt to solve
mathematics completely was itself the most powerful tool ever devised for proving that
mathematics cannot be completely solved."""),

        ('body', """This pattern — success generating the precise tools needed to demonstrate
the limits of success — recurs throughout the evidence in the following chapters.
The better the antibiotic, the stronger the selection pressure for resistance.
The better the financial instrument, the more precisely it channels systemic risk.
The better the social media algorithm, the more effectively it amplifies extremity.
In each case, the cascade is not a sign that something has gone wrong. It is a sign
that something has gone very, very right, and that right enough was not enough."""),
    ]

    for kind, text in more:
        story.append(P(' '.join(text.split()), S[kind]))

    story.append(SP(18))
    story.append(P('The Calculus Cascade: Three Centuries of Foundations', S['section']))
    story.append(P('The cascade generated by Newton\'s and Leibniz\'s calculus is instructive for its longevity: it took approximately 300 years to fully resolve, and the resolution itself generated new open questions. Newton developed the calculus in 1666 (published 1687 in the Principia) and Leibniz independently in 1675 (published 1684). Both formulations relied on the concept of the infinitesimal, a quantity smaller than any positive number but greater than zero. The practical power of the calculus was immediately apparent: it solved the problem of instantaneous rates of change, areas under curves, and the motion of bodies under forces with a generality and precision that no previous mathematical tool approached. The cascade arrived immediately.', S['body0']))
    story.append(P('In 1734, Bishop George Berkeley published "The Analyst," a devastating critique of the logical foundations of the calculus. Berkeley, motivated partly by a defence of religious faith against scientific materialism, demonstrated that the infinitesimal dx was being treated inconsistently: when convenient, it was treated as a nonzero quantity (to perform the differentiation); when inconvenient, it was treated as zero (to simplify the result). Berkeley\'s argument was not merely philosophical rhetoric; it was mathematically correct. He summarised the infinitesimal as "neither finite quantities, nor quantities infinitely small, nor yet nothing." The solution that had produced the most powerful mathematical tool in history rested on a logical contradiction. The calculus worked (the results were correct, as confirmed by experiment) but no one could explain why it worked without invoking a concept (the infinitesimal) that violated the laws of arithmetic.', S['body']))
    story.append(P('The cascade response occupied the next century of mathematics. Augustin-Louis Cauchy, in his 1821 Cours d\'analyse, introduced the epsilon-delta definition of limits: instead of speaking of infinitesimals, he spoke of arbitrarily small but nonzero quantities, and defined the limit of a function in terms of inequalities that avoided the paradoxical language of the infinitesimal. This was a genuine advance, the epsilon-delta framework was logically rigorous in a way that Newton\'s and Leibniz\'s formulations were not. But it generated its own cascade. Karl Weierstrass, working through the implications of the epsilon-delta framework in the 1860s and 1870s, constructed functions that were continuous everywhere but differentiable nowhere: functions that oscillated infinitely rapidly at every point, violating the intuition that continuous functions should be "smooth." Weierstrass\'s monster functions were a direct consequence of the epsilon-delta framework\'s generality: it was rigorous enough to include functions that no one had imagined, including functions that violated every geometric intuition about continuity and smoothness. The solution to Berkeley\'s paradox had opened the door to mathematical objects that the solution\'s inventors would have found incomprehensible.', S['body']))
    story.append(P('The cascade continued with Henri Lebesgue\'s 1901-1904 development of measure theory and the Lebesgue integral, which was motivated by the discovery that the Riemann integral (the standard integration theory since the 1850s) could not integrate the pathological functions that Weierstrass and others had produced. Lebesgue\'s integral resolved the integration problem for a much larger class of functions, but it required an entirely new mathematical infrastructure (measure theory, sigma-algebras, measurable sets) that added layers of abstraction to a subject already considerably more abstract than Newton had envisioned. In 1960, Abraham Robinson finally rehabilitated the original infinitesimal in a fully rigorous framework: non-standard analysis, using model theory and ultrafilters from mathematical logic, constructed a consistent number system that included genuine infinitesimals. The infinitesimal that Berkeley had correctly identified as logically incoherent in 1734 was finally given a rigorous definition in 1960 — 226 years later, at the cost of requiring a substantial portion of modern mathematical logic as background infrastructure. The cascade from a concept introduced to solve the problem of instantaneous rates of change took three centuries to fully resolve, and the resolution requires more mathematical machinery than the problem it was solving required.', S['body']))
    story.append(P('The Banach-Tarski Paradox is perhaps the most vivid example of the cascade generated by the Axiom of Choice, which was introduced in the early twentieth century to resolve certain otherwise undecidable set-theoretic questions. The Axiom of Choice states that given any collection of non-empty sets, it is possible to choose one element from each set simultaneously, even if the collection is infinite and no explicit selection rule is available. The axiom is intuitively plausible and enormously useful: it resolves dozens of otherwise unprovable theorems in analysis, topology, and algebra. Its cascade is the Banach-Tarski Paradox (1924): using the Axiom of Choice, it is possible to decompose a sphere into a finite number of pieces and reassemble those pieces into two spheres of the same size as the original. This is not a physical claim, the decomposition involves non-measurable sets that have no physical interpretation but it is a mathematical theorem, rigorously proved from the axioms of set theory with the Axiom of Choice included. The solution to the undecidability problems that motivated the Axiom of Choice generated a result so counterintuitive that it has the character of a logical paradox, despite being a theorem. Paul Cohen\'s 1963 proof that the Axiom of Choice is independent of the other axioms of ZF set theory means that mathematics can be consistently developed either with or without it but that either choice generates a different mathematical universe, with different theorems, different counterintuitive results, and different cascade structures.', S['body']))
    story.append(callout('<b>The Mathematics Cascade in One Statistic:</b> Hilbert\'s Programme proposed in 1900 that all of mathematics could be formalised in a finite, consistent axiomatic system. By 2024, the list of open mathematical problems, problems generated by the cascade of solutions to the problems that motivated previous solutions — includes seven Millennium Prize Problems (each with a $1 million prize), thousands of problems in the Clay Mathematics Institute\'s open problem list, and an uncountable (in the colloquial sense) collection of conjectures across every field of mathematics. The attempt to solve all of mathematics generated a frontier of unsolved mathematics that grows faster than mathematicians can solve it.', S))

    story.append(SP(22))
    story.append(P('Complexity Theory: The Cascade of Computational Questions', S['section']))
    story.append(SP(14))
    story.append(P(
        'Complexity theory, the branch of theoretical computer science that studies '
        'the resources required to solve computational problems, is itself a cascade '
        'generated by the success of computability theory. Alan Turing\'s 1936 '
        'paper established what computers can and cannot compute in principle; '
        'the next natural question was what computers can and cannot compute '
        '<i>efficiently</i>, within polynomial time, with polynomial memory. '
        'This question, which seems more practical than Turing\'s theoretical '
        'concerns, generated a theoretical superstructure of extraordinary depth '
        'and difficulty.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The complexity class P contains all decision problems solvable in polynomial '
        'time on a deterministic machine. The complexity class NP contains all '
        'decision problems whose solutions can be verified in polynomial time, '
        'problems where, given a proposed answer, you can check whether it is '
        'correct quickly, even if you cannot find the answer quickly. The question '
        'of whether P = NP, whether every problem whose solution can be verified '
        'quickly can also be solved quickly is the central open question of '
        'theoretical computer science and one of the Millennium Prize Problems.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The cascade from the P vs. NP question is the proliferation of complexity '
        'classes. NP-completeness, identified by Stephen Cook (1971) and Richard '
        'Karp (1972), describes a class of problems within NP such that if any '
        'one of them can be solved in polynomial time, all of them can. The '
        '21 problems in Karp\'s original list have since expanded to over 3,000 '
        'known NP-complete problems spanning optimisation, scheduling, graph '
        'theory, number theory, and combinatorics. Each NP-complete problem is '
        'a cascade endpoint: a problem that was generated by asking whether some '
        'computational task can be performed efficiently, which was in turn '
        'generated by a practical need, which was in turn generated by a previous '
        'solution. The world\'s most consequential open problem in mathematics '
        'emerged from the practical question of whether computers could efficiently '
        'solve scheduling and logistics problems.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The complexity zoo, a catalogue maintained by researchers at the '
        'University of Waterloo: lists over 500 distinct complexity classes, '
        'each defined by different resource bounds (time, space, randomness, '
        'quantum resources, number of rounds of interaction) and each generated '
        'by asking a new computational question. PSPACE (polynomial space), '
        'EXPTIME (exponential time), #P (counting the number of solutions), '
        'BPP (bounded-error probabilistic polynomial time), QMA (quantum '
        'Merlin-Arthur), IP (interactive proofs), each class is a cascade '
        'problem generated by asking a natural extension of the questions that '
        'motivated the previous class. The relationship between these classes '
        '— which ones contain which, which are equal, which are different, '
        'is almost entirely unknown. We are certain that P ⊆ NP ⊆ PSPACE ⊆ '
        'EXPTIME; beyond this basic containment chain, the landscape is open.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The cryptographic cascade is perhaps the most consequential practical '
        'consequence of complexity theory. Modern cryptography, the RSA encryption '
        'algorithm (1977), Diffie-Hellman key exchange (1976), elliptic curve '
        'cryptography (1985), rests on the computational difficulty of certain '
        'problems: factoring large numbers, computing discrete logarithms, '
        'finding square roots modulo composites. The security of these systems '
        'depends on the assumption that these problems are hard, i.e., not in '
        'P. But this assumption is not proven. If P = NP, all of modern '
        'cryptography collapses simultaneously: every public-key cryptographic '
        'system becomes trivially breakable. The entire architecture of internet '
        'security, the HTTPS protocol, digital signatures, online banking, '
        'electronic voting, rests on the unproven assumption that a '
        'seventy-year-old open problem in theoretical computer science has a '
        'specific answer. This is the practical stake of a cascade that began '
        'with Hilbert\'s 1928 Entscheidungsproblem.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'Quantum computing adds yet another cascade layer. Peter Shor\'s 1994 '
        'quantum algorithm for factoring large numbers runs in polynomial time '
        'on a quantum computer, which means that a sufficiently large '
        'quantum computer would break RSA encryption. This result, even though '
        'the required quantum computer does not yet exist at the necessary scale, '
        'has generated a global "post-quantum cryptography" research program '
        'to develop cryptographic systems whose security does not depend on '
        'the hardness of factoring. The National Institute of Standards and '
        'Technology completed a post-quantum cryptography standardisation process '
        'in 2024, selecting four algorithms for standardisation. Each of these '
        'algorithms relies on the hardness of a different problem (lattice '
        'problems, hash functions, coding theory), and for each, the question '
        'of whether a future quantum algorithm can solve it efficiently is open. '
        'The cascade from Hilbert\'s Programme to Turing\'s computability theory '
        'to complexity theory to cryptography to quantum computing to '
        'post-quantum cryptography is now six generations deep and has not '
        'reached a resolution.',
        S['body']))
    story.append(SP(14))

    story.append(SP(22))
    story.append(P('Statistics and the Replication Crisis: The Cascade of Measurement', S['section']))
    story.append(SP(14))
    story.append(P(
        'The cascade in mathematics extends into statistics, whose development '
        'as a formal discipline generated one of the most consequential and '
        'least acknowledged cascades in the history of science: the replication '
        'crisis. Ronald Fisher\'s p-value and significance threshold (p < 0.05), '
        'introduced in his 1925 "Statistical Methods for Research Workers," '
        'was a solution to a genuine problem: how to make defensible quantitative '
        'claims from noisy experimental data. The p-value solved the problem of '
        'arbitrary judgment in data interpretation by providing a standardised '
        'criterion for "statistical significance." The cascade arrived sixty '
        'years later.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The replication crisis, which became widely acknowledged in the early '
        '2010s following large-scale replication studies in psychology (the '
        'Reproducibility Project, 2015), medicine, and economics, revealed '
        'that a substantial fraction of published scientific findings could not '
        'be replicated. The Reproducibility Project replicated 100 psychology '
        'studies published in three leading journals and found that only 36-39% '
        'produced significant results in the replication, compared to 97% in '
        'the original publications. An analysis of clinical trials in cardiovascular '
        'medicine found that 24 of 45 landmark studies published in high-impact '
        'journals between 1990 and 2003 could not be replicated.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The cascade mechanism is the p-value threshold itself. When p < 0.05 '
        'is the criterion for publication, rational researchers have incentives '
        'to conduct multiple tests and report only the significant ones (p-hacking); '
        'to test multiple outcomes and report only the significant ones (outcome '
        'switching); to test a sample and, if the result is marginally non-significant, '
        'add more subjects until it becomes significant (optional stopping). None '
        'of these practices is fraudulent in the obvious sense, each step is a '
        'defensible choice at the time it is made but their cumulative effect '
        'is to produce a scientific literature with a systematic false positive '
        'rate far above the 5% that the p < 0.05 threshold nominally controls. '
        'The solution to the problem of arbitrary judgment in science created the '
        'problem of systematically misleading science.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The remedies proposed and partially implemented — pre-registration of '
        'study designs, registered reports, Bayesian alternatives to frequentist '
        'significance testing, larger required sample sizes are each generating '
        'their own cascades. Pre-registration creates incentives to publish null '
        'results (registered studies that must be published regardless of outcome), '
        'which floods the literature with negative evidence that changes the '
        'base rates in meta-analyses. Bayesian methods require specification of '
        'prior distributions, creating a new arena for subjective judgment, '
        'the problem that the p-value was designed to eliminate. The cascade '
        'from Fisher\'s 1925 solution is now a century old and is still '
        'generating new problems at the methodological frontier of every '
        'quantitative science.',
        S['body']))
    story.append(SP(14))

    # ── Chapter 3 Synthesis ─────────────────────────────────────────────────
    story.append(SP(18))
    story.append(P('Chapter 3 Synthesis: Mathematics as the Purest Cascade', S['section']))
    story.append(P(
        'The mathematical cascade is, in one sense, the purest form of the '
        'phenomenon this book describes. In technology, economics, and medicine, '
        'cascades involve physical, biological, and social systems with their own '
        'unpredictable dynamics. In mathematics, the system is fully deterministic: '
        'a set of axioms and inference rules. There are no unpredictable external '
        'forces, no emergent properties of physical matter, no irrational human '
        'actors. If the cascade could occur anywhere without these complicating '
        'factors, it would happen here. And it does, which is the most powerful '
        'argument that the cascade is fundamental, not contingent on the messiness '
        'of the physical and social world.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The pattern in mathematics is consistent and unmistakable. A problem is '
        'identified. A solution is found, a new concept, theorem, or formalism. '
        'The solution works, resolving the original problem. But the solution also '
        'has consequences: it opens new questions, reveals new problems, requires '
        'new machinery. The new machinery has its own implications. The process '
        'never converges. This is not a failure of mathematics. It is the signature '
        'of a living intellectual enterprise operating under fundamental constraints '
        'imposed by Gödel\'s incompleteness theorems: every formal system powerful '
        'enough to do arithmetic contains truths it cannot prove, and every '
        'extension of the system adds new truths without closing the gap.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The implication for the theory of cascade problems is significant. If the '
        'cascade occurs even in mathematics, where the system is fully deterministic '
        '— then the cascade is not a consequence of complexity or unpredictability '
        'in the material world. It is a consequence of a deeper structural feature: '
        'the impossibility of a finite, consistent description of an infinite, '
        'complex reality. Every solution is a partial map of unmapped territory. '
        'Drawing the map reveals more territory beyond its edges, and that '
        'territory also needs mapping. Progress does not reduce the total space '
        'of unsolved problems; it expands it, because progress reveals dimensions '
        'of the space that ignorance had previously kept hidden.',
        S['body']))
    story.append(SP(14))
    story.append(callout(
        '<b>The Cascade as Epistemic Necessity:</b> In mathematics, cascades arise '
        'not from unpredictability or human error but from the logical structure '
        'of formal systems. Since mathematics, the most rigorous human enterprise '
        '— exhibits the cascade, the phenomenon is not contingent on messy reality. '
        'It is a necessary consequence of the relationship between any finite '
        'problem-solving system and an infinite problem space.',
        S))
    story.append(SP(14))

    # ------------------------------------------------------------------ #
    # EXTENDED: Cryptography and the Quantum Security Cascade              #
    # ------------------------------------------------------------------ #
    story.append(SP(18))
    story.append(P('Cryptography: Mathematics as the Backbone of Digital Trust', S['section']))
    story.append(P(
        'Modern cryptography is built on mathematical structures whose '
        'security rests on unproven computational assumptions. '
        'RSA encryption, the protocol that secures the majority '
        'of digital commerce, banking, and communication, '
        'relies on the assumption that factoring large numbers '
        'is computationally intractable. This assumption has '
        'never been proven; it is an empirical observation '
        'that no classical algorithm discovered in fifty years '
        'of intensive research can factor a 2048-bit number '
        'in feasible time. The security of the global digital '
        'economy rests on a mathematical conjecture.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The cascade from RSA cryptography was quantum computing. '
        'Peter Shor\'s 1994 algorithm demonstrated that a '
        'sufficiently powerful quantum computer could factor '
        'large numbers in polynomial time — breaking RSA '
        'encryption. The quantum computing cascade created '
        'the post-quantum cryptography field: a new branch '
        'of mathematics developing encryption algorithms '
        'resistant to quantum attacks. NIST (the US National '
        'Institute of Standards and Technology) began a '
        'post-quantum standardisation process in 2016, '
        'culminating in the 2022 selection of CRYSTALS-Kyber '
        'and CRYSTALS-Dilithium as primary standards. '
        'The cascade from these new standards is already '
        'visible: their mathematical complexity makes them '
        'computationally more expensive than RSA, creating '
        'performance challenges for constrained devices '
        '(IoT sensors, smart cards, embedded systems). '
        'The solution to the RSA quantum vulnerability '
        'generates new hardware and performance cascades '
        'before the quantum threat has even fully materialised.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The "harvest now, decrypt later" threat adds a temporal '
        'dimension to the quantum security cascade. Adversarial '
        'state actors are currently collecting encrypted '
        'communications with the intention of decrypting them '
        'when sufficiently powerful quantum computers become '
        'available — anticipated by some analysts within '
        '10-15 years. This means that communications encrypted '
        'today with RSA may be readable by adversaries in the '
        '2030s. Data with a long-term sensitivity horizon, '
        'intelligence sources, diplomatic communications, '
        'medical records, financial data is at risk from '
        'a cascade that has not yet fully arrived. '
        'The cascade of quantum computing on cryptography '
        'is unusual in that its primary effect is retroactive: '
        'it will compromise past communications rather than '
        'future ones.',
        S['body']))
    story.append(SP(14))
    story.append(callout(
        '<b>The "Harvest Now, Decrypt Later" Cascade:</b> Adversaries '
        'collecting today\'s encrypted data for future quantum decryption '
        'create a cascade with a retroactive temporal structure, the '
        'harm occurs years after the encryption, when the encrypted data '
        'is finally readable. This violates the cascade monitoring '
        'assumption that harm can be observed in time to trigger '
        'corrective action.',
        S))
    story.append(SP(14))
    story.append(fig_to_image(fig_solution_problem_race(), w=5.5*72, h=3.6*72))
    story.append(P(
        'Figure 1.3 (Illustrative): The widening gap between solutions deployed and cascade '
        'problems generated (1900–2024, log scale). Values are schematic orders of magnitude '
        'capturing the qualitative shape of the relationship, the exponential divergence '
        'is the empirical claim; the precise coordinates are not. The shaded area represents '
        'the compounding deficit that has outpaced our collective addressing capacity.',
        S['caption']))
    story.append(SP(14))
    story.append(PageBreak())
    return story
