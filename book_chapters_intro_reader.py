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
        'medicine, from finance to public policy. The book that follows is '
        'what happened when I started looking for that same pattern '
        'outside the codebase.',
        S['preface']))
    story.append(SP(12))
    story.append(P(
        'What began as a software-engineering observation quickly became a '
        'comparative question. Was Mariam\'s remark a feature of large software '
        'systems specifically, or was it a specific instance of a more general '
        'pattern? Antibiotic resistance, foreseen by Fleming as early as 1945 '
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
        '<i>Ahmed Hafdi<br/>Kenitra, Spring 2025</i>',
        S['epig_attr']))
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
        ('body0', """In 1880s colonial India, the British administration in Delhi grew alarmed by
the city's population of venomous cobras. The snakes were a genuine public health
problem, people were dying. The solution seemed obvious: offer a cash bounty for
every dead cobra delivered to the colonial offices. Citizens would be incentivised
to hunt the snakes, the population would decline, and the city would be safer.
The logic was impeccable. The outcome was a catastrophe."""),
        ('body', """Within months, enterprising Delhiites had discovered something the
administrators had not anticipated: it was far easier to breed cobras than to hunt wild
ones. Cobra farms sprang up across the city. Dead snakes arrived at the colonial offices
by the basketful. The bounty payments flowed. The administrators, seeing the numbers
of delivered cobras climb, congratulated themselves on the program's success."""),
        ('body', """Then the colonial government, realising what was happening, cancelled the
bounty. The cobra farmers, now holding thousands of suddenly worthless snakes, did the
rational thing: they released them. Delhi ended up with significantly more cobras than
it had started with. The solution had created a problem larger than the one it was
designed to solve."""),
        ('body', """This story (known today as the Cobra Effect) has become a parable for
a phenomenon so common that it spans every domain of human endeavour, from the most
abstract reaches of pure mathematics to the most practical corridors of public policy.
It is the phenomenon this book sets out to explain: the systematic, mathematically
predictable tendency of solutions to generate more problems than they resolve."""),
        ('body', """The Cobra Effect is not a story about stupidity. The British administrators
were not fools; they were applying standard economic incentive theory, which was and
remains perfectly sound. The failure was not in the intelligence of the individuals
involved but in the structure of the system they were intervening in. They were thinking
linearly in a world that responds non-linearly. They were solving a problem as if it
existed in isolation, when it existed within a web of incentives, actors, and feedback
loops that immediately reorganised itself around their intervention."""),
        ('body', """This is the central insight of this book: the problem is not the solution.
The problem is the way we design solutions, in isolation, without accounting for the
system that will receive them, without asking what the system will do in response."""),

        ('section', 'A Pattern Across All of Human Knowledge'),
        ('body0', """The Cobra Effect is entertaining because it is exotic. But it is far from
unique. Consider what happens when you trace the consequences of humanity's greatest
innovations across time:"""),
        ('body', """The automobile solved the problem of slow, expensive horse-based transport.
It created traffic congestion, air pollution that kills approximately 4.2 million people
annually (WHO, 2023), urban sprawl that has consumed billions of acres of farmland,
and a global dependency on fossil fuels that now threatens the planet's climate. These
were not inevitable consequences of "progress"; they were consequences of designing
a transport solution without accounting for the system it would transform."""),
        ('body', """The internet solved the problem of expensive, slow information exchange.
It created surveillance capitalism, cybercrime costing the global economy $8 trillion
annually (Cybersecurity Ventures, 2023), mass misinformation that now threatens
democratic institutions, and digital addiction affecting an estimated 400 million people
worldwide. Again: not inevitable. Structural."""),
        ('body', """Antibiotics solved the problem of bacterial infection. They created
antibiotic-resistant superbugs that now directly kill an estimated 1.27 million people a
year (and contribute to nearly 5 million more), with one widely cited projection putting
the toll at 10 million a year by 2050. The O'Neill Review on
Antimicrobial Resistance (2016), commissioned by the British government, described
this as "an apocalyptic scenario" caused directly by the overuse of the very drugs
that represented medicine's greatest triumph."""),
        ('body', """In every case, the solution was real. Automobiles genuinely enabled
mobility. The internet genuinely democratised information. Antibiotics genuinely saved
hundreds of millions of lives. The issue is not that these innovations were mistakes.
The issue is that each of them entered a complex system, and the system responded by
generating new problems, problems that were in many cases structurally guaranteed
by the very nature of the intervention."""),

        ('section', 'What This Book Argues'),
        ('body0', """This book makes three claims, each more specific than the last."""),
        ('body', """<b>First claim:</b> The tendency of solutions to create new problems is
not accidental, cultural, or political. It is a deep structural tendency of complex
systems. When you introduce a handful of solutions into a system whose components
interact, the number of potential new problems does not just rise — the possible
combinations roughly double with each new solution added. This is not merely a
metaphor; it follows from ordinary counting and network theory, as Chapter 10
explains in plain terms. How many of those potential problems become real depends
on how many interactions turn harmful — and this book argues the fraction is never
zero. The
underlying reasoning does not care whether the solution is a government policy, a
software feature, a medical treatment, or a physical theory. The cascade is
structural."""),
        ('body', """<b>Second claim:</b> This mathematical reality is systematically invisible
to human cognition. We are wired, by evolution, culture, and institutional incentive,
to celebrate solutions and discount their future costs. We experience the benefit of a
solution immediately and locally. We experience its cascade of new problems later,
diffusely, and in contexts that rarely feel connected to the original intervention.
This temporal and cognitive gap is not a bug in human thinking that better education
can fix; it is a deep feature of how we process complex causality. Chapter 2 examines
the psychology in detail."""),
        ('body', """<b>Third claim:</b> The paradox can be managed, not eliminated, but
managed. There exist design principles, analytical tools, and institutional structures
that can significantly reduce the cascade rate. Ecosystems that are designed for
internal compatibility — where each new solution is evaluated not just for its primary
effect but for its interactions with existing solutions — generate problems at a slow,
sustainable rate, rather than the explosive rate that doubles every time a new solution
is added. The difference is the difference between a system that collapses under its
own complexity and one that sustains itself indefinitely. Part IV of this book is about
making that transition."""),

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
    story.append(P("The Delhi debacle was no one-off. Reconstructed from colonial records and the scholarship of economists Horst Siebert and Werner Troesken, it stands at the head of a series in which the same structure recurs in complete institutional isolation. In 1902, French colonial authorities in Hanoi, facing a serious problem with rat-borne disease in the newly constructed European quarter, instituted a bounty payable on the production of rat tails, a scheme chosen because it was less gruesome than requiring whole carcasses. The incentive was carefully calculated, the sanitary motivation was genuine, and the administrative logic was identical to the Delhi cobra program. Within weeks, city workers began finding rats in the sewers that had been deliberately caught and had their tails removed before being re-released. The rats, left intact and reproductively active, continued their population growth unabated. Worse, when the scheme was eventually discovered and terminated, rat populations in affected neighborhoods were found to have increased substantially — rat farmers had been releasing surplus animals just as the Delhi cobra farmers had. The historian Michael Vann, in his definitive account of the program, documents the memo in which the colonial director of public health noted with evident frustration that the city now contained 'an abundance of tailless rats', a phrase that has since become a minor classic of bureaucratic understatement.", S['body']))
    story.append(P("The Prague dog-tail bounty of the early twentieth century, though less well documented, follows the same structure. Municipal authorities, attempting to control the population of stray dogs, offered a bounty on dog tails. Entrepreneurial citizens discovered that a living dog could provide a continuous stream of tail-regrowth income if handled correctly, though in the case of dogs, of course, tails do not regenerate, so the scheme collapsed more quickly when authorities noticed the disproportion between tails delivered and stray-dog population reductions. What is remarkable about these three cases (Delhi, Hanoi, Prague) is not merely that they follow the same pattern but that they follow it in complete institutional isolation. There is no evidence that the Hanoi administrators knew of the Delhi failure, or that the Prague authorities knew of Hanoi. The cascade recurred not because bad information spread, but because the structural incentive created by the bounty mechanism is always and everywhere exploitable in the same way. The fault is not in the administrators. It is in the architecture of the solution.", S['body']))
    story.append(P("The most modern equivalent comes from Cambodia in the early 2010s. The Cambodian government and several international NGOs, working to clear unexploded ordnance (UXO): landmines, cluster munitions, and artillery shells remaining from the Vietnam War era — instituted various reward programs for the discovery and reporting of live ordnance. In at least two documented instances, villagers in rural provinces began extracting already-neutralised ordnance from storage facilities and re-presenting it as newly discovered material, collecting multiple payments. In one case investigated by a Mines Advisory Group field team in 2013, a cache of 'newly discovered' anti-personnel mines was traced to a legitimate disposal site three kilometers away. The incentive to game the reporting system was not greed in the pejorative sense, in a province where average annual household income was under five hundred dollars, the per-item payments represented transformative sums. The structural logic was identical to Delhi in 1880: well-intentioned administrators, facing a genuine and deadly problem, created an incentive that the local population rationally gamed. The solution generated a problem of its own: a reporting ecosystem polluted with false positives, compromising the data on which future UXO clearance efforts depended. The administrators of Delhi, Hanoi, Prague, and Phnom Penh were not fools. They were humans operating in complex systems with tools designed for simple ones.", S['body']))
    story.append(callout("<b>The Cobra Effect Template:</b> A genuine problem. A rational incentive-based solution. An agent population that optimises for the incentive rather than the underlying goal. Cancellation of the incentive. A problem larger than the original. This five-step template repeats with remarkable consistency across cultures, centuries, and domains.", S))

    story.append(SP(18))
    story.append(P("The Central Claim, Stated Four Ways", S['section']))
    story.append(P("This book has a single central argument. It can be stated simply, historically, mathematically, or philosophically. The level of precision increases with each formulation, but the argument is the same argument. The reader is invited to choose the formulation that is most persuasive and return to the others after the evidence of subsequent chapters has had its effect.", S['body0']))
    story.append(P("The <b>colloquial formulation</b> is: every solution creates new problems, and the problems grow faster than the solutions. This is the version that most people have experienced directly, in their software, their organisations, their governments, their bodies. The new feature that creates three new bugs. The regulation that creates the loophole industry. The medication that requires the medication to manage its side effects. It feels like a law of life. This book argues that it is a strong and consistent regularity — motivated by the mathematics of complex systems and confirmed by the evidence of every major domain of human endeavour.", S['body']))
    story.append(P("The <b>historical formulation</b> is: across every major domain of human endeavour surveyed in this book, the ratio of problems generated to problems solved by any given solution is greater than one, and this ratio increases over time as systems become more interconnected. This formulation is testable, and the test is what occupies Part II. Mathematics, medicine, economics, technology, ecology, law, and geopolitics each present their own evidence. The evidence is not cherry-picked from outliers. It emerges from the major, celebrated, paradigm-defining solutions in each field: the solutions we point to as our greatest achievements. The cascade is not generated by our failures. It is generated by our successes.", S['body']))
    story.append(P("The <b>mathematical formulation</b> is: in any complex system whose solutions can interact with each other, the number of potential problem-generating combinations roughly doubles with every new solution added, while the number of solutions itself grows only linearly with time. Chapter 10 unpacks why. The essential point is that when solutions interact — when a new solution can combine with any existing solution, or any pair, or any triple — the number of potential problem-generating combinations explodes, while the number of solutions we can actually deploy grows only at the pace of human effort. The gap between the rate at which problems can be generated and the rate at which solutions can be deployed is the central quantitative claim of this book. It does not depend on the quality of solutions, the intelligence of their designers, or the resources available for implementation. It depends only on the structure of interaction in complex systems.", S['body']))
    story.append(P("The <b>philosophical formulation</b> is: the act of intervening in a complex system is itself a perturbation of that system, and perturbations in complex systems generate cascades that exceed the scope of the intervention. This is the deepest formulation because it locates the source of the cascade not in the quality of the intervention but in the nature of complex systems themselves. A complex system is, by definition, one in which components interact non-linearly and in which the interactions produce emergent properties not predictable from the properties of the components. When you intervene in such a system (when you add a new component or modify an existing one) the system responds as a whole. The response includes effects in domains you were not targeting, through mechanisms you did not model, at timescales you did not consider. The intervention does not just solve the problem it was designed to solve. It perturbs the entire system. And the perturbation of a complex system is always, in principle, unbounded in its effects.", S['body']))
    story.append(P("These four formulations reinforce each other. The colloquial formulation captures the phenomenology. This is what it feels like from the inside. The historical formulation provides the empirical support. This is what the evidence shows. The mathematical formulation provides the theoretical foundation. This is why it must be so. The philosophical formulation provides the deepest explanation. This is what it means about the nature of knowledge and action in a complex world. A reader who finds one formulation unsatisfying is invited to try another. The argument does not stand or fall on any single version of itself.", S['body']))

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
    story.append(P("<b>Chapter 13 (A New Philosophy of Innovation)</b> closes Part IV by examining the institutional and educational changes — in government, industry, academia, and professional practice — that would be required to embed cascade awareness in decision-making at the scale at which the problem operates. <b>Chapter 14 (The Case Against This Book)</b> then turns the argument on itself, stating the strongest objections to the cascade thesis — selection bias, the overwhelmingly positive ledger of progress, unfalsifiability, and the risk that cascade thinking licenses harmful inaction — and judging honestly how much of the book survives them. A Conclusion and a set of appendices (a taxonomy of cascade types, worked case studies, checklists, and a glossary) complete the book. The cascade is among the most consequential and least recognised challenges of our era, and meeting it would require not new technology or new resources, only a more honest accounting of the costs of what we already do.", S['body']))

    story.append(SP(18))
    story.append(P('A Message for Leaders, Founders, and Policymakers', S['section']))
    story.append(P(
        'This book was written for everyone who has ever tried to make '
        'something better. That is a wide audience. But there is a subset '
        'of that audience for whom the stakes of the cascade argument are '
        'particularly high, because the decisions they make operate at a '
        'scale where even a marginal improvement in cascade awareness '
        'translates into millions of lives and trillions of dollars. '
        'To that subset, the heads of state, the CEOs, the central '
        'bank governors, the platform architects, the generals, the '
        'cabinet ministers, the WHO directors, the UN secretaries-general '
        '— this section is addressed directly.',
        S['body0']))
    story.append(P(
        'If you are a head of government, you will recognise this scenario: '
        'your predecessor identified a genuine crisis, deployed a bold '
        'solution, and left office celebrated. You inherited the cascade. '
        'The solution is entrenched; its constituency is powerful; '
        'its costs are diffuse and politically difficult to attribute. '
        'You are managing the aftermath of someone else\'s triumph, '
        'and your management of that aftermath will itself generate '
        'the cascade that your successor inherits. This is not a '
        'failure of governance. It is the structural condition of '
        'governance in complex systems. Every major policy, '
        'from the post-war welfare state to structural adjustment '
        'programmes, from the War on Terror to COVID-19 lockdowns, '
        'follows this pattern. The question is not whether your '
        'solutions will generate cascades. They will. The question '
        'is whether you have the analytical framework to anticipate '
        'them, and the institutional architecture to manage them '
        'when they arrive.',
        S['body']))
    story.append(P(
        'If you are a CEO or founder, the cascade is already your daily '
        'reality. Every product launch is a cascade event. The feature '
        'that delights your customers creates the security vulnerability '
        'your security team will spend six months closing. The efficiency '
        'gain from automating your supply chain creates the single point '
        'of failure that your operations team will panic about when a '
        'port closes or a pandemic hits. The platform you build to connect '
        'people creates the surveillance infrastructure that regulators '
        'will eventually investigate. You live this already but '
        'without a name for it, without a framework for anticipating it, '
        'and without the vocabulary to communicate the cascade risk to '
        'your board before it becomes a crisis. This book gives you '
        'all three. Steve Jobs designed the most successful consumer '
        'product in history. He did not design the attention economy, '
        'the App Store monopoly litigation, or the e-waste mountain '
        'that his product line would generate. These were the cascades '
        'of his genius. His successors now manage them. They would '
        'have been better positioned to do so if cascade theory had '
        'been part of Apple\'s strategic vocabulary from the beginning.',
        S['body']))
    story.append(P(
        'If you are a policymaker, regulator, or international official, '
        'the cascade argument has a specific and urgent implication: '
        'the timeline of political accountability does not match the '
        'timeline of cascade development. A policy deployed in Year 1 '
        'generates its primary benefits by Year 3, within the electoral '
        'cycle. Its cascade costs emerge by Year 7 to Year 15, after '
        'the architects have left office and the political credit for '
        'the solution has been fully collected. The architects of '
        'financial deregulation in the 1980s and 1990s were celebrated '
        'as champions of growth and efficiency. The cascade arrived '
        'in 2008, long after most of them had retired. The architects '
        'of antibiotic proliferation in the 1950s and 1960s were '
        'celebrated as saviours of millions of lives, which they '
        'genuinely were. The resistance cascade arrived in the 2000s. '
        'This temporal mismatch is not a moral failing of individual '
        'policymakers. It is a structural feature of complex system '
        'response. The correct institutional response is not to blame '
        'individuals but to build sunset clauses, mandatory impact '
        'reviews, and cascade monitoring into policy architecture, '
        'so that the cascade assessment continues after the '
        'policy architect has left the room.',
        S['body']))
    story.append(callout(
        '<b>The Leader\'s Cascade Imperative:</b> The most consequential '
        'question a leader can ask before deploying any major solution is '
        'not "Will this work?"; it will work, or it would not be '
        'proposed. The question is: "What will the system do in response, '
        'and does that response create problems larger than the ones '
        'I am solving?" This question is rarely asked systematically '
        'before deployment. It is always asked, with great urgency '
        'and far greater cost, after the cascade arrives.',
        S))
    story.append(SP(14))
    story.append(P(
        'The good news (and there is genuine good news in this book) '
        'is that cascade awareness is a learnable skill, cascade '
        'assessment is a practicable discipline, and cascade-resistant '
        'design is achievable with existing tools and knowledge. '
        'The leaders who understood this before their peers did not '
        'avoid cascades entirely (no one does) but they managed them '
        'more effectively, more cheaply, and with less human cost. '
        'The architects of the Montreal Protocol managed the ozone '
        'depletion cascade. The engineers behind the coordinated '
        'disclosure standard managed the cybersecurity cascade. '
        'The WHO\'s Intensified Eradication Programme managed the '
        'smallpox vaccine cascade. None of them eliminated the cascade. '
        'All of them contained it. That is the standard of success '
        'available to leaders who take cascade awareness seriously. '
        'It is a significantly better standard than the alternative.',
        S['body']))

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
        ('section', 'The Three Mechanisms'),
        ('body0', """Before we can understand why solutions create problems, we need to
understand how they create problems. Three mechanisms are at work, each operating at a
different scale and timescale. Together, they produce the cascade. Individually, each
one is manageable. Combined (which is how they always appear in complex systems) they
produce the kind of compounding problem growth that no amount of well-intentioned fixing can reliably outrun."""),

        ('body', """The first mechanism is <b>individual complexity</b>. Every solution
introduces new complexity into its operating environment. A new drug requires a new
production chain, a new regulatory pathway, new prescribing guidelines, new
pharmacist training, new patient monitoring protocols, and new drug interaction
databases. A new software feature requires new documentation, new test cases, new
edge-case handling, new compatibility checks with every existing feature, and new
security review. A new government regulation requires new enforcement mechanisms, new
reporting infrastructure, new legal interpretation frameworks, and new bureaucratic
processes. Each of these complexity additions creates its own surface area for
new problems."""),

        ('body', """This is not a design failure. It is the nature of solutions. A solution
that introduces zero complexity is a solution that does nothing. The complexity is
the mechanism by which the solution achieves its effect. The price is that complexity
is always a two-sided ledger: it enables the intended function, and it creates new
failure modes that did not exist before the solution arrived."""),

        ('body', """The second mechanism is <b>interaction effects</b>. Solutions do not
exist in isolation; they exist alongside other solutions. When you introduce solution
A into a system that already contains solutions B, C, and D, you create not just the
direct effects of A but the interaction effects A×B, A×C, A×D, and potentially
A×B×C, A×B×D, A×C×D, and A×B×C×D. Each new arrival creates a number of potential
interaction effects that doubles with every existing solution. Most of these
interactions are benign. But in complex systems, even a small percentage of harmful
interactions produces a large
absolute number of new problems, because n is always growing."""),

        ('body', """The drug interaction database maintained by the US National Library of
Medicine currently tracks interactions among more than fourteen hundred approved
medications. The number of possible pairwise interactions alone is close to a
million. The number of three-way interactions is over four hundred million. No
human physician can hold this space in mind. No clinical trial can test it. And
every new drug approval expands it further. This is interaction cascade in its
purest form."""),

        ('body', """The third mechanism is <b>network amplification</b>. Modern solutions
operate in highly connected networks (biological, social, digital, economic) that
transmit both the benefits and the problems of any intervention with extraordinary
speed and reach. A financial instrument created in a single bank in New York can,
within eighteen months, trigger a global economic crisis affecting hundreds of millions
of people who have never heard of the instrument. A social media algorithm tweak made
by an engineer in Menlo Park can, within weeks, shift the political discourse of
dozens of nations. A new respiratory pathogen arising in a single wet market can,
within four months, shut down every economy on earth."""),

        ('body', """Network amplification means that the problems generated by a solution
are not confined to the system the solution was designed to address. They propagate
along every network connection to every adjacent domain. The automobile was designed to
solve transport. Its cascade problems penetrated urban planning, atmospheric chemistry,
geopolitics (oil dependency), public health (sedentary lifestyles, air pollution), and
global economics. The internet was designed for information exchange. Its cascades now
pervade democracy, mental health, criminal justice, national security, and the economics
of attention. This propagation is not metaphorical; it follows the mathematical laws
of network diffusion, with amplification proportional to network connectivity."""),

        ('section', 'Murphy\'s Law Is Not a Joke'),
        ('body0', """Most people treat Murphy's Law — "Anything that can go wrong will go
wrong", as a sardonic joke, a piece of folk wisdom too cynical to take seriously in
an age of engineering precision. They are wrong. Murphy's Law is a mathematical
observation disguised as humour. It is a special case of the cascade framework, and it
is quantitatively supported by decades of reliability engineering data."""),

        ('body', """Edward Murphy Jr. formulated his law in 1949 while working on US Air
Force deceleration experiments. A colleague had connected a set of sensors in the only
possible wrong configuration. Murphy observed that in a system with enough components,
every possible failure mode will eventually be realised, because the probability of
at least one failure approaches certainty as the number of components grows. This is
not pessimism. It is probability theory."""),

        ('body', """If each component of a system has even a small chance of failure, and
the components fail independently of one another, then the probability that the whole
system works perfectly drops sharply as components are added. A system of a hundred
components, each with a 1% failure rate, has under a 40% chance of working perfectly
at any moment. A system of a thousand components has effectively no chance at all.
The system is virtually certain to fail somewhere. Adding solutions — which means
adding components — does not escape this logic. Each new solution multiplies the
failure surface."""),

        ('body', """The same logic applies to social and policy systems, though the
"components" are incentives, actors, and feedback loops rather than mechanical parts.
When the British administrators introduced the cobra bounty, they added a new
incentive component to the colonial economy of Delhi. That component interacted with
existing components, the entrepreneurial instincts of Delhiites, the economics of
animal husbandry, the distance between government offices and the street, in ways
they had not modelled. The failure was not in their competence. It was in the
combinatorial complexity of the system they were intervening in."""),

        ('section', 'The Exponential Trap'),
        ('body0', """The most important fact about cascade problems is not that
they exist (every thoughtful person suspects they do) but how quickly the <i>ways</i> they
can arise pile up. Linear growth is manageable. Quadratic growth is uncomfortable. The
near-doubling growth of <i>possible</i> interactions is the kind that overwhelms — and even a
small, fixed fraction of it turning harmful is enough to outrun our fixes."""),
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
that a non-trivial fraction will not be — and a small fraction of a doubling-with-each-
step number is, very quickly, a large number of real problems. This is the structural
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

        ('section', 'Comparison: Murphy, Merton, Jevons, and Streisand'),
        ('body0', """The cascade framework is not born in isolation. It belongs to a family
of related observations made across different disciplines over the past century and a
half. Understanding how these related ideas connect and differ helps to clarify what
is distinctive about the cascade framework presented here."""),

        ('body', """<b>Merton's Unintended Consequences (1936):</b> The American sociologist
Robert K. Merton was the first to provide a systematic academic treatment of the
phenomenon. In his landmark 1936 paper in the <i>American Sociological Review</i>,
Merton identified five sources of unintended consequences: ignorance, error, immediacy
of interest (short-term thinking), basic values that mandate certain actions regardless
of consequences, and self-defeating prophecies. Merton's framework is sociological —
it explains the human factors that make unintended consequences likely. The cascade
framework presented here is structural; it explains why
unintended consequences are not merely likely but extremely hard to avoid in complex systems,
largely regardless of the quality of human decision-making."""),

        ('body', """<b>Jevons Paradox (1865):</b> The economist William Stanley Jevons
observed that improvements in the efficiency of coal-burning steam engines, rather
than reducing coal consumption, actually increased it, because cheaper operation made
coal-based industry more economically attractive, expanding its scale. This is a
specific instance of cascade thinking: the solution (efficiency) creates a demand-side
problem (rebound effect) that swamps the supply-side benefit. The Jevons Paradox
applies wherever efficiency improvements lower the cost of an activity, which is most
of the time. It is examined in detail in Chapter 6."""),

        ('body', """<b>The Streisand Effect:</b> In 2003, the singer Barbra Streisand
attempted to suppress aerial photographs of her Malibu home by suing a photographer.
Before the lawsuit, the photograph had been downloaded six times. After the lawsuit —
which drew massive media attention to the very image she sought to suppress; it was
downloaded over 420,000 times in a month. The Streisand Effect is a cascade problem
in the domain of information: the solution (suppression) amplifies the very problem
(publicity) it was designed to solve. The network amplification mechanism makes this
not just possible but predictable."""),

        ('body', """What unites all of these observations is a single structural feature:
the solution modifies the system in a way that creates new problems, and the new
problems are often <i>caused by the same mechanism that makes the solution work</i>.
The antibiotic kills bacteria by disrupting their cell wall synthesis, and exactly
this selective pressure drives the evolution of resistant strains. The cobra bounty
creates an economic incentive to eliminate cobras, and exactly this incentive makes
cobra breeding profitable. The efficiency improvement makes coal cheaper to use — and
exactly this cost reduction expands the market for coal. The cascade is built into the
solution at the level of mechanism, not at the level of implementation error."""),

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
    story.append(P('Why Previous Theories Are Insufficient', S['section']))
    story.append(SP(14))
    story.append(P(
        'The cascade theory is not the first attempt to systematise the observation '
        'that solutions generate problems. Several well-developed frameworks exist, '
        'each of which captures a piece of the phenomenon. Understanding why each '
        'is insufficient (and what the cascade theory adds) is essential for '
        'establishing the theory\'s contribution rather than its repetition.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'Systems dynamics, developed by Jay Forrester at MIT in the 1950s and '
        'popularised by the Club of Rome\'s "Limits to Growth" (1972), models '
        'complex systems as networks of stocks, flows, and feedback loops. It '
        'correctly identifies that interventions in complex systems generate '
        'unexpected dynamics through feedback. The standard systems dynamics '
        'approach, however, typically models a fixed system structure and '
        'examines how different policies affect that structure\'s dynamics. '
        'The cascade framework adds to systems dynamics by addressing a question '
        'it does not ask: what happens to the complexity of the system structure '
        'itself as the number of solutions deployed into it grows? Systems '
        'dynamics takes the structure as given; cascade theory explains how the '
        'structure evolves.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'Complexity theory, in the tradition of Santa Fe Institute researchers '
        'Stuart Kauffman, W. Brian Arthur, and others, models complex adaptive '
        'systems and their emergent behaviours. Complexity theory correctly '
        'identifies that solutions operating in complex adaptive systems generate '
        'emergent effects that cannot be predicted from the properties of the '
        'components. Its primary contribution is the concept of emergence: '
        'properties that arise at the system level from component-level '
        'interactions. The cascade framework identifies a specific category of '
        'emergent property (cascade problems) and offers a quantitative estimate '
        'of its growth rate. Where complexity theory says "emergent '
        'properties are possible and sometimes surprising," cascade thinking says '
        '"cascade problems are pervasive and can grow combinatorially."',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'Risk management, in the tradition of financial economics and engineering '
        'reliability theory, addresses the probability and magnitude of adverse '
        'outcomes. It uses techniques like fault tree analysis, failure mode '
        'and effects analysis, and value-at-risk to quantify the risks of '
        'specific systems or portfolios. Risk management correctly identifies '
        'that adverse outcomes should be planned for. Its primary limitation, '
        'from the cascade perspective, is scope: it assesses the risks of the '
        'system as designed, not the risks generated by the system\'s interaction '
        'with other solutions in the ecosystem. A drug\'s risk management '
        'assessment evaluates the risk of adverse events in the treated patient '
        'population; it does not evaluate the risk of the drug\'s prescribing '
        'incentive structure generating an epidemic of misuse. The cascade '
        'framework extends risk management beyond the system boundary to the '
        'full ecosystem of interactions.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The cascade theory\'s unique contribution is the combination of three '
        'elements that no previous framework provides simultaneously: (1) an '
        'explicit structural argument for why cascade problem generation can grow '
        'combinatorially, far faster than the number of deployed solutions, largely '
        'regardless of the quality of individual solutions; (2) a quantitative framework (the CRI) for '
        'estimating cascade risk before deployment; and (3) an explicit '
        'treatment of the ecosystem, the full set of existing solutions and '
        'their interactions, as the determinant of cascade severity. This '
        'combination allows the theory to do what its predecessors cannot: '
        'predict, before deployment, not just whether a solution will fail '
        'but how the failure will propagate and at what rate.',
        S['body']))
    story.append(SP(14))

    # ── Chapter 1 extended ─────────────────────────────────────────────────
    story.append(SP(18))
    story.append(P('Five Historical Cases: The Cascade in Four Centuries', S['section']))
    story.append(P(
        'The mathematical argument above is most convincing when grounded in '
        'historical evidence. The following five cases are drawn from different '
        'centuries, different domains, and different types of solution, '
        'agricultural, biological, technological, financial, and regulatory. '
        'Each demonstrates the full cascade structure: an original problem, '
        'a genuine solution, a first-order cascade, and a second-order cascade '
        'that is still active. Together they establish that the cascade is '
        'not a modern phenomenon, not a feature of capitalism or technology, '
        'and not a consequence of insufficient intelligence in the solution '
        'designers. It is a permanent feature of problem-solving in complex systems.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        '<b>The Enclosure Movement (England, 1750-1830).</b> The problem: '
        'common land farming generated the "tragedy of the commons" (Hardin\'s '
        'formulation, but the phenomenon predates it) — collective overuse of '
        'shared pasture. The solution: enclosure, converting common land to '
        'privately owned fields, which would be managed by profit-motivated '
        'owners who internalised the costs of overuse. The solution worked '
        'for its primary objective: enclosed land was farmed more productively, '
        'contributing to the agricultural revolution that fed England\'s growing '
        'industrial population. The first-order cascade: displacement of hundreds '
        'of thousands of rural workers who had depended on common land access, '
        'driving them into industrial cities that were entirely unprepared '
        'for their arrival, generating the squalor, disease, child labour, '
        'and political unrest of early industrial urbanism. The second-order '
        'cascade: the political response to industrial urbanism (Chartism, '
        'trade unionism, eventually the Labour Party) restructured British '
        'politics for the next century. The solution to the tragedy of the '
        'commons created the conditions for the tragedy of industrial capitalism.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        '<b>Pasteur\'s Germ Theory (France, 1857-1877).</b> The problem: '
        'infectious diseases killed at rates that seemed inevitable, because '
        'they were attributed to miasmas (bad air) or spontaneous generation '
        'of disease within the body. Pasteur\'s demonstration that specific '
        'microorganisms cause specific diseases transformed medicine: it enabled '
        'the development of vaccines (rabies, anthrax), antiseptic surgical '
        'technique (Lister), and eventually antibiotics. The first-order cascade: '
        'germ theory\'s focus on specific microbial pathogens as the cause '
        'of disease created a medical model that was exquisitely effective '
        'at treating acute infectious disease and systematically less attentive '
        'to the chronic, multi-factorial conditions: cardiovascular disease, '
        'metabolic syndrome, cancer, depression, that would become the '
        'dominant causes of morbidity and mortality as infectious disease '
        'mortality declined. The second-order cascade: the biomedical model\'s '
        'dominance generated a pharmaceutical industry optimised for single-target '
        'drug development (the "magic bullet" paradigm), which created the '
        'drug-drug interaction problem, the antibiotic resistance crisis, and '
        'the marginalisation of preventive and environmental medicine. '
        'Pasteur\'s solution to infectious disease is the founding cascade '
        'of modern medicine.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        '<b>The Haber-Bosch Process (Germany, 1909-present).</b> The problem: '
        'nitrogen fixation, converting atmospheric nitrogen to ammonia for '
        'fertiliser was the binding constraint on global food production. '
        'Without fixed nitrogen, crops cannot grow beyond what soil bacteria '
        'can provide. By 1900, the world\'s population was approaching the '
        'Malthusian limit imposed by this constraint. Fritz Haber and Carl '
        'Bosch\'s industrial nitrogen fixation process, commercialised from '
        '1913, broke the Malthusian constraint: synthetic fertiliser enabled '
        'agricultural yields that could feed a global population of eight '
        'billion people. Without the Haber-Bosch process, demographers estimate '
        'that approximately half the world\'s current population could not '
        'be supported by available agricultural land. The first-order cascade: '
        'nitrogen runoff from synthetic fertiliser use has created over 400 '
        'coastal "dead zones" globally, including the 22,000 square kilometre '
        'dead zone in the Gulf of Mexico, where excess nitrogen drives algal '
        'blooms that consume all dissolved oxygen and kill marine life. '
        'The second-order cascade: the global population explosion enabled '
        'by the Haber-Bosch process has itself generated cascades in resource '
        'depletion, land use change, and climate forcing that are among the '
        'most consequential challenges of the twenty-first century. The '
        'solution to the problem of feeding humanity created the conditions '
        'for the challenge of sustaining eight billion people on a finite '
        'planet.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        '<b>The Glass-Steagall Repeal (United States, 1999).</b> The problem: '
        'the Glass-Steagall Act of 1933, which separated commercial banking '
        '(taking deposits, making loans) from investment banking (underwriting '
        'securities, trading for own account), was seen by 1990s financial '
        'institutions as an inefficiency that prevented American banks from '
        'competing with European universal banks. The Gramm-Leach-Bliley Act '
        '(1999) repealed the Glass-Steagall separation, allowing the combination '
        'of commercial and investment banking that had been prohibited for '
        '66 years. The solution worked for its stated purpose: US financial '
        'institutions could now operate as universal banks, competing more '
        'effectively in global markets. The cascade: the combination of '
        'deposit-taking (which is implicitly guaranteed by the federal government) '
        'with proprietary trading (which is inherently speculative) created '
        'an incentive structure in which financial institutions could privatise '
        'gains from trading and socialise losses through the deposit insurance '
        'backstop. This moral hazard was the core mechanism of the 2008 '
        'financial crisis: banks took on excessive risk knowing that the '
        'government would not allow large financial institutions to fail. '
        'The solution to the Glass-Steagall inefficiency created the '
        'conditions for the largest financial cascade in modern history, '
        'nine years after its passage.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        '<b>The Bluetooth Standard (1998-present).</b> The problem: '
        'short-range wireless communication between devices required '
        'proprietary, incompatible radio protocols, creating consumer friction '
        'and limiting the market for wireless peripherals. The Bluetooth '
        'standard, developed by Ericsson and five partner companies in 1994-1998, '
        'solved this problem by creating a universal wireless protocol that '
        'any manufacturer could implement. The solution was extraordinarily '
        'successful: approximately five billion Bluetooth-enabled devices '
        'are shipped annually as of 2024. The first-order cascade: Bluetooth '
        'created a universal attack surface. Any device within approximately '
        '100 metres of a Bluetooth-enabled device is potentially accessible '
        'to an attacker exploiting Bluetooth vulnerabilities. Security '
        'researchers have discovered over 100 significant Bluetooth '
        'vulnerabilities since 2000, including BlueBorne (2017), which '
        'could compromise billions of devices simultaneously without any '
        'user interaction. The second-order cascade: the proliferation of '
        'Bluetooth-enabled medical devices (pacemakers, insulin pumps, '
        'hearing aids) created the possibility of lethal remote attacks on '
        'medical implants, a cascade whose probability is low but whose '
        'severity is unbounded. The standard designed for consumer convenience '
        'has become part of the healthcare security crisis.',
        S['body']))
    story.append(SP(14))
    story.append(callout(
        '<b>Five Cases, One Pattern:</b> In each case: (1) the original '
        'problem was real; (2) the solution genuinely worked for its primary '
        'purpose; (3) the first-order cascade was foreseeable in retrospect '
        'and arguably in advance; (4) the second-order cascade was not '
        'foreseeable but followed necessarily from the first-order cascade '
        'interacting with the existing system. This is the invariant structure '
        'of the cascade across all domains and all centuries.',
        S))
    story.append(SP(14))

    story.append(SP(18))
    story.append(P('Three Principles of Cascade Innovation', S['section']))
    story.append(P(
        'The historical and structural evidence of this chapter can be '
        'condensed into three principles that summarise the theory '
        'of cascade innovation. They are not theorems in a strict mathematical '
        'sense, and they could in principle be overturned by sufficient evidence; '
        'they are empirical generalisations, motivated by the structure of complex '
        'systems and supported by the cases assembled in this book. They are called '
        '"laws" below only loosely — in the folk tradition of Murphy\'s Law and '
        'Goodhart\'s Law — not as formal results carrying the status of proof.',
        S['body0']))
    story.append(SP(14))
    story.append(theorem_box(
        'First Principle of Cascade Innovation',
        'Every solution to a problem in a complex system generates at least '
        'one new problem. The expected number of new problems generated by '
        'a solution grows with the connectivity of the system in which the '
        'solution is deployed. In connected systems with more than a critical '
        'number of existing solutions, the expected number of new problems '
        'generated by each new solution exceeds one.',
        S))
    story.append(SP(14))
    story.append(P(
        'The First Principle is the qualitative statement of the central claim: '
        'solutions generate problems. The "at least one" quantification '
        'is conservative: empirically, most solutions in complex systems '
        'generate multiple new problems, with the number increasing with '
        'system complexity. The criticality condition identifies the phase '
        'transition beyond which the cascade becomes explosive: in sparse '
        'systems (few solutions, low connectivity), cascades remain bounded; '
        'in dense systems (many solutions, high connectivity), cascades '
        'exceed the system\'s solution-generation capacity.',
        S['body']))
    story.append(SP(14))
    story.append(theorem_box(
        'Second Principle of Cascade Innovation',
        'The rate at which a solution ecosystem generates problems eventually '
        'outruns the rate at which solutions can be deployed. No matter how '
        'fast new solutions arrive — whether the rate grows linearly, '
        'quadratically, or at any ordinary pace — the rate of new problems '
        'will, sooner or later, exceed it.',
        S))
    story.append(SP(14))
    story.append(P(
        'The Second Principle is the statement of the long-run divergence between '
        'problem generation and problem solution. It says that no matter how '
        'fast we solve problems, as long as the solving rate is polynomial '
        '(which all physically realised solution processes are), the cascade '
        'generation rate eventually overtakes it. The "eventually" is important: '
        'for small n (few solutions), polynomial solving can keep pace with '
        'cascade generation. The crisis emerges as n grows large. Modern '
        'civilisation is already in the large-n regime in most domains.',
        S['body']))
    story.append(SP(14))
    story.append(theorem_box(
        'Third Principle of Cascade Innovation',
        'Cascade management interventions are themselves solutions deployed '
        'into the solution ecosystem, and are therefore subject to the First '
        'and Second Principles. There is no meta-level from which cascade management '
        'can operate that is immune to cascade generation.',
        S))
    story.append(SP(14))
    story.append(P(
        'The Third Principle is the most philosophically significant and the most '
        'easily overlooked. It says that the FDA, created to manage the '
        'pharmaceutical cascade, is itself a solution that generates cascades '
        '(drug approval delays, regulatory capture, pharmaceutical arbitrage). '
        'The Basel Committee, created to manage the financial cascade, is '
        'itself a solution that generates cascades (regulatory arbitrage, '
        'shadow banking migration, procyclical capital requirements). The '
        'WHO\'s antimicrobial resistance programme, created to manage the '
        'antibiotic resistance cascade, is itself a solution that generates '
        'cascades (institutional competition with national health agencies, '
        'political contestation of its recommendations). The Third Principle means '
        'that cascade management cannot be perfected; it can only be improved. '
        'Every improvement generates new problems. This is not a reason to '
        'abandon cascade management; it is the reason cascade management '
        'must be continuous, adaptive, and humble.',
        S['body']))
    story.append(SP(18))

    # ------------------------------------------------------------------ #
    # EXTENDED: Game Theory and the Prisoner's Dilemma Cascade             #
    # ------------------------------------------------------------------ #
    story.append(SP(18))
    story.append(P('Game Theory and the Strategic Cascade', S['section']))
    story.append(P(
        'Game theory, the mathematical framework for analysing '
        'strategic interaction between rational agents, '
        'developed by von Neumann and Morgenstern in '
        '<i>Theory of Games and Economic Behavior</i> (1944) '
        'and substantially extended by Nash (1950), '
        'solved the problem of modelling rational '
        'strategic behaviour. Before game theory, '
        'economics had no systematic framework for '
        'analysing situations where one actor\'s '
        'optimal strategy depends on what other '
        'actors do. Game theory provided this '
        'framework and immediately revealed '
        'a cascade: the rational individual '
        'strategies identified by game theory '
        'frequently produce collectively irrational '
        'outcomes.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The Prisoner\'s Dilemma, formalised by Merrill Flood '
        'and Melvin Dresher in 1950, is the archetype. '
        'Two suspects, questioned separately, each face '
        'the choice of cooperating with the other '
        '(staying silent) or defecting (betraying). '
        'The Nash equilibrium, the rational strategy '
        'for each individual is to defect. But '
        'if both defect, both receive worse outcomes '
        'than if both had cooperated. The solution '
        'to the problem of individual rationality '
        'cascades into the problem of collective '
        'irrationality. The Prisoner\'s Dilemma '
        'is not merely an abstract puzzle; it '
        'is the mathematical structure of antibiotic '
        'resistance (each physician\'s rational '
        'prescription generates collective resistance), '
        'of climate change (each country\'s rational '
        'energy use generates collective warming), '
        'and of financial crises (each institution\'s '
        'rational leverage generates collective fragility).',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'Nash\'s 1950 proof of the existence of equilibria '
        'in general n-player games extended the solution '
        'to the most general form of strategic interaction. '
        'The cascade from Nash\'s theorem is the cascade '
        'of game-theoretic applications. Nuclear deterrence '
        'strategy was developed using game-theoretic '
        'frameworks, and generated the nuclear arms race '
        'as a Nash equilibrium in which both superpowers '
        'maximised their arsenals (the dominant strategy) '
        'while both would have preferred mutual disarmament. '
        'Auction design, mechanism design, and market '
        'design, fields that have produced billions '
        'in economic value through telecommunications '
        'spectrum auctions and organ matching systems '
        '— are cascades from Nash\'s general equilibrium '
        'framework. Each application generates its own '
        'strategic cascade: spectrum auctions designed '
        'to maximise government revenue generate '
        'telecom market concentration; mechanism '
        'design for financial markets generates '
        'high-frequency trading strategies that '
        'were not anticipated by the mechanism\'s '
        'designers.',
        S['body']))
    story.append(SP(14))
    story.append(callout(
        '<b>The Nash Cascade:</b> Game theory solved the problem of '
        'modelling rational strategic behaviour and immediately revealed '
        'that rational individual strategies produce collectively irrational '
        'outcomes (the Prisoner\'s Dilemma structure). This insight, '
        'the cascade from the solution of individual rationality, '
        'underlies every collective action problem: climate change, '
        'antibiotic resistance, financial crises, arms races.',
        S))
    story.append(SP(14))

    story.append(SP(18))
    story.append(P('Chapter 1 Synthesis: The Pattern Is the Message', S['section']))
    story.append(P(
        'The historical cases in this chapter span four centuries, '
        'seven domains of human activity, and five continents. '
        'They involve solutions ranging from agricultural '
        'enclosure to wireless protocols, from steam engines '
        'to game-theoretic auction design. In each case, '
        'a solution was deployed to address a genuine problem; '
        'the solution worked; and the working of the solution '
        'generated new problems that were, in retrospect, '
        'foreseeable from the solution\'s mechanism and '
        'its interaction with the systems it entered.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The pattern has no exceptions in the historical record '
        'of this book, not because exceptions do not exist, '
        'but because solutions that do not cascade are solutions '
        'whose cascades have not yet manifested, whose cascades '
        'are too small to have attracted historical attention, '
        'or whose cascades were contained by cascade-aware '
        'design in the rare instances where such design was '
        'applied. The Montreal Protocol, smallpox eradication, '
        'and coordinated disclosure are the exceptions that '
        'prove the rule: they succeeded in managing their '
        'cascades precisely because they were designed with '
        'cascade management as an explicit objective, '
        'by institutions with the authority and resources '
        'to enforce cascade-limiting behaviours across '
        'the relevant actor population.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The message of this chapter is not "do not solve problems." '
        'It is "know what you are doing when you solve problems." '
        'Specifically: know that the cascade is coming; know how '
        'to estimate its magnitude; know what early warning signs '
        'to monitor; know what institutional mechanisms to build '
        'before deployment to manage the cascade when it arrives. '
        'The chapters of this book provide the evidence that the '
        'cascade is widespread, the reasoning that shows why it '
        'is so hard to avoid, and the frameworks that show how it can '
        'be managed. The case for cascade awareness rests not '
        'on pessimism about human ingenuity but on respect for '
        'the complexity of the systems our ingenuity operates in.',
        S['body']))
    story.append(SP(14))

    story.append(SP(18))
    story.append(P('Complexity Theory and the Limits of Anticipation', S['section']))
    story.append(P(
        'A final pillar of the theoretical case — this time for the '
        'unpredictability of cascades — comes from computational complexity theory. '
        'The question "can we, in principle, fully anticipate '
        'the cascade from a given solution?" has a formal '
        'answer that is deeply sobering: for most realistic '
        'classes of solution-problem interaction, the answer '
        'is provably no.',
        S['body0']))
    story.append(P(
        'Rice\'s theorem (1953) establishes that for any '
        'non-trivial semantic property of a computer program '
        '— that is, any property that is true of some programs '
        'and false of others; there is no general algorithm '
        'that can determine whether an arbitrary program has '
        'that property. This is a direct corollary of Turing\'s '
        'undecidability result, and it implies that the general '
        'problem of predicting the behaviour of an arbitrary '
        'software system is computationally undecidable. '
        'Software solutions (which are programs) '
        'therefore have cascade properties that cannot '
        'in general be predicted by any algorithm, '
        'however sophisticated. The limits on software '
        'cascade prediction are not engineering constraints '
        'to be overcome by better tools; they are '
        'mathematical constraints established by the '
        'fundamental theory of computation.',
        S['body']))
    story.append(P(
        'For non-software solutions, the equivalent '
        'complexity-theoretic constraints arise from the '
        'NP-hardness of the optimisation problems that '
        'cascade prediction requires. Predicting the '
        'full cascade from a solution deployment in a '
        'complex network requires enumerating the '
        'interactions between the solution and every '
        'element of the network, which is an exponential-time '
        'computation for networks of realistic size. '
        'No polynomial-time approximation algorithm for '
        'this problem is known, and the P ≠ NP conjecture '
        '(if true, as almost all complexity theorists believe) '
        'implies that none exists. The cascade prediction '
        'problem is, in the formal sense, intractable: '
        'it can be approximated, but not solved exactly, '
        'for any but the smallest network instances.',
        S['body']))
    story.append(P(
        'This formal intractability does not mean cascade management '
        'is impossible; it means it is inherently approximate. '
        'The CRI formula is an approximation; the five-stage '
        'trajectory is a heuristic; the design principles '
        'of Chapter 12 are rules of thumb that reduce '
        'cascade risk without eliminating it. This is '
        'exactly the right kind of tool for an intractable '
        'problem: not an exact solution, but a principled '
        'approximation that is better than no approximation. '
        'Weather forecasters cannot predict the weather '
        'exactly beyond a few days, but meteorology is '
        'not useless — probabilistic forecasts with '
        'quantified uncertainty are enormously valuable '
        'even though they are not exact. Cascade theory '
        'occupies the same epistemic position: '
        'principled approximation of an inherently '
        'uncertain process, delivering useful '
        'probabilistic guidance despite formal '
        'undecidability at the exact solution level.',
        S['body']))

    story.append(SP(18))

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
        ('body0', """The cascade is always there. So why don't we see it? The answer lies in
a collection of cognitive biases that are not pathologies of the uneducated mind — they
are features of the human brain that served our species well in the environments where
we evolved, and that serve us catastrophically badly in the complex systems we have
built around ourselves."""),

        ('body', """The most fundamental of these is <b>temporal discounting</b>: the
tendency to value immediate benefits more than equivalent future benefits, and to
discount future costs relative to equivalent present costs. This is not irrational in
evolutionary terms. In an environment where you might not live to see next month, it
makes perfect sense to prioritise the food you can eat today over the food that might
be available next spring. But in a world where the consequences of a policy decision
may take a decade to fully manifest, and where those consequences may affect people
who are not yet born — temporal discounting is a recipe for systematic error."""),

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
        ('body0', """In 1999, David Dunning and Justin Kruger published a study showing that
incompetent individuals systematically overestimate their own competence, and that
highly competent individuals systematically underestimate theirs. The mechanism is
elegant: accurate self-assessment requires the same cognitive skills as the activity
being assessed. If you lack those skills, you also lack the ability to perceive your
lack. This is the Dunning-Kruger effect, and it maps with uncomfortable precision onto
the pattern of innovation cascades."""),

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

        ('section', 'Institutional Incentives to Ignore Cascades'),
        ('body0', """Even when individual actors perceive cascade risks, institutional
incentive structures routinely suppress the information. This is the third layer of
cascade blindness, and in many ways the most important, because it is the layer that
most directly explains why we repeat the same mistakes across institutions, across
generations, and across cultures."""),

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
