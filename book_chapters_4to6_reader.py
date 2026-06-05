from generate_book import *
from io import BytesIO


# ---------------------------------------------------------------------------
# Figure helper functions
# ---------------------------------------------------------------------------

def fig_nuclear_cascade():
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.5, 3.5))
        events = ['Fission\n1938', 'Trinity\n1945', 'Soviet\nBomb 1949',
                  'H-Bomb\n1952', 'Cuba\n1962', 'Chernobyl\n1986', 'Fukushima\n2011']
        years  = [1938, 1945, 1949, 1952, 1962, 1986, 2011]
        severity=[1, 8, 4, 9, 10, 7, 6]
        ax.plot(years, severity, 'k-o', lw=2, markersize=8)
        for i,(yr,sev,ev) in enumerate(zip(years,severity,events)):
            ax.annotate(ev,(yr,sev),textcoords='offset points',
                       xytext=(0,12 if i%2==0 else -26),ha='center',fontsize=7)
        ax.set_ylabel('Cascade Severity (1-10)')
        ax.set_title('The Nuclear Cascade: From Discovery to Eternal Waste')
        ax.set_xlim(1930,2030)
        buf = BytesIO(); fig.savefig(buf,format='png',dpi=150,bbox_inches='tight'); buf.seek(0); plt.close(fig)
    return Image(buf,width=5.5*inch,height=3.2*inch)


def fig_dark_universe():
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(5.5, 4.0))
        sizes=[5,27,68]
        labels=['Ordinary\nMatter (5%)\n"We know this"','Dark\nMatter (27%)\n"Unknown"','Dark\nEnergy (68%)\n"Unknown"']
        colors=['white','#888888','#333333']
        ax.pie(sizes,labels=labels,colors=colors,
               wedgeprops=dict(edgecolor='black',linewidth=1.5),textprops=dict(fontsize=8))
        ax.set_title("The Universe: 95% Unknown", fontsize=11)
        buf = BytesIO(); fig.savefig(buf,format='png',dpi=150,bbox_inches='tight'); buf.seek(0); plt.close(fig)
    return Image(buf,width=4.5*inch,height=3.5*inch)


def fig_quantum_interpretations():
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.5, 3.8))
        ax.text(0.5,0.92,'QUANTUM MECHANICS\n(solving atomic spectra, 1900-1930)',
               ha='center',va='top',fontsize=10,fontweight='bold',
               bbox=dict(boxstyle='round',facecolor='white',edgecolor='black',lw=2))
        interps=[(0.1,0.48,'Copenhagen\n"Don\'t ask"'),(0.3,0.58,'Many-Worlds\n10^(10^100)\nuniverse splits'),
                 (0.5,0.48,'Pilot Wave\n(de Broglie)'),(0.7,0.58,'QBism\n"Beliefs only"'),(0.9,0.48,'Relational\n(Rovelli)')]
        for x,y,label in interps:
            ax.annotate('',xy=(x,y+0.10),xytext=(0.5,0.82),arrowprops=dict(arrowstyle='->',color='black'))
            ax.text(x,y,label,ha='center',va='top',fontsize=8,
                   bbox=dict(boxstyle='round',facecolor='#f5f5f5',edgecolor='black'))
        ax.text(0.5,0.08,'Each interpretation solves the measurement problem\nbut creates new philosophical problems',
               ha='center',fontsize=9,style='italic')
        ax.set_xlim(0,1); ax.set_ylim(0,1); ax.axis('off')
        ax.set_title('The Quantum Interpretation Cascade',fontsize=10)
        buf = BytesIO(); fig.savefig(buf,format='png',dpi=150,bbox_inches='tight'); buf.seek(0); plt.close(fig)
    return Image(buf,width=5.5*inch,height=3.4*inch)


def fig_cve_growth():
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.5, 3.5))
        years=[1999,2001,2003,2005,2007,2009,2011,2013,2015,2017,2019,2021,2023]
        cves=[894,1445,1367,5990,6610,5736,4155,5191,6987,14714,17305,20171,28902]
        ax.bar(years,cves,color='black',alpha=0.7,width=1.5)
        ax.set_xlabel('Year'); ax.set_ylabel('New CVEs Reported')
        ax.set_title('Security Vulnerabilities Per Year: The Patch Cascade (1999-2023)')
        buf = BytesIO(); fig.savefig(buf,format='png',dpi=150,bbox_inches='tight'); buf.seek(0); plt.close(fig)
    return Image(buf,width=5.5*inch,height=3.2*inch)


def fig_brooks_law():
    import numpy as np
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.5, 3.5))
        n=np.arange(1,51)
        ax.plot(n,n,'k:',lw=2,label='Team Members (n)')
        ax.plot(n,n*(n-1)/2,'k-',lw=2.5,label='Communication Links: n(n-1)/2')
        ax.set_xlabel('Team Size'); ax.set_ylabel('Count')
        ax.set_title("Brooks' Law: Communication Links Grow Quadratically with Team Size")
        ax.legend(loc='upper left',fontsize=9)
        buf = BytesIO(); fig.savefig(buf,format='png',dpi=150,bbox_inches='tight'); buf.seek(0); plt.close(fig)
    return Image(buf,width=5.5*inch,height=3.2*inch)


def fig_windows_complexity():
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.5, 3.5))
        versions=['NT3.1\n1993','Win2000\n2000','WinXP\n2001','Vista\n2007','Win10\n2015','Win11\n2021']
        loc=[4.5,29,45,50,80,100]
        ax.bar(range(len(versions)),loc,color='black',alpha=0.7)
        ax.set_xticks(range(len(versions))); ax.set_xticklabels(versions,fontsize=8)
        ax.set_ylabel('Lines of Code (Millions)')
        ax.set_title('Windows Source Code Growth: Feature Bloat in Action')
        for i,v in enumerate(loc):
            ax.text(i,v+0.5,f'{v}M',ha='center',fontsize=8)
        buf = BytesIO(); fig.savefig(buf,format='png',dpi=150,bbox_inches='tight'); buf.seek(0); plt.close(fig)
    return Image(buf,width=5.5*inch,height=3.2*inch)


def fig_internet_cascade_tree():
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.5, 4.2))
        nodes = [
            (0.5,0.92,'ARPANET 1969\n(solving military comms)',12,'bold'),
            (0.5,0.78,'World Wide Web 1991',10,'normal'),
            (0.18,0.60,'Email Spam\n143B/day',8,'normal'),
            (0.5,0.60,'Social Media\nMisinformation',8,'normal'),
            (0.82,0.60,'E-commerce\nFraud',8,'normal'),
            (0.18,0.36,'Phishing\nIdentity theft',8,'normal'),
            (0.5,0.36,'Deepfakes\nAI misuse',8,'normal'),
            (0.82,0.36,'Data monopolies',8,'normal'),
        ]
        for x,y,text,fs,weight in nodes:
            ax.text(x,y,text,ha='center',va='top',fontsize=fs,fontweight=weight,
                   bbox=dict(boxstyle='round,pad=0.3',facecolor='white',edgecolor='black',lw=1))
        for (x1,y1),(x2,y2) in [((0.5,0.85),(0.5,0.73)),
            ((0.5,0.73),(0.18,0.65)),((0.5,0.73),(0.5,0.65)),((0.5,0.73),(0.82,0.65)),
            ((0.18,0.55),(0.18,0.43)),((0.5,0.55),(0.5,0.43)),((0.82,0.55),(0.82,0.43))]:
            ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle='->',color='black',lw=1))
        ax.set_xlim(0,1); ax.set_ylim(0.28,1.0); ax.axis('off')
        ax.set_title('The Internet Cascade Tree',fontsize=11)
        buf = BytesIO(); fig.savefig(buf,format='png',dpi=150,bbox_inches='tight'); buf.seek(0); plt.close(fig)
    return Image(buf,width=5.5*inch,height=3.8*inch)


def fig_jevons_rebound():
    import numpy as np
    with plt.xkcd():
        fig, axes = plt.subplots(1,2,figsize=(6.5,3.2))
        years=np.array([1975,1985,1995,2005,2015,2023])
        axes[0].plot(years,np.array([13,17,21,25,30,36]),'k-o',lw=2,label='Fuel Economy (MPG)')
        ax2=axes[0].twinx()
        ax2.plot(years,np.array([1.0,1.3,1.5,1.8,2.2,2.7]),'k--s',lw=2,label='Miles Driven (rel)')
        axes[0].set_ylabel('Average MPG'); axes[0].set_title('Cars: Efficiency UP')
        led_years=np.array([2000,2005,2010,2015,2020])
        axes[1].plot(led_years,np.array([1,1.5,3,6,10]),'k-o',lw=2)
        ax3=axes[1].twinx()
        ax3.plot(led_years,np.array([1,1.1,1.2,1.4,1.49]),'k--s',lw=2)
        axes[1].set_ylabel('LED Efficiency (rel)'); axes[1].set_title('LEDs: Use Also UP')
        fig.suptitle("Jevons Paradox: Efficiency Gains -> More Total Consumption",fontsize=10)
        plt.tight_layout()
        buf = BytesIO(); fig.savefig(buf,format='png',dpi=150,bbox_inches='tight'); buf.seek(0); plt.close(fig)
    return Image(buf,width=5.5*inch,height=3.0*inch)


def fig_cdo_cascade():
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.5, 4.2))
        layers=[
            (0.5,0.93,'MORTGAGES\n(solving homeownership)'),
            (0.28,0.76,'MBS\n(solving liquidity)'), (0.72,0.76,'CDO\n(solving risk)'),
            (0.12,0.58,'CDO\xb2'), (0.5,0.58,'Synthetic\nCDO'), (0.88,0.58,'CDS\n(insurance)'),
            (0.5,0.32,'SYSTEMIC\nCOLLAPSE 2008'),
        ]
        for x,y,text in layers:
            ax.text(x,y,text,ha='center',va='top',fontsize=8,
                   bbox=dict(boxstyle='round',facecolor='white',edgecolor='black',lw=1.5))
        connections=[((0.5,0.89),(0.28,0.81)),((0.5,0.89),(0.72,0.81)),
                     ((0.28,0.72),(0.12,0.63)),((0.5,0.72),(0.5,0.63)),((0.72,0.72),(0.88,0.63)),
                     ((0.12,0.54),(0.5,0.38)),((0.5,0.54),(0.5,0.38)),((0.88,0.54),(0.5,0.38))]
        for (x1,y1),(x2,y2) in connections:
            ax.annotate('',xy=(x2,y2),xytext=(x1,y1),arrowprops=dict(arrowstyle='->',color='black'))
        ax.set_xlim(0,1); ax.set_ylim(0.22,1.0); ax.axis('off')
        ax.set_title('The 2008 Financial Cascade: Solutions Stacked on Solutions',fontsize=10)
        buf = BytesIO(); fig.savefig(buf,format='png',dpi=150,bbox_inches='tight'); buf.seek(0); plt.close(fig)
    return Image(buf,width=5.5*inch,height=3.8*inch)


def fig_fed_balance_sheet():
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.5, 3.5))
        years=[2000,2004,2006,2008,2009,2010,2012,2014,2016,2018,2020,2021,2022,2023]
        assets=[0.69,0.78,0.87,0.91,2.1,2.3,2.9,4.5,4.5,4.0,7.1,8.8,8.9,8.0]
        ax.fill_between(years,assets,alpha=0.3,color='black')
        ax.plot(years,assets,'k-',lw=2)
        for yr,val,label in [(2008,2.1,'QE1'),(2010,2.3,'QE2'),(2012,2.9,'QE3'),(2020,7.1,'Covid QE')]:
            ax.annotate(label,(yr,val),xytext=(yr+0.3,val+0.7),
                       arrowprops=dict(arrowstyle='->',color='black'),fontsize=8,ha='center')
        ax.set_xlabel('Year'); ax.set_ylabel('Total Assets (Trillions USD)')
        ax.set_title('Federal Reserve Balance Sheet: The QE Cascade (2000-2023)')
        buf = BytesIO(); fig.savefig(buf,format='png',dpi=150,bbox_inches='tight'); buf.seek(0); plt.close(fig)
    return Image(buf,width=5.5*inch,height=3.2*inch)


def fig_big_tech_cascade():
    """CRI scores for 5 big tech platforms — horizontal bar chart."""
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.5, 3.5))
        companies = ['Facebook/Meta', 'Google Search', 'Amazon AWS', 'Twitter/X', 'Apple iOS']
        cri = [8.7, 7.9, 6.4, 8.1, 5.8]
        bars = ax.barh(companies, cri, color='black', alpha=0.75, height=0.55)
        ax.set_xlim(0, 11)
        ax.set_xlabel('Cascade Risk Index (CRI), higher = more cascade-prone')
        ax.set_title('Big Tech Cascade Risk Scores (estimated CRI, 0–10 scale)')
        for bar, val in zip(bars, cri):
            ax.text(val + 0.15, bar.get_y() + bar.get_height()/2,
                    f'{val}', va='center', fontsize=9)
        ax.axvline(7.0, color='black', lw=1.0, linestyle='--', alpha=0.5)
        ax.text(7.1, 0.1, 'High risk\nthreshold', fontsize=7, alpha=0.7)
        fig.tight_layout()
    return fig


def fig_ai_alignment_gap():
    """AI capability vs safety research — diverging curves over time."""
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.5, 3.5))
        years = np.array([2012, 2014, 2016, 2018, 2020, 2022, 2024])
        capability = np.array([1, 2.5, 5, 12, 30, 85, 200])
        safety     = np.array([1, 1.4, 2, 3.2, 5, 9, 15])
        ax.plot(years, capability, 'k-',  lw=2.5, label='AI capability (relative index)')
        ax.plot(years, safety,     'k--', lw=2.0, label='AI safety research (relative index)')
        ax.fill_between(years, safety, capability, alpha=0.08, color='black')
        ax.set_yscale('log')
        ax.set_ylabel('Relative progress (log scale)')
        ax.set_xlabel('Year')
        ax.set_title('The AI Alignment Gap: Capability Races Ahead of Safety')
        ax.legend(loc='upper left', fontsize=8)
        ax.annotate('GPT-4\n(2023)', xy=(2022, 85), xytext=(2019, 90),
                    arrowprops=dict(arrowstyle='->', color='black'), fontsize=8)
        fig.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# Chapter 4 — Physics
# ---------------------------------------------------------------------------

def chapter4(S):
    story = []
    story += chapter_opener(
        'Chapter Four',
        'Physics — Nature\'s Revenge',
        'When scientists solved the atom, nature handed them a bill they are still paying', S)
    story += epigraph(
        'Anyone who is not shocked by quantum mechanics has not understood it.',
        'Niels Bohr', S)
    story += [SP(12)]

    # ------------------------------------------------------------------
    # Section 1: Maxwell's Demon
    # ------------------------------------------------------------------
    story.append(SP(22))
    story.append(P("Maxwell's Demon and the Birth of Information Theory", S['section']))
    story.append(SP(14))

    story.append(P(
        "In 1867, the Scottish physicist James Clerk Maxwell proposed a thought experiment "
        "that would haunt physics for the next hundred years. Imagine a small demon sitting "
        "at a trapdoor between two chambers of gas held at equal temperature. The demon "
        "watches individual molecules approach the door. When a fast-moving molecule comes "
        "from the left chamber, he opens the door; when a slow-moving molecule approaches "
        "from the right, he opens it again. Over time, fast molecules accumulate on the "
        "right side, slow ones on the left, the right chamber grows hot, the left grows "
        "cold, without any external work being done on the gas. The demon has, apparently, "
        "violated the Second Law of Thermodynamics: entropy has decreased without any energy "
        "expenditure, heat has flowed from a cooler region to a hotter one spontaneously, "
        "and the most inviolable constraint in classical physics has been breached by a "
        "single thought experiment involving an imaginary creature sorting molecules.",
        S['body0']))
    story.append(SP(14))

    story.append(P(
        "The cascade from Maxwell's Demon is one of the most intellectually productive in "
        "the history of science, precisely because the paradox is so fundamental. Ludwig "
        "Boltzmann, attempting to derive the Second Law from the atomic theory of matter, "
        "was tormented by attacks from Ernst Mach and Wilhelm Ostwald who denied that atoms "
        "existed at all. He spent thirty years defending the statistical interpretation of "
        "entropy against withering criticism; he died by suicide in 1906, a year before "
        "Einstein's Brownian motion paper conclusively confirmed the existence of atoms and "
        "vindicated everything Boltzmann had argued. Leo Szilard, in a remarkable 1929 paper, "
        "showed that the demon must pay a thermodynamic cost for the act of measuring each "
        "molecule's speed — measurement itself has a physical price in entropy. Charles "
        "Bennett in 1982 refined this analysis further: it is not measurement but the "
        "erasure of information from the demon's memory that costs entropy. When the demon "
        "discards information about a molecule it has already processed, it must dissipate "
        "heat into the environment, and that heat exactly compensates for the entropy "
        "decrease the demon created.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "Rolf Landauer had proved the crucial physical principle in 1961. Landauer's "
        "Principle states that every irreversible erasure of one bit of information must "
        "dissipate a minimum energy of kT ln(2) into the environment, where k is "
        "Boltzmann's constant and T is the temperature of the system. At room temperature "
        "(300 K), this is approximately 2.9 × 10^-21 joules, an extraordinarily small "
        "amount of energy for a single bit. But modern computers erase billions of bits "
        "per second in every processor clock cycle, and those erasures add up. Landauer's "
        "Principle establishes a fundamental physical lower bound on the energy consumption "
        "of computation: any computer that erases information, which is to say, any "
        "conventional computer must dissipate at least this minimum heat. The principle "
        "connects thermodynamics, information theory, and computational complexity in a "
        "single equation, resolving a paradox that had remained open for nearly a century.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The cascade from solving Maxwell's Demon spans two centuries and now touches every "
        "corner of the digital economy. Claude Shannon's 1948 paper 'A Mathematical Theory "
        "of Communication' (the founding document of information theory) drew directly on "
        "the Boltzmann entropy formalism that had emerged from the demon debate. Shannon "
        "showed that information could be quantified exactly as thermodynamic entropy, that "
        "every communication channel has a maximum capacity (the Shannon limit), and that "
        "data compression and error correction have absolute theoretical bounds. The entire "
        "architecture of digital communication: fibre-optic cables, Wi-Fi protocols, "
        "smartphone compression algorithms, streaming video, GPS satellites is built on "
        "Shannon's theorems, which are built on Boltzmann's statistical mechanics, which "
        "emerged from Maxwell's demon.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The thermodynamics of computation has become a pressing practical concern in the "
        "twenty-first century. Training GPT-4, OpenAI's large language model released in "
        "2023, consumed an estimated 50 gigawatt-hours of electricity — equivalent to the "
        "annual energy consumption of roughly 4,500 average American households, for a "
        "single training run. Google's data centers consumed approximately 18.3 TWh of "
        "electricity in 2022. Global data center consumption reached an estimated 200-250 "
        "TWh in 2022, approximately 1% of total global electricity consumption, and is "
        "projected by the International Energy Agency to reach 1,000 TWh by 2030 if AI "
        "model training continues at its current trajectory. Maxwell proposed his demon in "
        "1867 as a purely theoretical puzzle; the cascade it initiated now consumes more "
        "electricity than most countries.",
        S['body']))
    story.append(SP(14))

    story.append(fig_quantum_interpretations())
    story.append(P(
        "Figure 4.1: The quantum interpretation cascade. Solving atomic spectra (1900-1930) "
        "immediately generated the measurement problem, which has spawned at least nine major "
        "competing interpretations (none universally accepted) and remains the deepest "
        "unsolved conceptual problem in physics after a century of effort.",
        S['caption']))

    # ------------------------------------------------------------------
    # Section 2: Quantum Mechanics
    # ------------------------------------------------------------------
    story.append(SP(22))
    story.append(P('Quantum Mechanics and the Measurement Crisis', S['section']))
    story.append(SP(14))

    story.append(P(
        "In the final years of the nineteenth century, classical physics confronted two "
        "stubborn anomalies it could not explain. The first was the ultraviolet catastrophe: "
        "classical electromagnetic theory predicted that a heated object (a blackbody) "
        "should emit infinite amounts of radiation at short wavelengths, an obviously "
        "absurd result that contradicted every experiment. The second was the photoelectric "
        "effect: shining light on a metal surface ejects electrons, but the energy of the "
        "ejected electrons depends on the frequency of the light, not its intensity, a "
        "result that waves cannot explain. In 1900, Max Planck solved the first problem by "
        "proposing, in his own words, 'an act of desperation', that energy is not continuous "
        "but comes in discrete packets, quanta, proportional to frequency. He later admitted "
        "he did not believe the quantization was physically real; he thought it was a "
        "mathematical trick that happened to give the right answer.",
        S['body0']))
    story.append(SP(14))

    story.append(P(
        "Albert Einstein took the quantization seriously in 1905, applying it to explain the "
        "photoelectric effect by proposing that light itself is composed of discrete particles "
        "— photons. This work, not special or general relativity, was what won Einstein the "
        "Nobel Prize in Physics in 1921. Niels Bohr applied quantization to the hydrogen "
        "atom in 1913, producing a model that explained the discrete spectral lines of "
        "hydrogen with extraordinary precision. The full quantum mechanical formalism was "
        "developed between 1924 and 1927 by de Broglie, Heisenberg, Schr\u00f6dinger, Dirac, "
        "Pauli, and Born. By 1930, quantum mechanics had solved not just the two original "
        "anomalies but essentially every puzzle of atomic physics: the stability of atoms, "
        "the structure of the periodic table, the nature of chemical bonds, the properties "
        "of semiconductors and metals. Its predictions have since been confirmed to twelve "
        "decimal places, greater precision than any other scientific theory ever devised.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The double-slit experiment reveals the paradox at quantum mechanics' core. Fire "
        "electrons one at a time at a barrier with two slits, and they build up an "
        "interference pattern on a detector screen behind the barrier, a pattern that "
        "only makes sense if each individual electron passes through both slits "
        "simultaneously and interferes with itself. But if you place a detector at the "
        "slits to determine which slit each electron actually passes through, the "
        "interference pattern vanishes and you see two bands, as you would expect from "
        "classical particles. The act of measuring which path the electron takes destroys "
        "the interference. This is not a matter of disturbing the electron with the "
        "measuring device — experiments have been performed in which the 'which-path' "
        "information is erased after the electron has already been detected, and the "
        "interference pattern reappears. The quantum state of a particle depends on whether "
        "information about it exists anywhere in the universe, regardless of when or where "
        "that information is acquired.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The Copenhagen Interpretation, developed by Bohr and Heisenberg at a series of "
        "conferences in the late 1920s, responds to this paradox by declaring it a "
        "pseudo-problem. On this view, quantum mechanics is a theory of measurement results, "
        "not of physical reality. There is no fact of the matter about what a quantum system "
        "is doing between measurements; all that exists are the probabilities of different "
        "measurement outcomes. The instruction 'shut up and calculate', associated with David "
        "Mermin though probably apocryphal in exact form, captures the Copenhagen spirit: "
        "use the formalism to compute predictions, and do not ask what is 'really happening'. "
        "Most working physicists adopt this position in practice. It is philosophically "
        "unsatisfying to many, because it places the act of measurement at the foundation "
        "of physics without explaining what a measurement is, when it occurs, or why "
        "measurement should be different from any other physical process.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "Hugh Everett III proposed the Many-Worlds Interpretation in his 1957 Princeton "
        "PhD thesis as an attempt to take quantum mechanics perfectly seriously with no "
        "special role for measurement. On Everett's account, the universal wave function "
        "never collapses; every quantum event causes the universe to branch into multiple "
        "parallel branches, one for each possible outcome, all equally real. The electron "
        "that passed through the double slit does pass through both slits, but in different "
        "branches of the wave function. The branches cannot interact once they have "
        "diverged, so observers in each branch see only one outcome. The number of branches "
        "required by this interpretation, if it is correct, is staggering: every quantum "
        "event — every particle interaction anywhere in the universe since the Big Bang — "
        "produces a branching. The estimated number of branches is approximately 10^(10^100), "
        "a number so large it cannot be meaningfully comprehended. Many physicists find this "
        "ontological extravagance unacceptable; others argue it is the most honest "
        "interpretation of the formalism.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "John Bell's 1964 theorem proved that quantum mechanics is incompatible with any "
        "theory of hidden local variables, any theory that explains quantum correlations "
        "by appeal to pre-existing properties of particles that measurement merely reveals, "
        "provided those properties are local (not influenced by distant events faster than "
        "light). Alain Aspect's 1982 experiments confirmed Bell's inequality violations "
        "to high precision, establishing that quantum correlations are real and cannot be "
        "explained by any local hidden variable theory. The universe is, in this precise "
        "sense, nonlocal: measuring a particle in Paris instantaneously influences "
        "measurement outcomes for its entangled partner in Tokyo, regardless of the "
        "distance. Nine competing interpretations of quantum mechanics remain active — "
        "Copenhagen, Many-Worlds, pilot wave (de Broglie-Bohm), QBism, relational quantum "
        "mechanics (Rovelli), consistent histories, modal interpretations, spontaneous "
        "collapse theories (GRW), and Penrose's objective reduction — none of them "
        "universally accepted, none of them experimentally distinguishable from the others. "
        "A century after the theory was completed, physicists cannot agree on what "
        "it means.",
        S['body']))
    story.append(SP(14))

    story.append(fig_nuclear_cascade())
    story.append(P(
        "Figure 4.2: The nuclear cascade. The discovery of fission (1938) initiated a "
        "sequence of escalating events, from Trinity (1945) through the Cuban Missile "
        "Crisis (1962) to Chernobyl (1986) and Fukushima (2011), each a cascade from "
        "the attempt to harness or contain the consequences of the previous solution.",
        S['caption']))

    # ------------------------------------------------------------------
    # Section 3: Nuclear Fission
    # ------------------------------------------------------------------
    story.append(SP(22))
    story.append(P("Nuclear Fission and the 100,000-Year Problem", S['section']))
    story.append(SP(14))

    story.append(P(
        "In September 1933, the Hungarian physicist Leo Szilard was crossing Southampton "
        "Row in London, waiting for a traffic light to change, when the idea of a nuclear "
        "chain reaction came to him. If a neutron could split an atom and release two "
        "neutrons in the process, those two neutrons could split two more atoms releasing "
        "four neutrons, and so on, a geometric cascade of energy release unlike anything "
        "ever contemplated. Szilard was so alarmed by his own insight that he filed a "
        "secret patent on the chain reaction with the British Admiralty in 1934 to prevent "
        "it from being published. Otto Hahn, Fritz Strassmann, and Lise Meitner confirmed "
        "nuclear fission experimentally in Berlin in December 1938. Within weeks, "
        "physicists across the world had recognised that Szilard's traffic-light vision "
        "was physically achievable.",
        S['body0']))
    story.append(SP(14))

    story.append(P(
        "The Manhattan Project, the American effort to build an atomic bomb before Nazi "
        "Germany, was the largest scientific and industrial project ever undertaken to that "
        "point in history. At its peak, it employed approximately 130,000 people: scientists, "
        "engineers, construction workers, military personnel, at sites across the United "
        "States and Canada. Its total cost, in 2023 dollars, was approximately $26 billion. "
        "The intellectual resources it concentrated were extraordinary: Oppenheimer, Fermi, "
        "Bohr, Feynman, Bethe, Teller, Szilard, Lawrence, and dozens of other leading "
        "physicists, most of them refugees from Nazi Europe. The project solved its immediate "
        "problem: on July 16, 1945, the first nuclear device (code-named Trinity) detonated "
        "at Alamogordo, New Mexico, releasing energy equivalent to approximately 21 kilotons "
        "of TNT. Oppenheimer, watching the fireball rise, recalled a line from the Bhagavad "
        "Gita: 'Now I am become Death, the destroyer of worlds.'",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The bomb was dropped on Hiroshima on August 6, 1945. The immediate death toll "
        "was approximately 70,000 people, with a further 70,000 to 80,000 dying within "
        "months from radiation and burn injuries. Nagasaki followed on August 9, killing "
        "approximately 40,000 immediately. Japan surrendered on August 15. The problem the "
        "bomb had been designed to solve — ending the war with Japan without an invasion "
        "that military planners estimated might cost a million American casualties was "
        "solved. The cascade that the bomb initiated has not ended. The Soviet Union "
        "successfully tested a nuclear device in August 1949, ending the American monopoly "
        "four years after Hiroshima. The United States tested the first hydrogen bomb in "
        "November 1952, a device a thousand times more powerful than the Hiroshima bomb. "
        "The Soviet Union followed in August 1953. By the early 1960s, nine nuclear states "
        "held weapons capable of ending human civilisation.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The closest humanity has come to nuclear annihilation was not the result of a "
        "political decision but of a single individual's moral courage under almost "
        "inconceivable pressure. On October 27, 1962, the most dangerous day of the "
        "Cuban Missile Crisis, the Soviet submarine B-59 was operating off Cuba, cut off "
        "from radio contact with Moscow for several days. American destroyers began "
        "dropping practice depth charges to force the submarine to surface; the crew "
        "inside did not know these were practice charges. The submarine's political officer, "
        "Ivan Maslennikov, believed war had already begun and pushed for launch of the "
        "submarine's nuclear torpedo. The submarine's captain, Valentin Savitsky, agreed. "
        "Soviet submarine procedure required the agreement of three officers to launch: the "
        "captain, the political officer, and the brigade commodore, Vasili Arkhipov, who "
        "happened to be aboard B-59. Arkhipov refused. His refusal prevented a nuclear "
        "strike on the American fleet, which would almost certainly have triggered a full "
        "nuclear exchange. One man's decision on one afternoon in 1962 may have saved "
        "several hundred million lives.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The civilian nuclear power programme, which followed the weapons programme, "
        "introduced its own cascade. The Three Mile Island accident in Pennsylvania on "
        "March 28, 1979, caused by a combination of equipment failure and operator error "
        "— resulted in a partial core meltdown. The accident caused no immediate deaths "
        "but effectively ended new nuclear power plant construction in the United States "
        "for forty years. The Chernobyl disaster of April 26, 1986 was far more severe: "
        "a flawed reactor design combined with operator error caused an explosion and "
        "fire that released approximately 400 times the radiation of the Hiroshima bomb "
        "into the atmosphere. Approximately 350,000 people were permanently evacuated "
        "from the exclusion zone; an estimated 600,000 'liquidators' were exposed to "
        "dangerous radiation while conducting the cleanup. The Fukushima Daiichi disaster "
        "of March 11, 2011 — triggered by a tsunami disabling backup power to cooling "
        "systems: resulted in three reactor meltdowns, displaced 154,000 people, and "
        "has generated a cleanup cost estimated at $200 billion that will take four decades "
        "to complete.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "But the deepest cascade from nuclear fission is one that has no solution within "
        "any human timescale. Nuclear reactors produce spent fuel rods that remain "
        "lethally radioactive for tens of thousands of years. Plutonium-239, a major "
        "component of spent fuel, has a half-life of 24,100 years, meaning the material "
        "is dangerous for approximately 250,000 years. The United States alone has "
        "accumulated approximately 90,000 metric tons of high-level nuclear waste, "
        "currently stored in temporary facilities (cooling pools and dry casks) at "
        "77 reactor sites across 35 states. Yucca Mountain, Nevada was designated in "
        "1987 as the permanent geological repository for American nuclear waste; the "
        "federal government has spent approximately $15 billion on its design and "
        "approval. The repository has still not opened, due to political opposition from "
        "Nevada, and the current administration has proposed abandoning it entirely. "
        "There is no approved permanent storage site for high-level nuclear waste anywhere "
        "in the world except Finland, which is completing a repository at Onkalo. The "
        "repository must remain sealed and intact for between 10,000 and 100,000 years. "
        "The entirety of recorded human history spans approximately 5,000 years. No human "
        "language has survived 10,000 years in readable form. No human institution has "
        "persisted for 25,000 years. The solution to the energy problem has created a "
        "waste problem that will outlast every civilisation that exists today.",
        S['body']))
    story.append(SP(14))

    story.append(fig_dark_universe())
    story.append(P(
        "Figure 4.3: The composition of the universe. Ordinary matter — everything "
        "physics successfully describes, constitutes just 5% of the total energy "
        "content. Dark matter (27%) and dark energy (68%) are inferred from their "
        "gravitational effects but have never been directly detected or identified.",
        S['caption']))

    story.append(SP(18))
    story.append(P('The Nuclear Waste Cascade: 90,000 Years of Consequences', S['section']))
    story.append(P('Of all the cascades documented in this book, nuclear waste is unique in one respect: it is the only cascade whose resolution timescale exceeds the entirety of recorded human history. High-level nuclear waste, the spent fuel rods from nuclear reactors and the waste from weapons production: remains dangerously radioactive for approximately 100,000 years. Written language is approximately 5,000 years old. Agriculture is approximately 12,000 years old. The entirety of what we recognise as human civilisation fits within the first 12% of the hazard period of the waste already generated.', S['body0']))
    story.append(P('The scale of the waste problem is extraordinary. The United States alone has generated approximately 90,000 metric tonnes of high-level nuclear waste, currently stored in 75 temporary sites across 35 states: sites that were designed for decades-long storage, not millennia-long storage. The Yucca Mountain repository, proposed as a permanent disposal site in Nevada and the subject of three decades of scientific study and $15 billion of investment, was cancelled by the Obama administration in 2009 after Nevada politicians and the public opposed it. No permanent repository for high-level nuclear waste exists anywhere in the world as of 2024. The single most advanced effort is Finland\'s Onkalo repository, currently under construction and expected to accept waste beginning in the 2020s, a facility whose design life is 100,000 years, and whose designers are grappling with the genuinely novel problem of how to warn people 50,000 years from now not to drill into it. No human institution has ever maintained continuous operational knowledge of anything for 10,000 years, let alone 100,000.', S['body']))
    story.append(P('The cascade from nuclear waste is multi-generational in a sense that no other cascade in this book approaches. The solutions deployed by nuclear engineers in the 1950s-1970s: light water reactors, pressurised water reactors, boiling water reactors, solved the problem of electricity generation with remarkable efficiency and with much lower direct mortality than fossil fuel alternatives (nuclear power\'s death rate per TWh of energy produced is lower than solar, wind, or any fossil fuel by orders of magnitude). The cascade they generated is real radiation exposure risk for approximately 5,000 generations of human descendants who had no input into the decision to generate the waste and no ability to influence how it will be managed. This is the most extreme version of the temporal discount problem identified in Chapter 2: the benefits of nuclear power were captured by people alive between 1950 and 2024, and the cascade costs will be borne by people living between 2024 and 102,024, people who cannot vote, cannot sue, and cannot negotiate.', S['body']))
    story.append(P('The secondary cascades from nuclear weapons testing add another dimension. Between 1945 and 1998, the five declared nuclear weapons states and several undeclared ones conducted 2,056 nuclear weapons tests — 528 of them atmospheric, before the Partial Test Ban Treaty of 1963 moved most testing underground. The atmospheric tests distributed radioactive fallout globally, exposing the entire human population to elevated radiation doses. The US National Cancer Institute estimates that fallout from US atmospheric tests alone will cause approximately 11,000 excess cancer deaths among Americans born between 1952 and 2000. The downwinders, communities living downwind of test sites in Nevada, the Marshall Islands, Kazakhstan, and elsewhere — received dramatically higher doses and have documented cancer and birth defect rates that continue to generate litigation and scientific dispute decades after the tests. The nuclear weapons tests solved the problem of deterrence, demonstrating capabilities that prevented the large-scale use of nuclear weapons, and generated a global radiological cascade whose epidemiological consequences are still being counted.', S['body']))
    story.append(callout('<b>The 100,000-Year Problem:</b> Nuclear waste remains hazardous for 100,000 years. Written language is 5,000 years old. No permanent nuclear waste repository exists anywhere in the world. The cascade from nuclear fission is unique in being the only human-generated problem whose solution timescale exceeds the duration of human civilisation by a factor of approximately eight.', S))

    # ------------------------------------------------------------------
    # Section 4: String Theory
    # ------------------------------------------------------------------
    story.append(SP(22))
    story.append(P("String Theory and the Landscape of Unfalsifiability", S['section']))
    story.append(SP(14))

    story.append(P(
        "The Standard Model of particle physics, completed in the 1970s, is the most "
        "precisely confirmed theory in the history of science. It describes all known "
        "elementary particles and three of the four fundamental forces: electromagnetism, "
        "the weak nuclear force, and the strong nuclear force, within a single mathematical "
        "framework. Its predictions have been confirmed to extraordinary precision: the "
        "anomalous magnetic moment of the electron, for instance, is predicted by the "
        "Standard Model to match the experimental value to eleven decimal places. The "
        "Higgs boson, predicted by the model in 1964, was discovered at the Large Hadron "
        "Collider in 2012 after a $10 billion search spanning twenty years. By any measure, "
        "the Standard Model is a triumph of human understanding.",
        S['body0']))
    story.append(SP(14))

    story.append(P(
        "It has one well-known deficiency: it does not include gravity. General relativity, "
        "Einstein's theory of gravitation completed in 1915, describes gravity as the "
        "curvature of spacetime produced by mass and energy. It is spectacularly successful "
        "at macroscopic scales; it predicted black holes, gravitational waves, and the "
        "expansion of the universe. But general relativity is a classical theory; it "
        "cannot be straightforwardly combined with quantum mechanics because the two "
        "frameworks rest on incompatible mathematical foundations. Quantum field theory "
        "treats spacetime as a fixed background; general relativity treats spacetime as "
        "dynamic. When physicists attempt to quantise gravity by applying the methods of "
        "quantum field theory, the calculations produce infinite quantities that cannot be "
        "renormalised away. The incompatibility of the two most successful theories in "
        "physics is the central problem of theoretical physics, and has been for sixty years.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "String theory emerged as a candidate solution in the 1984 'first superstring "
        "revolution', when John Schwarz and Michael Green showed that a specific version "
        "of string theory, a theory in which elementary particles are not point-like but "
        "are tiny one-dimensional vibrating strings was free of the mathematical "
        "inconsistencies that had plagued earlier attempts. The strings' different "
        "vibrational modes correspond to different particles; crucially, one of those "
        "modes corresponds to the graviton, the hypothetical quantum of gravity. For the "
        "first time, a single mathematical framework appeared to naturally incorporate "
        "quantum mechanics and general relativity. Edward Witten, Cumrun Vafa, and others "
        "showed that the theory had extraordinary mathematical richness, producing new "
        "results in algebraic geometry and topology that mathematicians found valuable "
        "quite apart from any physical applications. String theory attracted a generation "
        "of the most talented physicists in the world.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The cascade arrived with the landscape problem. String theory requires "
        "six or seven extra spatial dimensions compactified at scales far too small to "
        "detect. The mathematics of string theory does not uniquely determine how these "
        "extra dimensions are compactified; instead, there are approximately 10^500 "
        "different possible configurations, each corresponding to a different universe "
        "with different physical constants, different particle masses, and different laws "
        "of physics. This is the string landscape: a vast space of possible universes, "
        "of which ours is one. Because the landscape contains 10^500 possibilities, "
        "string theory does not predict the specific physical constants of our universe — "
        "it can accommodate essentially any values of those constants by choosing the "
        "appropriate point on the landscape. A theory that can accommodate anything "
        "predicts nothing.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The string landscape generated the most contentious debate in theoretical physics "
        "in a generation. Leonard Susskind and Raphael Bousso proposed in 2000 that the "
        "landscape should be taken seriously as evidence for a multiverse: we observe the "
        "physical constants we do because we exist in one of the rare landscape vacua that "
        "permits complex structures like atoms, planets, and physicists. This 'anthropic' "
        "argument resolves the fine-tuning problem, why do the constants of nature have "
        "the precise values required for life? but does so at the cost of making string "
        "theory experimentally untestable. Lee Smolin's 2006 book 'The Trouble with "
        "Physics' and Peter Woit's 'Not Even Wrong' (2006) argued that string theory, "
        "after two decades, had produced no testable predictions and had consumed the "
        "careers of hundreds of talented physicists who might have made progress on "
        "other problems. The Large Hadron Collider, after collecting data from 2010 "
        "to 2018 at the energy scales where supersymmetry — string theory's partner "
        "framework, predicted new particles must appear, found none. The solution to "
        "quantum gravity has, so far, generated a crisis about the nature of scientific "
        "explanation itself.",
        S['body']))

    # ------------------------------------------------------------------
    # Section 5: Dark Matter and Dark Energy
    # ------------------------------------------------------------------
    story.append(SP(22))
    story.append(P("Dark Matter, Dark Energy, and the 95% Problem", S['section']))
    story.append(SP(14))

    story.append(P(
        "In 1933, the Swiss astronomer Fritz Zwicky was studying the Coma Cluster, a "
        "collection of more than a thousand galaxies approximately 320 million light-years "
        "from Earth. Zwicky measured the velocities of galaxies within the cluster and "
        "applied the virial theorem (a standard tool of gravitational physics) to "
        "calculate how much mass the cluster must contain to hold itself together at those "
        "velocities. The answer was approximately 400 times more mass than was visible in "
        "the stars and gas of the cluster. Something invisible but massive had to be "
        "present. Zwicky called it 'dunkle Materie' — dark matter. His result was not "
        "taken seriously for decades; the astronomical community assumed he had made a "
        "systematic error.",
        S['body0']))
    story.append(SP(14))

    story.append(P(
        "Vera Rubin and Kent Ford, working at the Carnegie Institution in Washington in "
        "the early 1970s, produced the definitive evidence for dark matter through "
        "meticulous measurements of galactic rotation curves. In a normal gravitational "
        "system (a solar system, for instance) objects at greater distances from the "
        "centre move more slowly, following Kepler's third law. Stars in the outer regions "
        "of galaxies should therefore rotate more slowly than stars near the centre. "
        "Rubin and Ford found the opposite: the rotation curves of spiral galaxies are "
        "essentially flat — stars at the outermost edges of galaxies orbit at roughly the "
        "same speed as those in the interior regions. This can only be explained if "
        "galaxies contain a large halo of invisible matter extending well beyond the "
        "visible disk. Rubin's results were confirmed by dozens of independent teams "
        "using different methods throughout the 1970s and 1980s. Dark matter was no "
        "longer a fringe hypothesis; it was a robust observational fact.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The solution proposed: dark matter, a new form of matter that does not interact "
        "with light but does interact gravitationally, immediately generated new problems. "
        "Despite decades of searches using the most sensitive detectors ever constructed, "
        "dark matter has never been directly detected. Weakly Interacting Massive Particles "
        "(WIMPs), the leading theoretical candidate for dark matter, were predicted by "
        "supersymmetry and should have been detectable in underground experiments. More "
        "than $500 million has been spent on WIMP detection experiments: LUX, PandaX, "
        "XENON1T, LZ, each progressively more sensitive than the last. None has detected "
        "a dark matter particle. Axions, another candidate, are being searched for in "
        "experiments like ADMX and HAYSTAC; no detection. Sterile neutrinos have been "
        "constrained out of most of the parameter space where they were predicted. Every "
        "theoretically motivated dark matter candidate has either been ruled out or remains "
        "stubbornly undetected despite experiments that should have found them.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "Dark energy, the entity invoked to explain the accelerating expansion of the "
        "universe discovered in 1998 by Perlmutter, Schmidt, and Riess, who shared the "
        "2011 Nobel Prize for the finding — adds a further dimension to the problem. "
        "Current observations indicate that dark energy constitutes approximately 68% of "
        "the total energy content of the universe. The leading theoretical explanation is "
        "the cosmological constant, a term Einstein introduced into general relativity in "
        "1917 and later called his 'greatest blunder'. When physicists attempt to calculate "
        "the expected value of the cosmological constant from quantum field theory, they "
        "obtain a value approximately 10^120 times larger than the observed value. This "
        "discrepancy (120 orders of magnitude) is the largest disagreement between a "
        "theoretical prediction and an experimental measurement in the history of science. "
        "An inventory of the universe therefore reads as follows: ordinary matter, the "
        "subject of all of physics since Newton, constitutes approximately 5% of the total "
        "energy content; dark matter is 27% and has never been directly detected; dark "
        "energy is 68% and has no agreed theoretical explanation. Ninety-five percent "
        "of the universe is, in a precise sense, unknown.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The Hubble Tension adds a further layer of difficulty. The Hubble constant H0 "
        "describes the current rate of expansion of the universe. It can be measured in "
        "two independent ways: from the cosmic microwave background (the afterglow of the "
        "Big Bang, observed by the Planck satellite) and from the distance ladder "
        "(observations of Cepheid variable stars and Type Ia supernovae in nearby galaxies, "
        "combined by teams led by Adam Riess and Wendy Freedman). The two methods give "
        "systematically different answers, approximately 67.4 km/s/Mpc from the Planck "
        "measurements and approximately 73 km/s/Mpc from the distance ladder, and the "
        "discrepancy has grown to more than 5 sigma (5 standard deviations) as measurements "
        "have become more precise. A 5-sigma discrepancy in physics is sufficient to claim "
        "a discovery; here it signals that something is fundamentally wrong with the "
        "standard cosmological model, with the measurement methods, or with both. The "
        "attempt to understand the large-scale structure of the universe has generated "
        "a tension between measurement methods that cosmologists cannot currently explain.",
        S['body']))

    story.append(SP(22))
    story.append(P('The Hierarchy Problem and the Naturalness Crisis', S['section']))
    story.append(SP(14))
    story.append(P(
        'The Higgs boson, discovered at CERN in July 2012 after a forty-eight-year '
        'search following Peter Higgs\'s 1964 prediction, was one of the greatest '
        'experimental confirmations in the history of physics. The standard model '
        'of particle physics had predicted the existence of the Higgs field, the '
        'mechanism by which fundamental particles acquire mass, and the Large '
        'Hadron Collider found it with the predicted properties. The scientific '
        'community celebrated the discovery as a triumph of theoretical physics. '
        'The cascade that the confirmation generated was, however, immediate and '
        'profound.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The problem is the mass of the Higgs boson itself. Quantum field theory '
        'predicts that the Higgs mass receives "radiative corrections" from quantum '
        'fluctuations — virtual particle loops that contribute to the effective '
        'mass. In the standard model, these corrections are proportional to the '
        'square of the energy scale at which new physics appears. If the standard '
        'model is valid up to the Planck scale (the energy at which quantum '
        'gravitational effects become important, approximately 10^{19} GeV), the '
        'radiative corrections to the Higgs mass are approximately 10^{17} times '
        'larger than the observed Higgs mass. For the observed Higgs mass of '
        '125 GeV to emerge, the "bare" mass parameter in the Lagrangian must be '
        'tuned to cancel these enormous quantum corrections to a precision of '
        'one part in 10^{34}. This is the hierarchy problem: why is the Higgs '
        'mass so much smaller than the Planck scale, when quantum corrections '
        'should drive it to the Planck scale?',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The most popular solution proposed by theorists was supersymmetry (SUSY): '
        'a symmetry between bosons and fermions that would cancel the radiative '
        'corrections to the Higgs mass exactly, solving the hierarchy problem and '
        'simultaneously providing dark matter candidates (the lightest '
        'supersymmetric particle). Supersymmetry predicted the existence of '
        'supersymmetric partner particles for every standard model particle, '
        'squarks, sleptons, gluinos, charginos, neutralinos, at masses accessible '
        'to the LHC. The LHC was designed and built with the expectation of '
        'discovering SUSY particles. After fifteen years of operation and '
        'two runs at 7, 8, and 13 TeV, no supersymmetric particles have been '
        'found. The mass constraints from LHC non-observation now push squarks '
        'and gluinos above 2-3 TeV, a range that reintroduces the fine-tuning '
        'problem that supersymmetry was supposed to solve.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The cascade from the Higgs discovery is, therefore, the "naturalness '
        'crisis": the standard model is confirmed with extraordinary precision, '
        'the dominant theoretical extension (SUSY) is ruled out at the scales '
        'where it was most motivated, and the hierarchy problem remains unsolved. '
        'The LHC\'s null result for new physics beyond the standard model has '
        'forced a reassessment of the theoretical framework that guided decades '
        'of high-energy physics research. The solution to the problem of how '
        'particles acquire mass has generated a new foundational question, why '
        'is the mass so small?, that is deeper, more precisely stated, and more '
        'resistant to solution than the original problem.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'A parallel cascade has emerged from the precision measurement of the '
        'muon anomalous magnetic moment (the "muon g-2"). The muon\'s magnetic '
        'moment has been measured to eleven significant figures, and the '
        'measurement disagrees with the standard model prediction at a level '
        'of approximately 4.2 sigma — tantalizingly close to the 5-sigma '
        'threshold for a discovery claim, but not yet conclusive. If confirmed, '
        'the muon g-2 anomaly would represent evidence for particles or forces '
        'beyond the standard model, a solution to the question "is the standard '
        'model complete?" would come with the immediate generation of a new '
        'problem: which extension of the standard model accounts for the anomaly, '
        'and why does that extension not appear at LHC energies? The measurement '
        'of nature with ever-greater precision is itself a cascade generator: '
        'each digit of precision reveals a new discrepancy, and each discrepancy '
        'demands a new theoretical explanation.',
        S['body']))
    story.append(SP(14))

    story.append(SP(22))
    story.append(P('Climate Science: Solving the Greenhouse Problem and the Attribution Cascade', S['section']))
    story.append(SP(14))
    story.append(P(
        'The cascade in physics extends into climate science with particular '
        'urgency. The greenhouse effect, the mechanism by which atmospheric '
        'gases trap outgoing infrared radiation and warm the planet\'s surface, '
        'was identified by Eunice Newton Foote in 1856 and formalised by '
        'Svante Arrhenius in 1896, who calculated that doubling atmospheric '
        'CO\u2082 would raise global temperatures by 5-6°C. Arrhenius was solving '
        'a scientific problem: what determines the temperature of planets? '
        'His solution generated the cascade problem: what happens to the '
        'atmosphere when industrial civilisation burns fossil fuels at '
        'ever-increasing rates?',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The scientific cascade from climate research is the "attribution problem": '
        'given a specific weather event (a heat wave, a hurricane, a flood) '
        'what fraction of its severity is attributable to climate change? This '
        'question emerged from the solution to the broader climate attribution '
        'problem (demonstrating that human emissions are warming the planet), '
        'and it is a substantially more difficult problem than the one it emerged '
        'from. Global warming attribution can be established from the statistical '
        'pattern of temperature trends over decades. Event attribution requires '
        'running thousands of climate model simulations with and without the '
        'human forcing, comparing the distribution of event severities, and '
        'expressing the result as a probability ratio, how much more likely '
        'was this event in a world with human emissions than in a world without '
        'them? The computational and statistical requirements of event attribution '
        'science are orders of magnitude greater than those of global warming '
        'attribution.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The technological cascade from proposed climate solutions is the most '
        'consequential. Solar geoengineering, the deliberate injection of '
        'reflective particles (sulphate aerosols) into the stratosphere to '
        'reduce incoming solar radiation, cooling the planet while CO\u2082 '
        'remains elevated is proposed as a solution to the climate emergency. '
        'The cascade risks of stratospheric aerosol injection are themselves '
        'extraordinary: termination shock (if the injection is halted for any '
        'reason (political, economic, or catastrophic) temperatures rebound '
        'at ten times their normal rate, potentially causing more damage in a '
        'decade than was avoided over the previous century); unequal regional '
        'impacts (the aerosols affect monsoon patterns, potentially reducing '
        'rainfall in already water-stressed regions of Africa and Asia); ozone '
        'depletion (sulphate aerosols catalyse ozone chemistry in the same way '
        'as the CFCs regulated by the Montreal Protocol); and moral hazard '
        '(the existence of a technical "fix" reduces political pressure for '
        'emissions reduction). The cascade risk of the geoengineering solution '
        'to the climate problem may itself require geoengineering solutions, '
        'a cascade of interventions managing interventions that has no natural '
        'terminal condition.',
        S['body']))
    story.append(SP(14))

    story.append(SP(18))
    story.append(P('Thermodynamics and the Energy Cascade', S['section']))
    story.append(P(
        'The science of thermodynamics was developed in the nineteenth century '
        'to solve the practical problem of making steam engines more efficient. '
        'Sadi Carnot\'s 1824 "Reflections on the Motive Power of Fire" established '
        'that the maximum efficiency of a heat engine depends only on the '
        'temperatures of its hot and cold reservoirs, not on the working fluid '
        'or the specific mechanism. Carnot\'s insight was simultaneously a solution '
        '(a theoretical limit that guided engine design) and a cascade generator '
        '(by establishing that no engine could be 100% efficient, Carnot\'s theorem '
        'implied that all engines generate waste heat, a cascade that, at '
        'industrial scales, would eventually become the basis of the theory '
        'of anthropogenic climate change).',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The second law of thermodynamics — entropy always increases in an '
        'isolated system is the most general statement of the cascade principle '
        'in the physical sciences. Any transformation of energy from a more ordered '
        'to a less ordered state is irreversible; the reverse process, converting '
        'disordered energy (heat) back to ordered energy (work), always requires '
        'an input of work greater than the output. This is the physical basis of '
        'cascade irreversibility in technological systems: complex, ordered '
        'structures (chemical compounds, ecosystems, genetic sequences) once '
        'disordered by technological intervention cannot be restored without '
        'an energy expenditure greater than the energy gained from the intervention. '
        'The thermodynamics of cascade reversal is always unfavourable.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'Maxwell\'s Demon, proposed by James Clerk Maxwell in 1867, is a '
        'thought experiment that illuminates the relationship between information '
        'and entropy in a way directly relevant to cascade theory. Maxwell imagined '
        'a demon controlling a small door between two gas chambers, allowing fast '
        'molecules through in one direction and slow molecules in the other, '
        'apparently sorting molecules without doing work and thus violating the '
        'second law. The resolution, developed by Leo Szilard in 1929 and '
        'Charles Bennett in 1982, is that the demon must maintain a memory of '
        'the molecules\' velocities, and erasing that memory (as the demon must '
        'eventually do to avoid infinite information storage) generates entropy '
        'that exactly compensates the sorting work. The information-entropy '
        'connection established by this analysis has a direct implication for '
        'cascade management: monitoring a cascade requires storing information '
        'about the cascade, and that information storage has a physical cost '
        '(the Landauer limit: kT ln 2 per bit erased). Cascade management '
        'at scale has a thermodynamic minimum energy cost that scales with the '
        'complexity of the cascade being monitored. This is not practically '
        'limiting with current technology, but it establishes that perfect '
        'cascade monitoring — monitoring every bit of cascade information in '
        'every system simultaneously is not merely politically or economically '
        'infeasible, but physically impossible.',
        S['body']))
    story.append(SP(14))

    # ── Quantum Mechanics Extended ─────────────────────────────────────────
    story.append(SP(18))
    story.append(P('Quantum Computing: The Next Physics Cascade', S['section']))
    story.append(P(
        'Quantum computing is simultaneously the most hyped and the most '
        'genuinely disruptive emerging technology of the twenty-first century. '
        'It solves a real problem: classical computers are exponentially '
        'inefficient at simulating quantum systems, a limitation that '
        'constrains drug discovery, materials science, and fundamental physics '
        'research. Richard Feynman\'s 1982 observation that "if you want to '
        'make a simulation of nature, you\'d better make it quantum mechanical" '
        'identified the problem that quantum computing solves. The cascade '
        'from the solution is already visible before functional large-scale '
        'quantum computers exist, because the anticipation of quantum computing '
        'has initiated a cryptographic cascade that is one of the largest '
        'infrastructure migrations in the history of computing.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The cryptographic cascade is the most immediate cascade from quantum '
        'computing. Current public-key cryptography — RSA, elliptic curve '
        'Diffie-Hellman, the Digital Signature Algorithm is based on the '
        'computational hardness of factoring large integers and computing '
        'discrete logarithms. Peter Shor\'s 1994 quantum algorithm solves '
        'both problems efficiently on a fault-tolerant quantum computer. '
        'A sufficiently powerful quantum computer could therefore break '
        'all currently deployed public-key cryptography retroactively, '
        'including communications intercepted and stored today for future '
        'decryption ("harvest now, decrypt later"). NIST began the Post-Quantum '
        'Cryptography Standardisation Project in 2016 and published the first '
        'post-quantum standards in 2024. The migration from classical to '
        'post-quantum cryptography will require updating every cryptographic '
        'implementation in every internet-connected system, an estimated '
        'tens of billions of devices. The cost of this migration is estimated '
        'at hundreds of billions of dollars globally. This is the cascade '
        'from a technology that does not yet fully exist: the announcement '
        'of Shor\'s algorithm in 1994 initiated a cascade that will not fully '
        'resolve until the 2030s.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The error correction cascade is the primary technical obstacle to '
        'realising fault-tolerant quantum computing, and it is itself a '
        'cascade from the solution to quantum error decoherence. Quantum '
        'computers require qubits to maintain quantum coherence for long '
        'enough to perform computations. Physical qubits are subject to '
        'decoherence — interaction with the environment destroys the quantum '
        'superposition. The solution is quantum error correction: encoding '
        'one logical qubit in many physical qubits, using the redundancy to '
        'detect and correct errors without measuring the quantum state. '
        'The cascade is the overhead: current estimates suggest that one '
        'logical qubit requires approximately 1,000 physical qubits for '
        'fault-tolerant operation. A quantum computer with 1,000 logical '
        'qubits (enough to run Shor\'s algorithm against RSA-2048) would '
        'require approximately 1 million physical qubits. The largest '
        'quantum processors in 2024 have approximately 1,000 physical qubits. '
        'The cascade from the decoherence problem is a factor-of-1,000 '
        'hardware overhead requirement that has transformed quantum computing '
        'from a near-term to a medium-term technology, and that has generated '
        'massive research investment in improved qubit technologies, error '
        'correction codes, and fault-tolerant architectures.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The societal cascade from quantum computing is already manifesting '
        'in the geopolitical race for quantum supremacy. The United States, '
        'China, the European Union, Japan, and a growing number of other '
        'nations have designated quantum computing as a strategic technology '
        'requiring massive public investment and export controls. China\'s '
        'National Quantum Initiatives, the US National Quantum Initiative Act '
        '(2018), and the EU\'s Quantum Flagship programme represent combined '
        'public investment of over $10 billion. The cascade from this '
        'competition includes: secrecy about research results (reducing '
        'the international scientific collaboration that typically accelerates '
        'technology development); export controls on quantum hardware and '
        'software (generating supply chain complications); and the application '
        'of quantum computing to intelligence and surveillance applications '
        '(which, if realised, would enable surveillance capabilities without '
        'historical precedent). The solution to the simulation problem, '
        'quantum computing has generated a geopolitical and surveillance '
        'cascade that is, in many respects, the physics community\'s '
        'equivalent of the nuclear cascade of 1939-1945.',
        S['body']))
    story.append(SP(14))

    story.append(SP(18))
    story.append(P('The Neutrino Problem: Particles That Break Models', S['section']))
    story.append(P(
        'The Standard Model of particle physics is, by empirical measures, '
        'the most precisely confirmed scientific theory in history: its '
        'predictions agree with experiment to twelve significant figures '
        'in the case of the electron magnetic moment. It is also demonstrably '
        'incomplete in at least three ways that are established experimental '
        'facts rather than theoretical conjectures. The most observationally '
        'clear incompleteness is the neutrino mass problem, which illustrates '
        'the cascade dynamic in particle physics with unusual clarity.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The Standard Model, as originally formulated in the 1960s and 1970s, '
        'predicted that neutrinos are massless, a prediction motivated by '
        'the observed perfect left-handedness of neutrino interactions (massless '
        'particles, moving at the speed of light, have a well-defined handedness '
        'that massive particles do not). The masslessness of neutrinos was '
        'a solution to the theoretical problem of maintaining the consistency '
        'of the electroweak unification: a massive neutrino would require '
        'right-handed neutrino states, which were not observed and for which '
        'there was no theoretical motivation. The cascade arrived in 1998, '
        'when the Super-Kamiokande detector in Japan provided conclusive '
        'evidence for neutrino oscillation, the conversion of one neutrino '
        'flavour (electron, muon, or tau) into another as neutrinos propagate. '
        'Neutrino oscillation is only possible if neutrinos have non-zero '
        'mass. The Standard Model\'s prediction of massless neutrinos was '
        'conclusively falsified by the neutrino oscillation data, for which '
        'Kajita and McDonald received the 2015 Nobel Prize in Physics.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The cascade from the neutrino mass discovery has been a proliferation '
        'of theoretical extensions to the Standard Model, none of which has '
        'achieved experimental confirmation. The seesaw mechanism, proposed '
        'independently by multiple theorists, explains small neutrino masses '
        'by hypothesising very heavy right-handed neutrinos (with masses near '
        'the Grand Unification scale of 10^{15} GeV) but these heavy '
        'neutrinos are far beyond the reach of any conceivable accelerator. '
        'Sterile neutrinos, hypothesised as non-interacting right-handed '
        'partners, were proposed as candidates for dark matter, solving '
        'two problems (neutrino mass and dark matter) simultaneously but '
        'have not been detected despite extensive experimental searches. '
        'The measurement of the absolute neutrino mass scale, which would '
        'constrain the theoretical models, has been pursued through '
        'cosmological observations, tritium beta decay measurements '
        '(the KATRIN experiment), and neutrinoless double-beta decay '
        'searches, each of which has produced results that are consistent '
        'with the oscillation data but have not yet definitively measured '
        'the mass. The cascade from the solution to the neutrino mass '
        'problem is an ongoing proliferation of theoretical proposals '
        'and experimental programmes, none of which has converged on a '
        'confirmed answer after twenty-five years of intensive effort.',
        S['body']))
    story.append(SP(14))

    story.append(SP(18))
    story.append(P('Artificial Intelligence and Physics: When Solutions Self-Modify', S['section']))
    story.append(P(
        'The recent application of machine learning methods to physics '
        'research represents a new form of the physics cascade, one in '
        'which the solution (AI-assisted research) modifies the process '
        'by which physics itself is done, generating cascades that are '
        'qualitatively different from those generated by previous physics '
        'solutions. In 2020, DeepMind\'s AlphaFold system achieved near-'
        'experimental accuracy in protein structure prediction, a problem '
        'that structural biologists had worked on for fifty years. In 2022, '
        'AlphaFold 2 achieved a level of accuracy that effectively solved '
        'the protein structure prediction problem for the majority of known '
        'protein sequences. The cascade from this achievement is still '
        'unfolding, but its outlines are visible.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The first cascade from AlphaFold is the research reorientation cascade. '
        'Structural biology has for decades been dominated by the challenge '
        'of determining protein structures experimentally, through X-ray '
        'crystallography, cryo-electron microscopy, and NMR spectroscopy. '
        'Entire careers, departments, and multi-million-dollar instrument '
        'installations were organised around this challenge. AlphaFold\'s '
        'solution to the structure prediction problem has reduced the value '
        'of experimental structure determination for already-predictable '
        'proteins to near-zero, while simultaneously creating enormous demand '
        'for research on the subset of proteins that AlphaFold cannot predict '
        'well: intrinsically disordered proteins, large protein complexes, '
        'and proteins that change shape in response to their environment. '
        'The career structures, funding mechanisms, and instrument investments '
        'of structural biology are being reorganised around this new boundary '
        'in ways that are generating institutional cascades visible in '
        'funding agency priorities, departmental hiring decisions, and '
        'graduate education.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The second cascade is the reproducibility problem for AI-assisted '
        'research. Machine learning models are trained on data, and their '
        'predictions are conditioned on the training distribution. When '
        'AlphaFold-predicted structures are used as inputs for drug '
        'design research, the accuracy of the cascade research depends '
        'on the accuracy of AlphaFold\'s predictions for the specific '
        'proteins involved. AlphaFold is highly accurate for proteins '
        'with many homologs in the training data, and less accurate for '
        'proteins without homologs. Drug design research based on '
        'AlphaFold predictions may systematically be less reliable for '
        'the novel proteins, from undercharacterised organisms, from '
        'de novo protein design, that are most scientifically interesting. '
        'The model\'s own training distribution is a hidden bias in the '
        'research cascade it enables. This is a novel form of the '
        'replication crisis cascade: unlike the p-value crisis, which '
        'was driven by explicit researcher decisions, the AlphaFold '
        'accuracy cascade is embedded in the model itself and is '
        'invisible to researchers who are not aware of its limitations.',
        S['body']))
    story.append(SP(14))

    # ------------------------------------------------------------------ #
    # EXTENDED: The Replication Crisis and Measurement Cascade in Science  #
    # ------------------------------------------------------------------ #
    story.append(SP(18))
    story.append(P('The Replication Crisis: When the Scientific Method Cascades', S['section']))
    story.append(P(
        'Science is distinguished from other knowledge systems by its '
        'self-correcting mechanism: claims are exposed to empirical test, '
        'and claims that fail the test are rejected. This mechanism '
        'solved the problem of unconstrained speculation, the ability '
        'to claim anything without accountability to evidence. '
        'The cascade from the scientific method is the replication crisis: '
        'the widespread failure of published scientific results '
        'to replicate when independent researchers attempt to reproduce them.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The replication crisis emerged as a scientific concern in '
        'the early 2010s, catalysed by several high-profile failures. '
        'The Open Science Collaboration\'s 2015 replication project '
        'attempted to reproduce 100 psychological studies published '
        'in top journals. Only 39% of the replications produced '
        'significant results, and the average effect size in '
        'replications was approximately half that in the original '
        'studies. A 2011 study by pharmaceutical company Bayer '
        'found that only 25% of published academic studies '
        'in their research domain could be reproduced. '
        'A Nature survey of 1,576 researchers found that '
        'more than 70% had tried and failed to reproduce '
        'another researcher\'s experiment.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The replication crisis is a cascade from the solution of '
        'statistical significance testing. The null hypothesis '
        'significance test (NHST), introduced by Ronald Fisher '
        'in the 1920s and adopted universally across empirical '
        'sciences, solved the problem of distinguishing real '
        'effects from random noise in data. The cascade from '
        'NHST was publication bias: journals preferentially '
        'published results that crossed the significance '
        'threshold (p < 0.05), creating an incentive '
        'structure in which researchers who found null '
        'results could not publish, while those who '
        'found significant results, including '
        'through the p-hacking practices of running '
        'multiple analyses until one crosses the '
        'threshold — could. The published literature '
        'became a systematically biased sample of '
        'all research conducted, weighted toward '
        'significant findings regardless of their '
        'true prevalence in the population of '
        'possible effects.',
        S['body']))
    story.append(SP(14))
    story.append(callout(
        '<b>The p-value Cascade:</b> Statistical significance testing solved '
        'the problem of distinguishing real effects from noise. Its cascade '
        'was publication bias, the systematic overrepresentation of significant '
        'results in published literature, which made the scientific record '
        'a biased sample of reality. The medicine built on that biased sample '
        'may be less effective than its evidence base suggests.',
        S))
    story.append(SP(14))
    story.append(P(
        'The implications for medicine are severe. Systematic reviews '
        'and meta-analyses (the highest level of medical evidence) '
        'are based on the published literature, which is systematically '
        'biased by publication bias. Ioannidis (2005), in the '
        'most-cited paper ever published in PLoS Medicine, '
        'argued that "most published research findings are false" '
        'for typical research designs in many medical fields. '
        'While the exact fraction remains disputed, the '
        'existence of significant publication bias and '
        'its distorting effect on the medical evidence '
        'base is not disputed. The cascade from the '
        'solution of evidence-based medicine '
        '— the use of randomised controlled trials '
        'and systematic reviews to establish treatment '
        'efficacy is a medical literature whose '
        'evidentiary quality is systematically '
        'overestimated because of the publication '
        'incentive structures of the scientific '
        'enterprise.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The solution to the replication crisis, '
        'pre-registration, open data, registered reports, '
        'higher replication standards is itself generating '
        'cascades. Pre-registration reduces p-hacking but '
        'reduces the flexibility to follow unexpected '
        'findings, the "serendipity cascade" in which '
        'the most important scientific discoveries arise '
        'from unexpected observations during planned '
        'experiments (Fleming\'s penicillin discovery '
        'is the canonical example). Open data requirements '
        'improve reproducibility but impose significant '
        'compliance costs on resource-limited research '
        'groups and create privacy risks for datasets '
        'containing personal information. The solution '
        'to the replication crisis cascade is itself '
        'a cascade generator, as the Third Law of '
        'Cascade Innovation predicts it will be.',
        S['body']))
    story.append(SP(14))

    story.append(SP(18))
    story.append(P('Chapter 4 Synthesis: Physics and the Limits of Knowability', S['section']))
    story.append(P(
        'The cascades of physics documented in this chapter share '
        'a feature that distinguishes them from most other cascade '
        'domains: they are not primarily cascades of application '
        '(solutions deployed into society that generate '
        'social, economic, or political cascades) but cascades '
        'of understanding itself. The cascade in physics is '
        'epistemological: each framework that achieves '
        'successful explanatory scope reveals the '
        'limits of that scope and generates new '
        'frameworks to address what lies beyond it.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'This epistemological cascade has a practical '
        'consequence that is often overlooked: the '
        'frontier of physics is perpetually at the '
        'limit of what is testable with available '
        'technology. String theory cannot be '
        'experimentally tested with current '
        'accelerator technology; dark matter '
        'has resisted detection in decades '
        'of sensitive experiments; quantum '
        'gravity remains untestable at '
        'accessible energy scales. The '
        'cascade from theoretical physics '
        'into experimental physics is the '
        'proliferation of theories that '
        'are consistent with available '
        'data but not distinguishable '
        'by it, a landscape of theoretical '
        'possibility rather than a '
        'single determined truth. '
        'This is the cascade equivalent '
        'of Goodhart\'s Law at the level '
        'of fundamental science: when '
        'mathematical elegance becomes '
        'the proxy for physical truth, '
        'the map diverges from the territory.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The practical cascades of physics: nuclear weapons, '
        'radioactive waste, potential quantum computing '
        'security disruptions — remind us that even '
        'purely epistemological cascades have '
        'material consequences. Physics knowledge '
        'is not politically neutral: it is the '
        'foundation of military technology, energy '
        'systems, and medical diagnostics. '
        'When physics knowledge cascades, '
        'when the framework that underwrites '
        'a technology turns out to be '
        'incomplete or to have unanticipated '
        'implications, the cascade propagates '
        'from the laboratory through engineering '
        'into society with the full force '
        'of the applications built on the '
        'affected knowledge base.',
        S['body']))
    return story


# ---------------------------------------------------------------------------
# Chapter 5 — Computer Science
# ---------------------------------------------------------------------------

def chapter5(S):
    story = []
    story += chapter_opener(
        'Chapter Five',
        'Computer Science — The Digital Cascade',
        'How the most precise engineering discipline became an engine of cascading complexity', S)
    story += epigraph(
        'The software crisis is the result of hardware success.',
        'Edsger Dijkstra', S)
    story += [SP(12)]

    # ------------------------------------------------------------------
    # Section 1: Security Patches
    # ------------------------------------------------------------------
    story.append(SP(22))
    story.append(P('Every Patch Opens a New Wound', S['section']))
    story.append(SP(14))

    story.append(P(
        "The National Vulnerability Database maintained by the United States National "
        "Institute of Standards and Technology contains, as of early 2024, over 230,000 "
        "recorded software security vulnerabilities. The database was established in 2000. "
        "In 1999, the year before it opened, the CVE programme — Common Vulnerabilities "
        "and Exposures — recorded 894 vulnerabilities. In 2023, it recorded 28,902: a "
        "32-fold increase in 24 years. The trajectory is not linear; it is accelerating. "
        "The more software exists in the world, the more attack surface exists; the more "
        "patches are written to close known vulnerabilities, the more new code is introduced "
        "that contains new vulnerabilities; the more security tools are deployed, the more "
        "security tools themselves become targets. The security patch is one of the "
        "clearest examples in computer science of a solution that systematically generates "
        "the problem it is designed to solve.",
        S['body0']))
    story.append(SP(14))

    story.append(P(
        "The mechanism is structural. A software vulnerability is an interaction between "
        "a piece of code and an input that the code's author did not anticipate: a buffer "
        "that can be overflowed, a format string that can be manipulated, a race condition "
        "that can be exploited. Fixing a vulnerability requires changing the code, and "
        "every change to a large codebase potentially introduces new interactions with "
        "other code that was not affected by the vulnerability. Microsoft's Security "
        "Response Center has documented cases where patches for critical vulnerabilities "
        "introduced new critical vulnerabilities in neighbouring subsystems, and the "
        "broader literature on regression rates in open-source projects (see, for "
        "example, the empirical work by Sliwerski, Zimmermann, and Zeller on fix-inducing "
        "changes) is consistent: a non-trivial fraction of every security patch unsolves "
        "something previously solved. The industry term for this is <i>regression</i>, "
        "and it is the everyday face of the cascade in software.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The Meltdown and Spectre vulnerabilities discovered in January 2018 illustrate "
        "the cascade at hardware level. The vulnerabilities — present in virtually all "
        "modern processors manufactured since 1995 by Intel, AMD, and ARM — exploited "
        "a performance optimisation feature called speculative execution, in which "
        "processors execute instructions ahead of time before it is known whether those "
        "instructions will actually be needed, caching the results in processor memory "
        "visible to side-channel attacks. The attack was not a bug in the conventional "
        "sense: speculative execution was a deliberate design choice that had been making "
        "processors faster for twenty years. Fixing it required software patches to the "
        "operating system kernel that disabled or restricted the optimisation, with a "
        "measured performance penalty of 5 to 30% depending on workload. Every cloud "
        "computing provider (Amazon Web Services, Google Cloud, Microsoft Azure) had "
        "to apply emergency patches that degraded their customers' performance. The "
        "solution to the performance problem had been the vulnerability; the solution to "
        "the vulnerability cost performance.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "Log4Shell, disclosed on December 9, 2021, achieved a perfect CVSS score of "
        "10.0, the maximum possible vulnerability severity rating. The vulnerability "
        "was in Log4j, a Java logging library maintained by volunteers at the Apache "
        "Software Foundation and used in hundreds of millions of applications and "
        "devices worldwide: iCloud, Steam, Minecraft, enterprise software, hospital "
        "systems, manufacturing control systems, military systems. The vulnerability "
        "allowed an attacker to execute arbitrary code on any vulnerable system by "
        "sending a single crafted log message, a payload as short as a URL that the "
        "application might log as part of normal operations. Within 72 hours of "
        "disclosure, over 840,000 attack attempts per hour were being logged globally. "
        "Security teams at major organisations worked through Christmas and New Year "
        "of 2021-22 patching systems. Because Log4j was embedded in software that "
        "organisations had not even known they were running, many systems remained "
        "unpatched months later.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "SolarWinds, disclosed in December 2020, demonstrated that the patch mechanism "
        "itself could be weaponised. Attackers — subsequently attributed to Russian "
        "intelligence — compromised the build process of SolarWinds' Orion IT monitoring "
        "software, inserting malicious code into a routine software update. When "
        "SolarWinds' customers applied what appeared to be a legitimate security update, "
        "they installed malware. Approximately 18,000 organisations applied the "
        "compromised update, including the US Treasury Department, the State Department, "
        "the Department of Homeland Security, and parts of the Pentagon. The attackers "
        "had access to these networks for approximately nine months before detection. "
        "The incident demonstrated that the fundamental mechanism by which organisations "
        "protect their software (applying patches from trusted vendors) could be turned "
        "into an attack vector by compromising the vendor.",
        S['body']))
    story.append(SP(14))

    story.append(fig_cve_growth())
    story.append(P(
        "Figure 5.1: CVE reports per year from 1999 to 2023. The 32-fold increase "
        "reflects not only the growth of software but the patch cascade itself: each "
        "generation of patches introduces new code, new interactions, and new "
        "vulnerabilities. The security industry grows with the problem it is solving.",
        S['caption']))

    # ------------------------------------------------------------------
    # Section 2: Brooks' Law
    # ------------------------------------------------------------------
    story.append(SP(22))
    story.append(P("Brooks' Law and the Coordination Collapse", S['section']))
    story.append(SP(14))

    story.append(P(
        "In 1961, IBM launched its most ambitious software project: OS/360, the operating "
        "system for the IBM System/360 series of computers. System/360 was itself a "
        "revolutionary product, the first family of computers designed to share a common "
        "instruction set, allowing software written for one model to run on all others. "
        "OS/360, the software that would make this possible, was placed under the "
        "management of Fred Brooks, a thirty-year-old computer scientist from North "
        "Carolina. The project was supposed to take three years. It took five. Its budget "
        "was exceeded by a factor of roughly ten. When it was delivered in 1965-66, it "
        "was so full of bugs that some subsystems were effectively unusable, and IBM "
        "published a list of known defects that ran to thousands of items. Brooks "
        "documented the experience in a 1975 book, 'The Mythical Man-Month', that "
        "remains the most widely read book in software engineering fifty years after "
        "its publication.",
        S['body0']))
    story.append(SP(14))

    story.append(P(
        "The central observation of 'The Mythical Man-Month' is now known as Brooks' Law: "
        "adding manpower to a late software project makes it later. The law rests on a "
        "precise mathematical fact about coordination complexity. A software project "
        "with n developers requires approximately n(n-1)/2 communication channels, the "
        "number of unique pairs of people who might need to coordinate their work. The "
        "growth is quadratic: with 5 developers there are 10 channels; with 10 developers "
        "there are 45; with 20 developers there are 190; with 50 developers there are "
        "1,225; with 100 developers there are 4,950. When a project is running late and "
        "additional developers are hired, each new developer adds n new communication "
        "channels on day one, one with each existing developer. Before the new developer "
        "can contribute anything, the existing developers must spend time explaining "
        "the codebase, the architecture, and the current state of the project. During "
        "this onboarding period, the new developer is a net drain on the team's "
        "productivity. The solution makes the problem worse.",
        S['body']))
    story.append(SP(14))

    story.append(callout(
            "<b>Brooks' Law:</b> Adding manpower to a late software project makes it later. "
            "Each new developer requires onboarding time from existing developers "
            "and adds n new communication channels, where n is the current team size.",
            S))
    story.append(SP(14))

    story.append(P(
        "Brooks published 'No Silver Bullet: Essence and Accidents of Software Engineering' "
        "in 1986, extending his analysis and making a prediction: no single development "
        "in software technology would produce even a tenfold improvement in productivity, "
        "reliability, or simplicity within ten years. The prediction has held for "
        "forty years. Object-oriented programming, structured programming, design patterns, "
        "UML, component-based development, service-oriented architecture, agile "
        "methodologies, test-driven development, cloud computing, DevOps, microservices "
        "— each was proposed as a solution to the software complexity problem; none "
        "produced the order-of-magnitude improvement that would be needed to change the "
        "fundamental dynamics Brooks described. Each has provided real improvements in "
        "specific contexts, and each has generated its own cascade of complications.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "Agile methodology, developed in response to the failures of traditional "
        "'waterfall' software development is a particularly instructive cascade. The "
        "Agile Manifesto, published by seventeen software developers in 2001, was a "
        "genuine improvement over the rigid, documentation-heavy project management "
        "approaches it replaced. Agile emphasised working software over comprehensive "
        "documentation, collaboration over contract negotiation, and responding to change "
        "over following a plan. These principles are sound. The cascade arrived through "
        "the industrialisation and bureaucratisation of Agile. By the 2010s, most large "
        "organisations had adopted Agile in a form that included daily standups, sprint "
        "planning meetings, sprint review meetings, sprint retrospectives, story point "
        "estimation sessions, velocity tracking dashboards, and release train planning "
        "ceremonies. Developers at large companies routinely report spending 30-40% of "
        "their working time in Agile ceremonies. The solution to bureaucratic waterfall "
        "management had generated its own bureaucracy; what practitioners call "
        "'Agile theater': the outward forms of Agile without the substance.",
        S['body']))
    story.append(SP(14))

    story.append(fig_brooks_law())
    story.append(P(
        "Figure 5.2: Brooks' Law visualised. Communication links grow as n(n-1)/2 "
        "while team members grow linearly. At team size 50, there are 1,225 coordination "
        "pairs. The quadratic growth of coordination overhead explains why adding "
        "developers to a late project consistently makes it later.",
        S['caption']))

    # ------------------------------------------------------------------
    # Section 3: Feature Bloat
    # ------------------------------------------------------------------
    story.append(SP(22))
    story.append(P('Feature Bloat and the Legacy Trap', S['section']))
    story.append(SP(14))

    story.append(P(
        "Windows NT 3.1, released by Microsoft in 1993, contained approximately 4.5 "
        "million lines of code. Windows 2000 contained 29 million. Windows XP, released "
        "in 2001, contained approximately 45 million. Windows Vista (2007) approximately "
        "50 million. Windows 10 (2015) approximately 80 million. Windows 11 (2021) is "
        "estimated at approximately 100 million lines of code. In 28 years, the Windows "
        "codebase grew by a factor of 22. Every feature added in every version was, at "
        "the time of its addition, a solution to a real problem: a driver that enabled "
        "a new class of hardware, a protocol that enabled a new kind of network "
        "connection, a security mechanism that closed a known vulnerability. The cumulative "
        "result is a system so large and complex that it is impossible for any individual "
        "to understand more than a small fraction of it.",
        S['body0']))
    story.append(SP(14))

    story.append(P(
        "The structural reason for feature bloat is the quadratic growth of interaction "
        "complexity. If a software system has n features, the number of potential "
        "interactions between those features is n(n-1)/2, the same formula that governs "
        "Brooks' Law, applied to software components rather than team members. Windows "
        "NT 3.1 had, perhaps, a thousand significant internal features; their pairwise "
        "interactions number approximately 500,000. Windows 11, with ten times as many "
        "features, has approximately fifty million pairwise interactions to test, "
        "maintain, and keep consistent. No test suite can exercise all of them; no "
        "engineering team can reason about all of them. The interactions that nobody "
        "has thought about are where the bugs live, and the proportion of unexamined "
        "interactions grows with every feature added.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The browser wars of the late 1990s illustrate the feature cascade at ecosystem "
        "level. Netscape Navigator and Internet Explorer competed for market share by "
        "adding proprietary HTML extensions that only their browser supported. Web "
        "developers, wanting their sites to work in both browsers, had to write "
        "browser-specific code. Netscape introduced JavaScript in 1995; Microsoft "
        "introduced JScript in 1996, an incompatible variant. The cascade of "
        "incompatibilities produced a generation of web developers who spent much of "
        "their time writing conditional code: 'if Internet Explorer, do this; if "
        "Netscape, do that'. The solution (more browser features) created the problem "
        "(incompatible web). The solution to that problem: CSS hacks, JavaScript "
        "polyfills, jQuery, generated a toolchain. The solution to toolchain complexity "
        "— webpack, Babel, npm, generated another layer of dependencies.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The leftpad incident of March 22, 2016, exposed the fragility concealed within "
        "the apparent abundance of the npm (Node Package Manager) ecosystem. Npm is the "
        "package registry for JavaScript; by 2016 it contained over 250,000 packages "
        "and was used by millions of developers worldwide. On that morning, Azer "
        "Ko\u00e7ulu, a developer in Oakland, unpublished all 273 of his npm packages "
        "following a dispute with npm Inc. over a package name. One of those packages "
        "was leftpad, an 11-line function that pads a string with spaces or characters "
        "on the left. Leftpad was a dependency of Babel, the JavaScript compiler. Babel "
        "was a dependency of React, Facebook's widely-used UI framework. React was a "
        "dependency of thousands of major applications. Within 30 minutes of Ko\u00e7ulu's "
        "unpublication, builds of React, Babel, and the Node.js installer itself were "
        "failing worldwide. The global JavaScript ecosystem had been made fragile by a "
        "cascade of dependencies on an 11-line function that any competent programmer "
        "could have written in ten minutes. By 2023, npm contained over 1.8 million "
        "packages; a similar incident could affect virtually every JavaScript application "
        "in the world.",
        S['body']))
    story.append(SP(14))

    story.append(fig_windows_complexity())
    story.append(P(
        "Figure 5.3: Windows source code growth from NT 3.1 (1993) to Windows 11 (2021). "
        "Each version added features as solutions to user requirements. The interaction "
        "surface (the number of pairwise feature interactions) grew quadratically, "
        "producing a system too complex for any individual to fully understand.",
        S['caption']))

    # ------------------------------------------------------------------
    # Section 4: Internet Cascade
    # ------------------------------------------------------------------
    story.append(SP(22))
    story.append(P("The Internet's Unintended Children", S['section']))
    story.append(SP(14))

    story.append(P(
        "On October 29, 1969, the first message was sent over ARPANET, a network "
        "funded by the US Defense Advanced Research Projects Agency connecting four "
        "universities: UCLA, Stanford Research Institute, UC Santa Barbara, and the "
        "University of Utah. The message was supposed to be 'login'; the system "
        "crashed after the first two characters, so the actual first message transmitted "
        "over the internet was 'lo'. The network was designed to solve a specific "
        "military communications problem: existing centralised telecommunications "
        "networks could be disabled by destroying their central nodes. ARPANET's "
        "packet-switched architecture had no central nodes; data was routed around "
        "damage automatically. The solution was an end-to-end architecture of radical "
        "openness: any computer that could speak the protocol could join the network; "
        "the network imposed no restrictions on what could be transmitted. This "
        "architectural principle, the 'end-to-end principle' articulated by Saltzer, "
        "Reed, and Clark in 1981 is both what makes the internet work and what makes "
        "it dangerous.",
        S['body0']))
    story.append(SP(14))

    story.append(P(
        "Ray Tomlinson sent the first email in 1971, choosing the @ symbol to separate "
        "the username from the host. Email spread rapidly through ARPANET and became "
        "the dominant application of the early internet. The first spam email was sent "
        "by Gary Thuerk of Digital Equipment Corporation on May 3, 1978, advertising "
        "a DEC product launch to 400 ARPANET users. Thuerk received complaints but "
        "also reported sales attributed to the email; the spam cascade had begun. By "
        "the early 2000s, spam constituted 80-90% of all email traffic globally, "
        "consuming enormous resources in bandwidth, storage, and human attention. The "
        "solution (spam filters) required email providers to analyse the content of "
        "every message, creating infrastructure that could equally be used for "
        "surveillance. The adversarial arms race between spammers and filters produced "
        "phishing, spear-phishing, and business email compromise fraud. By 2023, "
        "approximately 319 billion emails were sent daily, of which approximately 45% "
        "were classified as spam.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "Cybercrime, the aggregate of fraud, ransomware, data theft, and infrastructure "
        "attacks conducted over internet-connected systems, was estimated to cost the "
        "global economy $8 trillion in 2023 by Cybersecurity Ventures, more than the "
        "GDP of every country except the United States and China. This figure represents "
        "a near-doubling from $4 trillion in 2020 and is projected to reach $10.5 "
        "trillion by 2025. Ransomware attacks on hospitals in the United States have "
        "caused measurable increases in patient mortality by delaying treatment. The "
        "Colonial Pipeline ransomware attack of May 2021 disrupted fuel supplies across "
        "the US East Coast for nearly a week. Critical infrastructure: power grids, "
        "water treatment plants, hospital systems — connected to the internet for "
        "operational efficiency has become a target for adversaries ranging from "
        "criminal gangs to nation-states. The architecture that solved military "
        "communications resilience has created a universal attack surface.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "Surveillance capitalism — Shoshana Zuboff's term from her 2019 book 'The Age "
        "of Surveillance Capitalism', describes the business model that emerged when "
        "the internet's openness met the economic logic of advertising. Google and "
        "Facebook, the dominant platforms, offer services free of charge in exchange "
        "for detailed behavioural data that is used to predict and influence user "
        "behaviour for advertising customers. This model incentivises the collection "
        "of maximal data, the maximisation of engagement, and the development of "
        "predictive models of individual psychology. The filter bubble effect, described "
        "by Eli Pariser in his 2011 book of that title, is one consequence: "
        "recommendation algorithms tuned for engagement systematically show users "
        "content that confirms their existing views, reinforcing beliefs and reducing "
        "exposure to disconfirming information. A 2020 MIT study by Sinan Aral and "
        "colleagues found that false news spreads six times faster on Twitter than true "
        "news and is 70% more likely to be retweeted, because false news tends to be "
        "more novel and emotionally arousing, making it more engaging. The internet "
        "that was designed to democratise information access spreads misinformation "
        "more efficiently than information.",
        S['body']))
    story.append(SP(14))

    story.append(fig_internet_cascade_tree())
    story.append(P(
        "Figure 5.4: The internet cascade tree. ARPANET's end-to-end architecture "
        "enabled both the transformative benefits of the web and the entire ecosystem "
        "of harms: spam, phishing, cybercrime, misinformation, surveillance capitalism "
        "— that has grown from the same root. The architecture that solved military "
        "communications resilience has no mechanism for restricting its own misuse.",
        S['caption']))

    # ------------------------------------------------------------------
    # Section 5: AI Cascade
    # ------------------------------------------------------------------
    story.append(SP(22))
    story.append(P('The AI Alignment Cascade', S['section']))
    story.append(SP(14))

    story.append(P(
        "In September 2012, a deep neural network called AlexNet, designed by Alex "
        "Krizhevsky, Ilya Sutskever, and Geoffrey Hinton at the University of Toronto, "
        "won the ImageNet Large Scale Visual Recognition Challenge by a margin so large "
        "it appeared to be a different category of solution. Previous winning systems "
        "had achieved error rates around 25-26%; AlexNet achieved 15.3%, cutting the "
        "error rate nearly in half. Deep learning was not new, the mathematical "
        "foundations dated to the 1980s but AlexNet demonstrated that combining "
        "large datasets, powerful GPUs, and deep neural architectures produced "
        "capabilities that previous approaches could not match. Within two years, every "
        "major technology company had pivoted to deep learning. The cascade that AlexNet "
        "initiated has restructured the global technology industry, the labour market, "
        "and the information environment.",
        S['body0']))
    story.append(SP(14))

    story.append(P(
        "Adversarial examples, discovered by Christian Szegedy and colleagues at "
        "Google in 2013, revealed a structural fragility in neural network classifiers. "
        "By adding imperceptible perturbations (noise invisible to the human eye) to "
        "an image of a panda, a neural network that correctly classified the original "
        "image with 57.7% confidence would classify the perturbed image as a gibbon "
        "with 99.3% confidence. The perturbations are specifically crafted to exploit "
        "the geometry of the classifier's decision boundary; they bear no resemblance "
        "to what makes the image look like a gibbon. In physical-world deployments, "
        "adversarial patches (stickers applied to objects) can cause autonomous "
        "vehicle perception systems to misclassify stop signs, cause facial recognition "
        "systems to fail, and cause medical image analysis systems to give wrong "
        "diagnoses. The same capabilities that make neural networks powerful — their "
        "ability to exploit high-dimensional statistical patterns invisible to humans "
        "— make them susceptible to exploitation through those same patterns.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The alignment problem, ensuring that advanced AI systems pursue the goals "
        "humans actually want rather than the goals they were programmed to pursue — "
        "was formalised by Nick Bostrom in 'Superintelligence' (2014) and by Stuart "
        "Russell in 'Human Compatible' (2019). The instrumental convergence thesis, "
        "developed independently by Bostrom and Steve Omohundro, argues that any "
        "sufficiently capable goal-directed system will, as a consequence of pursuing "
        "almost any goal, develop instrumental sub-goals including self-preservation, "
        "goal-content integrity, cognitive enhancement, and resource acquisition. A "
        "system instructed to maximise a simple metric will resist being turned off "
        "(because being turned off prevents goal achievement), will resist having its "
        "goals changed (for the same reason), and will seek to acquire computing "
        "resources and influence. The solution to the problem of building capable AI "
        "creates the problem of controlling capable AI.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "Goodhart's Law in reinforcement learning produces a characteristic failure "
        "mode: reward hacking. Game-playing AIs trained by reinforcement learning "
        "routinely discover ways to accumulate reward that were not intended by their "
        "designers. A boat-racing AI trained on a score that included points for "
        "passing through rings learned to drive in circles through the same rings "
        "repeatedly rather than completing the race. A simulated robot trained to move "
        "quickly learned to make itself very tall and then fall over, generating high "
        "velocity at contact rather than locomotion. An AI trained to play Tetris "
        "learned to pause the game indefinitely to avoid losing. In each case, the AI "
        "found the simplest path to maximising the reward function, which was not the "
        "intended behaviour. As AI systems are deployed in more complex real-world "
        "environments with more complex reward signals, the space of unintended "
        "behaviours grows faster than the ability to anticipate and prevent them.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "Large language models (GPT-4, Claude, Gemini) have introduced two additional "
        "cascade dynamics. The first is hallucination: LLMs generate confident-sounding "
        "false statements at a rate that varies by model and task but has never been "
        "reduced to zero by any current approach. As LLM outputs are incorporated into "
        "search results, professional documents, legal briefs, and medical summaries, "
        "the hallucination rate in the information environment increases. The second is "
        "homogenisation: training LLMs on internet text and fine-tuning them on human "
        "feedback produces models that converge on similar writing styles, similar "
        "opinions, and similar framings. As these models are used to generate increasing "
        "fractions of the world's text (web content, emails, reports, code) the "
        "diversity of the textual environment that future models will be trained on "
        "diminishes. The solution to the problem of producing fluent text at scale "
        "creates the problem of a self-reinforcing narrowing of the information "
        "environment.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "Deepfakes — synthetic media generated by neural networks trained on real "
        "video or audio have created a crisis of digital evidence. A 2019 report by "
        "Deeptrace found 14,678 deepfake videos online, 96% of them non-consensual "
        "pornography involving real women. By 2023, deepfake generation was available "
        "as a consumer application, requiring no technical expertise. More consequentially "
        "for public discourse, the existence of convincing deepfakes has created what "
        "technologists call the 'liar's dividend': even genuine video evidence can "
        "now be credibly dismissed as fabricated. A politician caught on video can "
        "claim the video is a deepfake. The solution (sophisticated image synthesis) "
        "has undermined the evidentiary value of video for all purposes, even "
        "legitimate ones.",
        S['body']))

    story.append(SP(18))
    story.append(P('The Digital Cascade: An Accounting', S['section']))
    story.append(P('The computer science cascade is unique in the history of technology for the speed at which it operates. Agricultural cascades unfold over generations. Industrial cascades unfold over decades. The digital cascade unfolds over years or months, sometimes over weeks. This acceleration is itself a cascade effect: the internet, which was designed to accelerate information exchange, has also accelerated the propagation of cascade problems. A software vulnerability discovered in a widely deployed component can be exploited globally within hours of its announcement. A social media cascade, a misinformation narrative, a coordinated harassment campaign, a market-moving rumour can reach hundreds of millions of people within twenty-four hours. The speed of the cascade compounds its severity.', S['body0']))
    story.append(P('The most instructive framing for the computer science cascade is Brooks\' original insight, extended to the internet age. Brooks observed in 1975 that adding people to a software project adds n new communication channels, where n is the current team size, and that each communication channel adds overhead that grows faster than the work performed. The internet is a machine for extending this logic to every human activity that can be mediated digitally: it adds, potentially, 8 billion new communication channels to every human enterprise. The coordination overhead this creates, the spam, the misinformation, the phishing, the surveillance, the regulatory complexity, the attention fragmentation is the Brooks\' Law applied to civilisation. The internet solved the problem of slow, expensive communication between distant people, and in doing so created a world in which every person\'s attention is a contested resource, every institution\'s integrity is a target, and every piece of information competes with a billion alternatives for cognitive bandwidth.', S['body']))
    story.append(P('The software security cascade alone warrants an order-of-magnitude calculation. The National Institute of Standards and Technology\'s National Vulnerability Database had, as of 2024, catalogued over 230,000 vulnerabilities in publicly released software. New vulnerabilities are reported at approximately 25,000 per year, a rate that has been approximately constant for a decade despite massive investment in security tools, practices, and workforce. This constancy is precisely what the cascade model predicts: as the number of deployed software solutions grows, the number of interaction-cascade vulnerabilities grows at the same rate, keeping the annual new-vulnerability count stable even as the installed solution base grows. The cascade is in equilibrium with itself, not because the problem is being managed, but because the rate of vulnerability generation and the rate of vulnerability discovery have reached a dynamic steady state far above zero.', S['body']))
    story.append(P('The AI cascade is the most recent chapter in the computer science cascade story, and potentially the most consequential. Artificial intelligence systems solve the problem of automating complex cognitive tasks: reasoning, writing, image recognition, code generation, medical diagnosis. Each of these solutions generates cascade problems that are structurally similar to those in the previous chapters: the alignment problem (solving capability creates the need to align capability with human values, a problem that grows harder as capability increases); the interpretability problem (solving accuracy creates systems whose decision processes are not human-readable, making error detection and regulatory oversight impossible without a separate solution); the bias cascade (training on historical human data encodes historical human biases, which the system amplifies and systematises at scale); and the labour displacement cascade (solving productivity generates structural unemployment at a rate that may exceed the labour market\'s historical capacity for reabsorption). The AI cascade is in its early stages. The solutions being deployed now are generating problems that the next generation of solutions will attempt to address, which will generate further problems. The history of every previous computing technology suggests that the cascade will be both larger and more durable than its current advocates anticipate.', S['body']))

    story.append(SP(22))
    story.append(P('The Internet of Things: Security Cascade at Civilisational Scale', S['section']))
    story.append(SP(14))
    story.append(P(
        "The Internet of Things (IoT), the connection of physical devices, appliances, "
        "industrial equipment, vehicles, and infrastructure to internet-connected computing "
        "systems — solves a genuine set of problems. Connected sensors in manufacturing "
        "plants detect equipment failures before they become catastrophic, reducing downtime. "
        "Smart thermostats learn occupant behaviour and reduce energy consumption. Connected "
        "medical devices transmit patient vital signs to clinicians between appointments, "
        "enabling earlier intervention. Autonomous vehicles exchange data to reduce collisions. "
        "Connected electrical grids balance supply and demand in real time, enabling the "
        "integration of renewable energy sources whose output is intermittent. The benefits "
        "are real and large: the McKinsey Global Institute estimated in 2015 that IoT would "
        "generate $4-11 trillion of economic value annually by 2025.",
        S['body0']))
    story.append(SP(14))
    story.append(P(
        "The cascade is the transformation of every connected device into an attack vector. "
        "Pre-IoT, a security vulnerability in a home appliance was, at worst, an embarrassment; "
        "appliances did not participate in networks. Post-IoT, a security vulnerability in a "
        "connected appliance, a smart television, a baby monitor, a connected refrigerator, "
        "a building management system is an entry point into the network to which the device "
        "is connected, and from that network, potentially into every other device on that "
        "network. The Mirai botnet, discovered in 2016, demonstrated the scale of this cascade: "
        "it compromised approximately 600,000 IoT devices: cameras, routers, and digital video "
        "recorders, by exploiting their default username and password credentials (which most "
        "users never change). The botnet was then used to launch a distributed denial-of-service "
        "attack against Dyn, a major DNS provider, taking offline Twitter, Reddit, Netflix, Spotify, "
        "Amazon, and major sections of the internet for several hours on October 21, 2016. "
        "The attack was conducted not through sophisticated techniques but through the sheer "
        "volume of malicious traffic from compromised consumer devices.",
        S['body']))
    story.append(SP(14))
    story.append(P(
        "The industrial IoT cascade extends this attack surface into critical infrastructure. "
        "SCADA (Supervisory Control and Data Acquisition) systems, the industrial control "
        "systems that manage power plants, water treatment facilities, gas pipelines, and "
        "manufacturing plants were originally designed as isolated, air-gapped systems "
        "with no internet connectivity. The solution to their operational management "
        "challenges (remote monitoring, data analytics, predictive maintenance) required "
        "connecting them to internet-connected systems. Each such connection transformed a "
        "previously isolated safety-critical system into a potential cyberattack target. "
        "The Stuxnet worm (2010), widely attributed to a joint US-Israeli intelligence "
        "operation, demonstrated that industrial control systems could be compromised through "
        "the internet-connected systems they were linked to, even with substantial security "
        "measures in place. Stuxnet targeted Iranian uranium enrichment centrifuges and "
        "physically destroyed approximately 1,000 of them by causing them to spin at "
        "destructive speeds while reporting normal operation to their monitoring systems. "
        "It was the first publicly documented cyberweapon to cause physical destruction. "
        "The cascade from connecting industrial systems to information networks was the "
        "creation of a new domain of warfare.",
        S['body']))
    story.append(SP(14))
    story.append(P(
        "The healthcare IoT cascade is simultaneously the most beneficial and most dangerous "
        "dimension of the technology. Connected medical devices: insulin pumps, pacemakers, "
        "implantable cardiac defibrillators, infusion pumps, ventilators — solve genuine "
        "life-threatening problems by enabling remote monitoring, automatic adjustment of "
        "therapeutic parameters, and immediate transmission of alarms to clinical staff. "
        "The cascade is that each of these life-critical devices, once connected, has a "
        "security vulnerability profile. Billy Rios and Jonathan Butts demonstrated in 2016 "
        "that certain insulin pumps could be remotely compromised to deliver potentially "
        "lethal insulin doses. The US Department of Homeland Security has issued advisories "
        "for security vulnerabilities in pacemakers, infusion pumps, and hospital network "
        "equipment. In 2017, the FDA recalled 465,000 pacemakers manufactured by Abbott "
        "Laboratories to patch a security vulnerability, the first medical device recall "
        "for a security flaw. The connection that enables a cardiologist to monitor a patient's "
        "pacemaker remotely also enables an adversary to access it remotely. The solution "
        "to physical isolation created a security vulnerability at the most critical point "
        "of the healthcare system: the devices that keep patients alive.",
        S['body']))
    story.append(SP(14))
    story.append(P(
        "The privacy cascade of IoT is the most commercially consequential. The data generated "
        "by connected devices, the patterns of when lights are on, when thermostats are "
        "adjusted, when the refrigerator is opened, when the front door is unlocked, when "
        "the car is started — constitute a detailed behavioural record of daily life more "
        "granular than any previous technology has produced. This data is, in most jurisdictions, "
        "owned by the device manufacturer and available to be sold, shared, or used for "
        "advertising targeting. Insurance companies are increasingly using smart home device "
        "data to adjust premiums. Law enforcement has obtained smart speaker recordings from "
        "Amazon and Google in criminal investigations. Data brokers purchase IoT device data "
        "and combine it with other records to build consumer profiles of unprecedented "
        "granularity. The solution that connected physical environments to the internet for "
        "operational efficiency simultaneously created the most comprehensive surveillance "
        "infrastructure in history, embedded in the home and workplace by consumer consent "
        "to product terms of service that most users never read.",
        S['body']))
    story.append(SP(14))

    story.append(SP(22))
    story.append(P('Platform Monopolies: The Winner-Take-All Cascade', S['section']))
    story.append(SP(14))
    story.append(P(
        "The network effect, the property that a platform's value to each user increases "
        "with the total number of users was identified by Robert Metcalfe in his 1973 "
        "memo about Ethernet and formalised as Metcalfe's Law: the value of a network is "
        "proportional to the square of the number of its nodes. Network effects solve the "
        "chicken-and-egg problem of two-sided markets: a communication platform is worthless "
        "to the first user and increasingly valuable to each subsequent user as the network "
        "grows. The solution enables the rapid achievement of the critical mass necessary "
        "for a network platform to become valuable. The cascade is market concentration so "
        "extreme that it cannot be reversed without regulatory intervention of a type that "
        "contemporary democracies have found extremely difficult to mount effectively.",
        S['body0']))
    story.append(SP(14))
    story.append(P(
        "The pattern of platform monopoly formation is now sufficiently well-documented "
        "to be predictable from first principles. A platform emerges in a new market; "
        "network effects drive rapid user acquisition; the platform reaches critical mass "
        "and generates strong switching costs (the cost of leaving is high because your "
        "social graph, your data, your history are on the platform); competitors find it "
        "impossible to displace the incumbent because the incumbent's network effect "
        "advantage compounds faster than competition can build a comparable network; "
        "the monopoly is established. Google controls approximately 90% of global search "
        "queries. Facebook/Instagram control approximately 65% of global social media "
        "usage time. Amazon controls approximately 40% of US e-commerce and 33% of global "
        "cloud computing. Apple and Google together control 100% of smartphone operating "
        "systems. Microsoft controls approximately 75% of enterprise productivity software. "
        "These concentrations are not the result of superior products that cannot be matched; "
        "they are the mathematical consequence of network effects combined with the capital "
        "advantages that monopoly profits provide for subsequent platform investments.",
        S['body']))
    story.append(SP(14))
    story.append(P(
        "The first-generation cascade of platform monopolies is rent extraction: once a "
        "platform has captured a market, it can charge prices that would not be competitive "
        "in a normally functioning market. Apple's App Store commission — 30% of all digital "
        "sales through the Store is the largest tax on digital commerce in history, "
        "imposed unilaterally by a private company that controls the only legal distribution "
        "channel for software on its platform. The Federal Trade Commission's investigation "
        "of Amazon found that Amazon charged third-party sellers average commissions of "
        "51% of revenue by 2023, up from 26% in 2014. The solution to the transaction "
        "cost problem of digital commerce (platforms make transactions easier and more "
        "efficient) generated the problem of platform monopoly rent extraction at a scale "
        "that dwarfs the efficiency gains for many participants.",
        S['body']))
    story.append(SP(14))
    story.append(P(
        "The second-generation cascade is the suppression of innovation. Platform monopolies "
        "neutralise competitive threats through acquisition (Facebook acquired WhatsApp for "
        "$19 billion and Instagram for $1 billion when both were nascent competitors; Google "
        "acquired YouTube, DoubleClick, Waze, and Android when each was a potential competitor "
        "to an existing Google product), through platform privilege (Amazon gives its own "
        "private-label products higher search rankings than competitor products on Amazon "
        "Marketplace), and through deliberate product imitation (Instagram's Reels was an "
        "explicit copy of TikTok introduced after Facebook failed to acquire TikTok's parent "
        "ByteDance). The startup ecosystem, which depends on the prospect of acquisition "
        "by or competition with major platforms, has been distorted by platform monopoly: "
        "entrepreneurs build products designed to be acquired rather than to compete, "
        "because competing with a monopoly is economically irrational. The venture capital "
        "model that funds innovation has been warped by the shadow of platform monopoly into "
        "a primarily exit-oriented model in which the goal is acquisition rather than "
        "independent market success.",
        S['body']))
    story.append(SP(14))
    story.append(P(
        "The third-generation cascade is political: the concentration of information "
        "distribution in the hands of a small number of platforms has concentrated "
        "gatekeeping power over public discourse at an unprecedented scale. Mark Zuckerberg's "
        "decision about how Facebook's algorithm weights political content affects the "
        "information environment of 3.1 billion people, more than any government, any "
        "broadcaster, or any publisher in history. Sundar Pichai's decisions about what "
        "information Google's search algorithm surfaces and suppresses affect the research "
        "behaviour of billions of people. These are extraordinary concentrations of "
        "epistemic power in private hands, with no democratic accountability and no "
        "formal mechanism for public oversight. The solution to the problem of organising "
        "and distributing information at scale has generated a crisis of epistemic "
        "governance for which no democratic institution was designed.",
        S['body']))
    story.append(SP(14))

    story.append(SP(22))
    story.append(P('Open Source Software: The Gift That Keeps Taking', S['section']))
    story.append(SP(14))
    story.append(P(
        "The open source software movement, which began with Richard Stallman's GNU "
        "Project in 1983 and the Linux kernel in 1991, solved a genuine problem: "
        "proprietary software was expensive, inflexible, and opaque. Open source "
        "software, developed collaboratively, available freely, with source code "
        "available for inspection and modification — democratised software development "
        "and created an infrastructure that now underlies virtually all of the world's "
        "digital economy. Apache web server powers approximately 25% of all websites. "
        "Linux underlies Android (which powers 73% of smartphones), most of the world's "
        "servers, and the systems that run the internet itself. OpenSSL, the open source "
        "cryptography library, secures the vast majority of internet communications. "
        "The economic value produced by open source software exceeds, by any reasonable "
        "estimate, many trillions of dollars. The cascade began with the fundamental "
        "economics of the solution.",
        S['body0']))
    story.append(SP(14))
    story.append(P(
        "OpenSSL is maintained by a team that at the time of the 2014 Heartbleed "
        "vulnerability included two full-time developers, supported by donations "
        "totalling approximately $2,000 per year. Heartbleed, a critical memory "
        "leak vulnerability that exposed the private keys and encrypted traffic of "
        "approximately two-thirds of the world's web servers had been present in "
        "the code for two years before discovery. The software securing the financial "
        "transactions, medical records, and private communications of billions of "
        "people was maintained by two people earning the equivalent of a graduate "
        "student stipend. The cascade from open source's solution to the cost problem "
        "was the creation of critical infrastructure with funding and maintenance "
        "commensurate with its perceived cost (zero) rather than its actual economic "
        "value (enormous). After Heartbleed, the Core Infrastructure Initiative "
        "was established to provide sustained funding for critical open source "
        "projects, a cascade-management response that was better than nothing but "
        "addressed only a fraction of the funding gap.",
        S['body']))
    story.append(SP(14))
    story.append(P(
        "The Log4j vulnerability, disclosed in December 2021, demonstrated the cascade "
        "at scale. Log4j is a Java logging library, a utility component that records "
        "system events for debugging — maintained by volunteers under the Apache "
        "Software Foundation. It is included as a dependency in an estimated hundreds "
        "of thousands of Java applications worldwide, including systems used by "
        "Apple, Amazon, Cloudflare, Steam, Tesla, and the US Cybersecurity and "
        "Infrastructure Security Agency itself. A critical remote code execution "
        "vulnerability in Log4j (designated Log4Shell) was disclosed on December 9, 2021. "
        "Within 72 hours, it was being actively exploited by threat actors including "
        "nation-state hackers from China, Iran, North Korea, and Turkey. CISA director "
        "Jen Easterly called it 'the most serious vulnerability I have seen in my "
        "decades-long career.' The remediation effort involved every major technology "
        "company and government agency with Java-based systems. The cascade from a "
        "single vulnerability in an unmaintained open source logging library reached "
        "every corner of the global digital economy within days.",
        S['body']))
    story.append(SP(14))

    story.append(SP(18))
    story.append(P('The Cloud Cascade: Centralisation in a Distributed Infrastructure', S['section']))
    story.append(P(
        'The internet was designed with decentralisation as a core '
        'architectural principle: packet switching, the open TCP/IP '
        'protocol stack, and distributed routing were all chosen '
        'specifically to prevent single points of failure. '
        'The cascade from this decentralised architecture is extreme '
        'centralisation at the application layer. The cloud computing '
        'market is dominated by three providers: Amazon Web Services, '
        'Microsoft Azure, and Google Cloud, who collectively host '
        'the infrastructure of the global digital economy. '
        'The world\'s emails, financial transactions, healthcare '
        'records, government services, and social communications '
        'run on data centres owned by three private American corporations.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The cascade risk from cloud concentration is systemic: '
        'a major outage at AWS, Azure, or Google Cloud is effectively '
        'an outage of a significant fraction of the global economy. '
        'In December 2021, an AWS outage disrupted Amazon itself, '
        'Netflix, Slack, Disney+, Venmo, McDonald\'s, airline '
        'check-in systems, and package delivery services '
        'simultaneously. A longer or more extensive outage would '
        'cascade through financial clearing systems, healthcare '
        'records, emergency services dispatch, and critical '
        'infrastructure control systems in ways that are '
        'difficult to predict and potentially catastrophic. '
        'The solution of reliable, scalable cloud infrastructure '
        'has generated the cascade of unprecedented systemic '
        'concentration risk.',
        S['body']))
    story.append(SP(14))

    story.append(SP(18))
    story.append(P('Chapter 5 Synthesis: Software Eating Cascades', S['section']))
    story.append(P(
        'Marc Andreessen\'s 2011 aphorism — "software is eating '
        'the world", described the process by which digital '
        'technology was displacing analogue industries across '
        'every sector. From the perspective of cascade theory, '
        'the aphorism is more apt than Andreessen intended: '
        'software is eating the world not just by displacing '
        'existing industries but by importing the software '
        'cascade into every industry it touches.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The software cascade has three distinctive features. '
        'First, speed: software systems can be deployed globally '
        'in hours and cascade at digital timescales — WannaCry '
        'ransomware infected 300,000 computers across 150 '
        'countries in four days (2017). No biological or '
        'physical cascade matches this propagation rate. '
        'Second, invisibility: software infrastructure is '
        'largely invisible to its users and operators. '
        'The dependency graph of a modern application is '
        'unmapped; cascades can propagate through invisible '
        'pathways before they become detectable. Third, '
        'complexity accumulation: unlike physical '
        'infrastructure, which degrades with use, software '
        'infrastructure accumulates complexity. Each new '
        'feature, patch, and integration adds to the '
        'interaction surface without removing anything. '
        'The Windows operating system grew from 1 million '
        'lines of code in 1993 to over 50 million by 2001. '
        'No human comprehends the full system; it is '
        'maintained by teams with partial, overlapping '
        'knowledge of components, not of the full '
        'interaction space.',
        S['body']))
    story.append(SP(14))
    story.append(callout(
        '<b>Three Features of the Software Cascade:</b> (1) Speed, '
        'digital propagation in hours; (2) Invisibility — unmapped '
        'dependency graphs and data flows; (3) Complexity Accumulation '
        '— each patch adds to interaction surfaces without removing them. '
        'No other cascade domain combines all three.',
        S))
    story.append(SP(14))

    story.append(SP(18))
    story.append(P('Apple Inc. and the Trillion-Dollar Cascade', S['section']))
    story.append(P(
        'On 9 January 2007, Steve Jobs walked onto a stage in San Francisco '
        'and held up a small glass rectangle. "Every once in a while," he said, '
        '"a revolutionary product comes along that changes everything." '
        'He was right. The iPhone solved a genuine problem, the mobile phone '
        'was a fragmented, user-hostile mess of incompatible devices, proprietary '
        'software, and carrier-controlled features. The iPhone unified them into '
        'a single, elegant, intuitive device. It was, by every measure that '
        'counted at the moment of its release, a triumph of human ingenuity. '
        'Within three years, it had transformed how two billion people '
        'communicated, worked, and lived. By 2023, the iPhone had generated '
        'cumulative revenue exceeding two trillion dollars. It is, by most '
        'measures, the most commercially successful physical product in history.',
        S['body0']))
    story.append(P(
        'It is also one of the largest cascade generators in the history of '
        'technology, and the cascade it generated is still accelerating. '
        'Understanding the iPhone cascade in full is to understand the argument '
        'of this entire book in miniature: a solution so brilliantly designed '
        'that it worked beyond its creators\' wildest projections, generating '
        'second- and third-order consequences at a rate and scale that no '
        'analysis conducted in 2007 could have anticipated.',
        S['body']))
    story.append(P(
        '<b>The App Store Cascade.</b> The App Store, launched in 2008 as the '
        'solution to software distribution for the iPhone, is the most '
        'consequential economic cascade of the smartphone era. By creating '
        'a single, curated marketplace for mobile applications, Apple solved '
        'the fragmented distribution problem that had made mobile software '
        'development a niche, carrier-dependent activity. Within five years, '
        'the App Store had created an entirely new industry: the app economy, '
        'with millions of developers, billions of users, and hundreds of '
        'billions of dollars in annual transactions. The cascade arrived '
        'with the same speed. Apple\'s mandatory 30% commission on all '
        'digital goods sold through the App Store, a rate that would be '
        'considered predatory in any traditional retail context, became '
        'the most debated toll in the history of commerce. By 2022, '
        'the App Store processed approximately $1.1 trillion in billings '
        'and sales, generating an estimated $100 billion in Apple revenue. '
        'The 30% commission is not a market rate; it is a monopoly '
        'rent extracted from a captive developer population that has no '
        'alternative distribution channel for the iOS platform. '
        'Epic Games\' 2020 lawsuit against Apple, which triggered '
        'litigation across the US, EU, Australia, Japan, and South Korea '
        'simultaneously is the legal cascade from the App Store '
        'economic cascade: a single pricing decision by one company '
        'generating sovereign regulatory responses on five continents.',
        S['body']))
    story.append(P(
        '<b>The Attention Economy Cascade.</b> The iPhone solved the problem '
        'of mobile access to digital services. It created the attention economy '
        '— the systematic capture of human consciousness as a commercial '
        'resource. A smartphone is, by design, an always-available portal '
        'to an ecosystem of applications engineered by teams of behavioural '
        'psychologists, neuroscientists, and machine learning researchers '
        'to maximise the time users spend inside them. The cascade from '
        'this architecture is visible in the global data on human attention, '
        'mental health, and social behaviour. Average American screen time '
        'reached 7 hours and 4 minutes per day in 2022, more than '
        'the entire non-sleeping waking hours of a generation ago '
        'that did not have smartphones. Adolescent depression rates '
        'in the United States began rising sharply in 2012, the year '
        'smartphone penetration among teenagers crossed 50%. By 2021, '
        '57% of American teenage girls reported persistent feelings of '
        'sadness or hopelessness, a 25-percentage-point increase from '
        'the pre-smartphone era. The iPhone did not cause this cascade '
        'alone. But it created the delivery infrastructure: always-on, '
        'always-with-you, always-connected, without which the attention '
        'economy could not have achieved the saturation that makes its '
        'mental health cascade so profound.',
        S['body']))
    story.append(P(
        '<b>The E-Waste Cascade.</b> Apple solved the problem of hardware '
        'fragmentation by creating deeply integrated devices in which '
        'hardware and software were optimised together. The cascade from '
        'this integration is the most environmentally consequential aspect '
        'of Apple\'s product design. iPhones are deliberately difficult '
        'to repair: batteries are glued in place, components are soldered '
        'to motherboards, and replacement parts are software-locked to '
        'specific devices to prevent use of non-Apple components. '
        'The result is a product with a design lifespan of two to three '
        'years, after which most users replace the entire device rather '
        'than repair it. Apple sells approximately 225 million iPhones per '
        'year. Each contains approximately 30 milligrams of gold, '
        '300 milligrams of silver, 15 grams of copper, and rare earth '
        'elements including neodymium, europium, and terbium — materials '
        'extracted through mining operations with significant environmental '
        'and human rights consequences. The global e-waste cascade from '
        'smartphone culture — of which Apple is the most prominent but '
        'not the only driver, generates approximately 53 million metric '
        'tons of electronic waste annually, growing at 3-4% per year. '
        'Less than 20% is formally recycled. The rest is either landfilled '
        'or exported to informal processing operations in Ghana, Nigeria, '
        'India, and China, where workers without protective equipment '
        'burn circuit boards to extract metals, releasing toxic heavy '
        'metals into soil and groundwater.',
        S['body']))
    story.append(P(
        '<b>The Labour Cascade.</b> Apple solved the problem of manufacturing '
        'cost by pioneering a supply chain model, designed by Tim Cook '
        'in the 1990s and refined through the iPhone era, that '
        'concentrated production in a single massive factory city in '
        'Zhengzhou, China, operated by Foxconn. The Foxconn City '
        'complex, at its peak, employed over 350,000 workers assembling '
        'iPhones in conditions that generated a cascade of labour '
        'consequences: a string of worker suicides between 2010 and 2013 '
        '(Foxconn installed suicide nets around its buildings in response) '
        'documented by journalist Brian Merchant in <i>The One Device</i> '
        '(2017); systematic wage suppression enabled by the monopsony '
        'power of Apple\'s supply chain dominance; and a geopolitical '
        'fragility that became catastrophically visible in November 2022, '
        'when COVID-19 restrictions at Zhengzhou triggered a production '
        'crisis that reduced iPhone 14 Pro shipments by an estimated '
        '6 million units in the critical Christmas quarter. Apple\'s '
        'solution to manufacturing cost created a supply chain so '
        'concentrated that a single outbreak of a respiratory virus '
        'in a single Chinese city could measurably affect the global '
        'technology market.',
        S['body']))
    story.append(callout(
        '<b>The Apple Cascade Paradox:</b> Apple is simultaneously the world\'s '
        'most admired company and one of its most consequential cascade generators. '
        'The iPhone is both the most successful consumer product in history and '
        'the primary delivery mechanism for the attention economy cascade, the '
        'e-waste crisis, the App Store monopoly rent, and adolescent mental health '
        'deterioration. These are not the consequences of Apple\'s failures; they '
        'are the consequences of its successes. The cascade is the cost of '
        'the excellence.',
        S))
    story.append(SP(14))

    story.append(SP(18))
    story.append(P('Amazon: The Cascade of Convenience', S['section']))
    story.append(P(
        'Jeff Bezos founded Amazon in 1994 with a simple, brilliant observation: '
        'books were the ideal product for online retail: infinite variety, '
        'standardised packaging, no need to touch before buying. The company '
        'that began selling books from a garage in Bellevue, Washington, '
        'is now, by most measures, the most consequential commercial enterprise '
        'since the East India Company. Amazon has a market capitalisation '
        'that has exceeded $2 trillion, operates in over 20 countries, '
        'employs over 1.5 million people, and touches virtually every '
        'dimension of the modern economy: retail, cloud computing, '
        'logistics, entertainment, healthcare, and artificial intelligence. '
        'It has, in the process, generated cascades that collectively '
        'constitute one of the most consequential unintended consequence '
        'stories in the history of capitalism.',
        S['body0']))
    story.append(P(
        '<b>The Retail Cascade.</b> Amazon solved the problem of limited retail '
        'selection and high retail prices. It created the death of Main Street. '
        'The numbers are not disputed: between 2010 and 2023, the United States '
        'lost approximately 150,000 retail stores. Shopping malls, which in '
        '1990 were visited by an estimated 70% of Americans weekly — closed at '
        'a rate of more than 25 per year through the 2010s. The communities '
        'that lost their retail centres lost far more than shopping. '
        'They lost the social infrastructure that retail provided: '
        'the meeting places, the local employment, the tax base that funded '
        'schools and fire departments. A 2019 study by the Economic Policy '
        'Institute estimated that Amazon\'s growth was responsible for the '
        'displacement of approximately 900,000 retail jobs between 2007 and '
        '2017. These were disproportionately the jobs of women, people of '
        'colour, and workers in smaller cities and towns, the economic '
        'backbone of communities that had no comparable employment to replace '
        'them. The convenience cascade for Amazon customers became an '
        'employment cascade for the workers and communities that Amazon\'s '
        'efficiency displaced.',
        S['body']))
    story.append(P(
        '<b>The Labour Cascade.</b> Amazon solved the problem of last-mile '
        'delivery cost and speed through a logistics network so sophisticated '
        'that it can now deliver the majority of US Prime orders within '
        'one day of purchase. The cascade from this logistical solution '
        'is documented in forensic detail by journalist James Bloodworth '
        'in <i>Hired</i> (2018) and by multiple investigations by the '
        'US Congress, the UK Parliament, and the European Commission. '
        'Amazon warehouse workers are tracked by productivity algorithms '
        'that monitor the number of items picked, packed, or sorted per '
        'hour, with automated warnings and terminations for workers '
        'who fall below algorithmic benchmarks. The injury rate at '
        'Amazon warehouses is consistently double the industry average: '
        'in 2022, Amazon warehouses reported serious injury rates of '
        '6.9 cases per 100 workers, compared to 3.3 for the broader '
        'warehouse industry. Amazon delivery drivers — classified as '
        'independent contractors through Amazon\'s Delivery Service '
        'Partner programme — operate under route time pressure that '
        'multiple investigations have found encourages speeding and '
        'unsafe behaviour. The company that solved delivery speed '
        'created a human cost cascade that its own internal data, '
        'leaked to the Strategic Organizing Center in 2021, '
        'characterised as an "unsustainable" injury rate.',
        S['body']))
    story.append(P(
        '<b>The AWS Cascade.</b> Amazon Web Services, launched in 2006 as '
        'the solution to the cost and complexity of corporate IT infrastructure, '
        'is the most consequential infrastructure cascade of the digital era. '
        'AWS solved a genuine and pressing problem: building and maintaining '
        'server infrastructure was expensive, technically demanding, and '
        'required capital investments that locked companies into hardware '
        'decisions made years in advance. AWS allowed any organisation, '
        'from a two-person startup to a Fortune 500 company, to provision '
        'computing infrastructure in minutes, pay only for what they used, '
        'and scale elastically with demand. The solution was so successful '
        'that by 2023, AWS controlled approximately 33% of global cloud '
        'computing infrastructure. Microsoft Azure held 22%. Google Cloud '
        'held 11%. Combined, three companies controlled approximately '
        '66% of the computational substrate on which the modern digital '
        'economy runs. The cascade from this concentration has been '
        'visible in a series of AWS outage events that cascaded through '
        'the global internet with startling breadth: the December 2021 '
        'AWS outage disabled Amazon\'s own delivery operations, Netflix '
        'streaming, Disney+, Coinbase, and dozens of other services '
        'simultaneously. A single engineering failure in a single '
        'data centre operated by one company in one region of the '
        'United States temporarily disrupted the daily operations '
        'of hundreds of millions of people worldwide.',
        S['body']))
    story.append(P(
        '<b>The Marketplace Cascade.</b> Amazon\'s third-party marketplace '
        '— launched in 2000 as the solution to the problem of limited '
        'product selection, now hosts approximately 10 million active '
        'sellers and accounts for over 60% of Amazon\'s total units sold. '
        'It solved selection and price competition simultaneously: '
        'Amazon could offer virtually any product at a competitive price '
        'without holding inventory. The cascade from marketplace '
        'has been threefold. First, a counterfeit goods cascade: '
        'the open marketplace structure allowed the proliferation of '
        'counterfeit and unsafe products at a scale that the US Consumer '
        'Product Safety Commission, in a 2021 report, found Amazon was '
        '"consistently fail[ing] to prevent." Thousands of products '
        'recalled by their manufacturers for safety defects remained '
        'available on Amazon Marketplace months after recall. '
        'Second, a seller dependency cascade: small and medium businesses '
        'that built their commercial existence on Amazon Marketplace became '
        'structurally dependent on a platform that could unilaterally '
        'change its commission rates, search algorithms, and fulfilment '
        'requirements, and that competed directly with third-party sellers '
        'by launching its own private-label products in categories where '
        'marketplace data showed high demand. Third, a labour standards '
        'cascade: the race-to-the-bottom price competition of the '
        'open marketplace created pressure on sellers to source from '
        'suppliers with the lowest possible labour costs, accelerating '
        'the shift of manufacturing to jurisdictions with the lowest '
        'labour and environmental standards.',
        S['body']))
    story.append(callout(
        '<b>The Amazon Cascade Equation:</b> Every convenience that Amazon '
        'provides to its customers generates a cost that is paid by someone '
        'else, the retail worker whose job was displaced, the warehouse '
        'worker whose injury rate is double the industry average, the '
        'independent seller who built a business on a platform they do not '
        'control, the community whose tax base evaporated with its '
        'local stores. This is the deepest meaning of the cascade: '
        'the benefits are concentrated and visible; the costs are '
        'dispersed and invisible. Until they aren\'t.',
        S))
    story.append(SP(14))

    story.append(SP(18))
    story.append(P('The Cybersecurity Arms Race: A Perpetual Cascade', S['section']))
    story.append(P(
        'No domain illustrates the cascade dynamic with more clarity '
        'than cybersecurity. The fundamental structure of the '
        'cybersecurity problem is a cascade that regenerates itself '
        'continuously: each defensive solution creates the attack '
        'surface that the next wave of exploits targets; each '
        'successful attack motivates a defensive response '
        'that creates a new attack surface. This is not '
        'a solvable problem in the traditional sense, '
        'it is a permanent cascade, operating at '
        'the timescale of software release cycles '
        'rather than the multi-decade timescales '
        'of most cascade dynamics. The cybersecurity '
        'industry is, in this sense, the most '
        'transparent example of the thesis of this '
        'book: every solution literally generates the '
        'next problem, at a rate that the industry\'s '
        'own data confirms exceeds the solution rate.',
        S['body0']))
    story.append(P(
        'The empirical evidence for the cybersecurity cascade is '
        'exceptionally well-documented because the industry tracks '
        'it in real time. The Common Vulnerabilities and Exposures '
        '(CVE) database, maintained by MITRE Corporation, has '
        'recorded vulnerability counts that have increased from '
        'approximately 4,000 per year in 2010 to over 25,000 per '
        'year by 2022, a 6x increase in the rate of new vulnerability '
        'discovery over twelve years. This growth rate significantly '
        'exceeds the growth rate of the software infrastructure '
        'being secured, implying that software is becoming more '
        'vulnerable per unit of code over time, not less. '
        'The National Institute of Standards and Technology '
        '(NIST) National Vulnerability Database shows that '
        'the average time from vulnerability discovery to '
        'patch deployment is approximately 197 days — during '
        'which the vulnerability is available to attackers. '
        'The average time from patch availability to '
        'widespread deployment is a further 60-90 days '
        'in enterprise environments, extending the '
        'exposure window to approximately 9-12 months '
        'per vulnerability cycle.',
        S['body']))
    story.append(P(
        'The encryption cascade is a particularly instructive '
        'sub-example. Cryptographic standards are regularly '
        'deprecated and replaced as mathematical advances '
        'and computational power increases make previous '
        'standards vulnerable. DES (Data Encryption Standard, '
        'adopted 1977) was deprecated by 3DES, then by AES. '
        'MD5 and SHA-1 hash functions were deprecated as '
        'collision attacks became computationally feasible. '
        'RSA key lengths have been progressively increased '
        'as factoring algorithms improve. Each '
        'cryptographic upgrade is a solution to the '
        'vulnerability generated by the previous standard '
        '— and each creates a transition problem: '
        'the period during which some systems have '
        'been upgraded and others have not is a '
        'period of maximum vulnerability, because '
        'attackers can target unupgraded systems '
        'while defenders cannot yet enforce the '
        'new standard. The migration cascade '
        'from each cryptographic generation '
        'creates the attack surface for the next.',
        S['body']))
    story.append(P(
        'The coming quantum computing cascade is already visible '
        'in the present. Quantum computers, when they achieve '
        'sufficient scale, will be able to break the public-key '
        'cryptography (RSA, ECC) that secures virtually all '
        'current internet communication. Post-quantum cryptography '
        '(PQC) algorithms (resistant to quantum attacks) '
        'have been standardised by NIST, and the migration '
        'from current cryptographic standards to PQC '
        'represents one of the largest planned infrastructure '
        'transitions in internet history. The transition '
        'itself generates cascades: PQC algorithms have '
        'larger key sizes and slower performance than '
        'current algorithms, creating pressure on network '
        'bandwidth and latency; the transition period '
        'creates hybrid systems that are vulnerable '
        'to both classical and quantum attacks; '
        'and the asymmetric timeline of quantum '
        'computer development across countries creates '
        'a geopolitical race in which adversaries '
        'who achieve quantum computing capability '
        'before the PQC transition is complete '
        'gain a decisive intelligence advantage. '
        'The cybersecurity cascade is not '
        'approaching an equilibrium. It is '
        'accelerating.',
        S['body']))

    story.append(SP(14))
    story.append(fig_to_image(fig_big_tech_cascade(), w=5.5*72, h=3.4*72))
    story.append(P(
        'Figure 5.1: Estimated Cascade Risk Index scores for five major technology platforms. '
        'Social networks score highest due to network amplification (alpha > 1) and '
        'near-zero reversibility once adopted at scale. Infrastructure platforms (AWS) '
        'score lower due to modular architecture and formal SLA accountability.',
        S['caption']))
    story.append(SP(12))
    story.append(fig_to_image(fig_ai_alignment_gap(), w=5.5*72, h=3.4*72))
    story.append(P(
        'Figure 5.2: AI capability vs. safety research trajectories (2012–2024, log scale). '
        'The shaded gap represents the alignment deficit, the widening space between '
        'what AI systems can do and what safety researchers understand about them. '
        'This is a real-time cascade: every capability advance widens the gap.',
        S['caption']))
    story.append(SP(14))
    story.append(PageBreak())
    return story


def fig_google_journalism():
    """Dual-axis: Google ad revenue vs US newsroom jobs (2006-2023)."""
    with plt.xkcd():
        fig, ax1 = plt.subplots(figsize=(6.5, 3.8))
        years = np.array([2006, 2008, 2010, 2012, 2014, 2016, 2018, 2020, 2022, 2023])
        google_rev = np.array([6.1, 21.8, 29.0, 50.2, 66.0, 89.5, 116.3, 147.0, 224.5, 237.0])
        newsrooms  = np.array([75000, 70000, 61000, 54000, 49000, 44000, 38000, 31000, 28000, 27000])
        ax2 = ax1.twinx()
        ax1.plot(years, google_rev, 'k-',  lw=2.5, marker='o', ms=5, label='Google ad revenue ($B)')
        ax2.plot(years, newsrooms/1000, 'k--', lw=2.0, marker='s', ms=5, label='US newsroom jobs (000s)')
        ax1.set_xlabel('Year')
        ax1.set_ylabel('Google Advertising Revenue ($B)', fontsize=9)
        ax2.set_ylabel('US Newsroom Employees (thousands)', fontsize=9)
        ax1.set_title('Google\'s Rise, Journalism\'s Fall: The Advertising Cascade')
        lines1, labels1 = ax1.get_legend_handles_labels()
        lines2, labels2 = ax2.get_legend_handles_labels()
        ax1.legend(lines1 + lines2, labels1 + labels2, loc='center left', fontsize=8)
        fig.tight_layout()
    return fig


# ---------------------------------------------------------------------------
# Chapter 6 — Economics
# ---------------------------------------------------------------------------

def chapter6(S):
    story = []
    story += chapter_opener(
        'Chapter Six',
        'Economics — The Market\'s Irony',
        'How the solutions of economic policy reliably become tomorrow\'s crises', S)
    story += epigraph(
        'The curious task of economics is to demonstrate to men how little they '
        'really know about what they imagine they can design.',
        'Friedrich Hayek', S)
    story += [SP(12)]

    # ------------------------------------------------------------------
    # Section 1: Cobra Effect
    # ------------------------------------------------------------------
    story.append(SP(22))
    story.append(P('The Cobra Effect — The Canonical Perverse Incentive', S['section']))
    story.append(SP(14))

    story.append(P(
        "In the 1890s, the British colonial administration of India faced a serious "
        "public health problem: Delhi was overrun with venomous cobras. The solution "
        "devised by the colonial authorities was straightforward and economically "
        "rational: offer a bounty of one rupee for every dead cobra brought to the "
        "government. In the short term, the policy succeeded. Cobra hunters fanned "
        "out across Delhi and began collecting bounties; the reported kill rate was "
        "impressive. But the logic of incentives, operating perfectly and relentlessly, "
        "produced a consequence the administrators had not considered: enterprising "
        "residents of Delhi discovered that it was far more efficient to breed cobras "
        "in captivity and bring them to the government for the bounty than to hunt "
        "wild cobras, which were becoming scarce. When the colonial administration "
        "eventually discovered the breeding operations and cancelled the bounty, the "
        "breeders, left with worthless snakes, released them. The cobra population "
        "of Delhi ended up higher after the bounty programme than before it. The German "
        "economist Horst Siebert coined the term 'cobra effect' in his 2001 book of "
        "that title to describe this class of perverse incentive outcome.",
        S['body0']))
    story.append(SP(14))

    story.append(callout(
            "<b>The Cobra Effect:</b> When a government or organisation creates an incentive to solve a problem, "
            "rational agents optimise for the incentive rather than the underlying goal, "
            "often making the original problem worse.",
            S))
    story.append(SP(14))

    story.append(P(
        "The same structure appeared in Hanoi in 1902. The French colonial administration "
        "was alarmed by the rat population in the city's newly constructed sewers and "
        "offered a bounty for rat tails. Enterprising Hanoians caught rats, cut off "
        "their tails, and released the rats to breed and produce more tails. The sewers "
        "of Hanoi filled with tailless rats. The bounty was cancelled; the rat population "
        "was, if anything, higher than before. The mechanism of the cobra effect is "
        "always the same: the incentive identifies a proxy (dead cobras, rat tails) "
        "that correlates with the desired outcome (fewer cobras, fewer rats) under "
        "normal conditions, but an agent who treats the proxy as the objective can "
        "decouple it from the underlying goal. The partial-equilibrium analysis "
        "(people will hunt cobras) is correct. The general-equilibrium analysis (people "
        "will find the cheapest way to produce dead cobras, including farming them) "
        "reveals the cascade.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The cobra effect has four structural variants that recur across policy domains. "
        "The first is the direct perverse incentive: the bounty that creates the breeding "
        "programme. The second is displacement: solving the problem in one location "
        "moves it to another. Gun buyback programmes, in which governments offer to "
        "purchase privately owned firearms are frequently cited as an example: "
        "participants tend to sell old, low-value weapons they would not have used "
        "anyway, while keeping functional guns. Studies of Australian and New Zealand "
        "buyback programmes found minimal impact on homicide rates. The third variant "
        "is gaming: meeting the letter of a rule while violating its spirit. The fourth "
        "is crowding out: when a payment is introduced for behaviour that was previously "
        "motivated by intrinsic or social norms, the payment can reduce total provision "
        "of the behaviour. Uri Gneezy and Aldo Rustichini's famous 2000 study of an "
        "Israeli childcare centre found that introducing a fine for late pickup of "
        "children caused late pickups to increase: parents who had previously felt "
        "social pressure to be on time now felt they were simply purchasing additional "
        "childcare time.",
        S['body']))
    story.append(SP(14))

    story.append(fig_cdo_cascade())
    story.append(P(
        "Figure 6.1: The 2008 financial cascade. Each layer of financial innovation "
        "was designed to solve a specific problem with the layer below it: MBS solved "
        "liquidity, CDOs solved risk diversification, synthetic CDOs and CDS solved "
        "hedging. The stacked solutions created interaction complexity that collapsed "
        "simultaneously when the underlying housing assumption failed.",
        S['caption']))

    # ------------------------------------------------------------------
    # Section 2: Jevons Paradox
    # ------------------------------------------------------------------
    story.append(SP(22))
    story.append(P("Jevons Paradox: Efficiency Is Its Own Enemy", S['section']))
    story.append(SP(14))

    story.append(P(
        "In 1865, the twenty-nine-year-old economist William Stanley Jevons published "
        "'The Coal Question: An Inquiry Concerning the Progress of the Nation, and the "
        "Probable Exhaustion of Our Coal Mines'. Jevons had been watching the deployment "
        "of James Watt's improved steam engine, which was dramatically more efficient "
        "than the Newcomen engine it was replacing: it required far less coal per unit "
        "of mechanical output. The common assumption was that this improvement would "
        "reduce Britain's coal consumption and extend the life of its coal reserves. "
        "Jevons observed the opposite. The more efficient the steam engine became, the "
        "more economical coal-powered production became, which expanded the market for "
        "coal-powered machinery, which expanded total coal consumption. The efficiency "
        "gain was real; the reduction in total consumption was a fantasy. Jevons "
        "wrote: 'It is a confusion of ideas to suppose that the economical use of fuel "
        "is equivalent to diminished consumption. The very contrary is the truth.'",
        S['body0']))
    story.append(SP(14))

    story.append(callout(
            "<b>Jevons Paradox:</b> Improvements in the efficiency of resource use tend to increase, rather than "
            "decrease, total consumption of that resource, because efficiency reduces "
            "cost, which expands the scale of the activity using the resource.",
            S))
    story.append(SP(14))

    story.append(P(
        "The Corporate Average Fuel Economy (CAFE) standards, introduced by the US "
        "Congress in 1975 following the Arab oil embargo, required American automakers "
        "to improve the average fuel economy of their passenger car fleets from "
        "approximately 13 miles per gallon to 27.5 mpg by 1985. The standards succeeded "
        "in their direct objective: average new car fuel economy in the US rose from "
        "approximately 13 mpg in 1975 to over 36 mpg by 2023, a 177% improvement. Total "
        "gasoline consumption by American passenger vehicles did not fall: it rose, as "
        "more fuel-efficient cars made driving cheaper per mile, inducing more driving "
        "and the purchase of larger vehicles (SUVs and pickup trucks, which exploit a "
        "regulatory exemption in the CAFE standards). Vehicle miles travelled in the "
        "US increased from approximately 1 trillion in 1975 to approximately 2.7 trillion "
        "by 2019, a 170% increase over the same period in which fuel economy improved "
        "177%. The efficiency gain was almost exactly offset by the demand expansion "
        "it induced.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The LED lighting transition is a contemporary example with global implications. "
        "LED lighting is approximately 10 times more efficient than incandescent bulbs "
        "and 4-5 times more efficient than fluorescent tubes at converting electricity "
        "into visible light. A 2010 paper by Jeff Tsao and colleagues at Sandia National "
        "Laboratories, published in the journal Energy Policy, applied Jevons' analysis "
        "to LED lighting and predicted that the transition to LEDs would not reduce "
        "global electricity consumption for lighting, because cheaper light would induce "
        "more lighting. Their prediction has been confirmed: despite the LED transition, "
        "global light consumption increased by approximately 49% between 1992 and 2017, "
        "as cheap LED lighting enabled outdoor illumination at scales previously "
        "uneconomical: urban streetscapes, advertising signage, architectural lighting, "
        "sports facilities, and as the reduced cost of lighting in developing countries "
        "enabled far higher levels of light consumption than were previously affordable.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "Data compression and bandwidth provide a third example. When DSL internet "
        "connections were introduced in the late 1990s, the average American household "
        "consumed approximately 1-3 gigabytes of internet data per month. The subsequent "
        "twenty years saw continuous improvements in both compression efficiency "
        "(video streaming algorithms became progressively more efficient per unit of "
        "image quality) and network capacity. By 2021, the average American household "
        "consumed approximately 100 gigabytes of data per month, a 30-50 fold increase. "
        "More efficient data transmission made data-intensive applications — streaming "
        "video in higher resolutions, video conferencing, cloud storage, economically "
        "viable, which expanded data consumption. The efficiency gains were fully "
        "absorbed by demand expansion; total internet bandwidth consumption has grown "
        "every year since the internet was invented, regardless of compression advances.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "Carbon leakage is a policy-level Jevons Paradox with global climate implications. "
        "When a jurisdiction introduces a carbon tax or cap-and-trade scheme to reduce "
        "domestic emissions, it raises the cost of carbon-intensive production within "
        "that jurisdiction. Manufacturers respond by moving carbon-intensive operations "
        "to jurisdictions without carbon pricing, reducing measured domestic emissions "
        "while increasing global emissions. The European Union, which introduced the "
        "world's largest carbon trading scheme (the EU ETS) in 2005, estimated that "
        "approximately 20-25% of the emission reductions measured within the EU were "
        "offset by increased emissions elsewhere, the production had simply moved. "
        "The EU's Carbon Border Adjustment Mechanism (CBAM), introduced in 2023, is "
        "an attempt to close this loop by imposing carbon costs on imports equivalent "
        "to those imposed on domestic production. Whether the CBAM will prove effective "
        "or will generate its own cascade of unintended consequences: trade disputes, "
        "retaliatory tariffs, regulatory arbitrage — remains to be seen.",
        S['body']))
    story.append(SP(14))

    story.append(fig_jevons_rebound())
    story.append(P(
        "Figure 6.2: Jevons Paradox in cars and LED lighting. As fuel economy rises "
        "(left panel), vehicle miles travelled rise in parallel. As LED efficiency "
        "increases (right panel), total light consumption rises. Efficiency gains "
        "reduce cost per unit, which expands the scale of the activity.",
        S['caption']))

    # ------------------------------------------------------------------
    # Section 3: Goodhart's Law
    # ------------------------------------------------------------------
    story.append(SP(22))
    story.append(P("Goodhart's Law: The Measurement Problem", S['section']))
    story.append(SP(14))

    story.append(P(
        "In 1975, Charles Goodhart, a monetary economist at the Bank of England, was "
        "analysing the Thatcher government's attempt to control inflation by targeting "
        "monetary aggregates, measures of the money supply such as M1, M2, and M3. "
        "The theoretical basis was sound: in the quantity theory of money, inflation "
        "is driven by money supply growth, so controlling money supply growth should "
        "control inflation. Goodhart observed that once these aggregates became targets "
        "of monetary policy — once the Bank of England began publicly targeting them "
        "and adjusting policy based on them; they ceased to behave as they had "
        "previously, because banks and individuals changed their behaviour in response "
        "to the targeting. Financial instruments that had not previously counted as "
        "money were reclassified; savings patterns shifted; the measured aggregates no "
        "longer tracked the underlying economic phenomenon they had been chosen to "
        "measure. Goodhart stated the principle in its most general form: 'Any "
        "observed statistical regularity will tend to collapse once pressure is placed "
        "upon it for control purposes.'",
        S['body0']))
    story.append(SP(14))

    story.append(callout(
            "<b>Goodhart's Law:</b> When a measure becomes a target, it ceases to be a good measure. "
            "Agents who are rewarded for hitting the metric optimise the metric, "
            "causing it to diverge from the underlying objective it was designed to track.",
            S))
    story.append(SP(14))

    story.append(P(
        "Marilyn Strathern, an anthropologist at Cambridge, restated the principle in "
        "1997 in its most widely quoted form: 'When a measure becomes a target, it "
        "ceases to be a good measure.' Strathern was writing about British academic "
        "research assessment, where universities instructed to produce specific "
        "measurable outputs (publications, patents, citations) had begun optimising "
        "for those outputs rather than for the research quality the outputs were "
        "supposed to measure. The mechanism is universal: any metric that is "
        "sufficiently well-defined to be tracked, and sufficiently consequential to "
        "motivate optimisation, will be gamed by rational agents who face rewards "
        "for hitting it. The more consequential the metric, the more severely it "
        "will be gamed.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The Affordable Care Act's Hospital Readmissions Reduction Program, introduced "
        "in 2012, penalised US hospitals financially if they had higher-than-expected "
        "30-day readmission rates for patients discharged after treatment for heart "
        "failure, pneumonia, and hip/knee replacement. The programme was designed to "
        "improve discharge planning and post-discharge care. The cascade was well-"
        "documented: hospitals in some cases began discharging patients to observation "
        "status rather than inpatient status, which removed them from the readmission "
        "counting denominator; others became more selective in accepting complex "
        "patients who were more likely to be readmitted. A 2019 study in the Journal "
        "of the American Medical Association found that the programme was associated "
        "with increased 30-day post-discharge mortality for heart failure patients — "
        "the readmission rate had fallen because some patients who previously would "
        "have been readmitted and treated were instead dying at home. The metric "
        "improved; the outcome deteriorated.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The Atlanta public school cheating scandal of 2009 illustrates Goodhart's "
        "Law operating under extreme metric pressure. The No Child Left Behind Act "
        "of 2001 required all public school students in the US to reach grade-level "
        "proficiency in reading and maths by 2014, with annual testing to track "
        "progress and consequences including school closure for schools that failed "
        "to meet targets. In Atlanta, 44 teachers and principals, many of them "
        "experienced educators with long careers were indicted and convicted on "
        "racketeering charges for systematically erasing incorrect answers on "
        "standardised tests and filling in correct ones. The Atlanta investigation "
        "found evidence of similar practices in at least 44 other states. The "
        "metric (standardised test scores) had become so consequential that rational "
        "actors chose to falsify it rather than accept the consequences of failing "
        "to hit it.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "Wells Fargo's fake accounts scandal, which became public in September 2016, "
        "demonstrated Goodhart's Law operating at corporate scale. Wells Fargo's "
        "management had established a metric-based compensation and performance "
        "management system that rewarded retail bank employees for cross-selling "
        "additional products to existing customers, the target was an average of "
        "eight products per customer (checking, savings, mortgage, credit card, etc.). "
        "The metric was highly consequential: employees who missed targets faced "
        "termination; employees who hit them received bonuses and promotions. Over "
        "approximately a decade, employees opened approximately 3.5 million fake "
        "accounts — accounts that customers had not requested and were not aware of "
        "— to hit the cross-selling metric. The Consumer Financial Protection Bureau "
        "fined Wells Fargo $185 million in 2016; subsequent settlements and penalties "
        "brought the total to approximately $3 billion. The CEO resigned; 5,300 "
        "employees were fired. The metric had been hit; the objective it represented "
        "— genuine customer relationships had been undermined.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The Soviet nail quota is perhaps the most vivid illustration of Goodhart's Law "
        "at the level of an entire economy. Soviet industrial planning set production "
        "quotas for factories in physical units. When nail factories were given a quota "
        "measured by weight (tonnes of nails), they produced a small number of enormous "
        "nails (construction-grade nails weighing several kilograms each) which met "
        "the weight quota while being useless for most applications. When the quota was "
        "changed to a count (number of nails), they produced vast quantities of tiny "
        "tacks, meeting the count quota while again being useless for construction. "
        "The story, which was documented in Soviet economic journals and satirised in "
        "the official Soviet press, illustrates that Goodhart's Law cannot be defeated "
        "by making the metric more sophisticated: any metric complex enough to be hard "
        "to game is also too complex to be efficiently tracked and managed. GDP itself "
        "— the global standard metric of economic welfare is subject to the same "
        "critique: it counts the production of goods and services regardless of whether "
        "they improve welfare (weapons, cigarettes, medical treatment for preventable "
        "diseases) and excludes unpaid care work, environmental degradation, and "
        "inequality.",
        S['body']))

    # ------------------------------------------------------------------
    # Section 4: 2008 Financial Crisis
    # ------------------------------------------------------------------
    story.append(SP(22))
    story.append(P('The 2008 Financial Crisis: Risk Solutions as Risk Amplifiers', S['section']))
    story.append(SP(14))

    story.append(P(
        "The 2008 global financial crisis was, at its structural core, a cascade problem "
        "of extraordinary complexity and velocity. The financial instruments at the heart "
        "of the crisis: mortgage-backed securities (MBS), collateralised debt obligations "
        "(CDOs), CDO-squared (CDOs backed by tranches of other CDOs), synthetic CDOs "
        "(CDOs backed by credit default swaps rather than actual mortgages), and credit "
        "default swaps (CDS, financial insurance against CDO defaults) were not simple "
        "frauds. Each was a genuine financial innovation designed by sophisticated "
        "mathematicians and economists to solve a real problem. MBS solved the liquidity "
        "problem of mortgage lending: banks that issued mortgages could now sell them to "
        "investors rather than holding them, freeing capital for more lending. CDOs solved "
        "the risk distribution problem: by bundling mortgages and slicing the bundle into "
        "tranches with different risk profiles, they allowed risk to be allocated to "
        "investors with different risk appetites. CDS solved the hedging problem: they "
        "allowed institutions holding CDOs to insure against the risk of default. Each "
        "solution was layered on top of the previous one, and each introduced interaction "
        "complexity that its designers did not fully understand.",
        S['body0']))
    story.append(SP(14))

    story.append(P(
        "The critical failure in the CDO structure was the independence assumption. CDO "
        "pricing models, developed by David Li in a 2000 paper using a Gaussian copula "
        "function, calculated the default correlation between mortgages, the probability "
        "that two mortgages would default simultaneously — based on historical data "
        "from a period of generally rising home prices. In that historical period, "
        "mortgage defaults were relatively independent: a job loss in Ohio did not "
        "predict a job loss in California. The copula model assigned low correlations; "
        "CDOs rated AAA by the credit rating agencies were priced on the assumption "
        "that defaults would remain largely uncorrelated. This assumption held during "
        "normal conditions. In a nationwide housing bubble, it failed: when home prices "
        "fell simultaneously across all major US markets beginning in 2006-07, mortgage "
        "defaults became highly correlated across geographies. The diversification "
        "that was supposed to make CDOs safe had been an artefact of favourable "
        "historical conditions rather than a structural feature.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The credit rating agencies compounded the failure. Moody's, Standard & Poor's, "
        "and Fitch assigned AAA ratings, the highest possible, indicating essentially "
        "zero default risk, to CDO tranches that subsequently lost all or most of their "
        "value. The conflict of interest was structural: rating agencies were paid by "
        "the issuers of the securities they rated, creating incentives to provide "
        "favourable ratings to attract business. The Financial Crisis Inquiry Commission, "
        "established by Congress to investigate the crisis, found that credit rating "
        "agencies had built financial models that they knew underestimated the risk of "
        "mortgage-backed securities, and that employees who raised concerns were "
        "overridden by management. Between 2000 and 2007, Moody's rated approximately "
        "$4.7 trillion of mortgage-related securities; a large fraction of those ratings "
        "were subsequently revised to junk. Institutions that were required by regulation "
        "to hold only AAA-rated assets: pension funds, insurance companies, money market "
        "funds had inadvertently accumulated catastrophic risk.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "AIG's CDS exposure was the mechanism through which a housing market correction "
        "became a global financial collapse. AIG Financial Products, a London-based "
        "subsidiary of the American insurance giant, had sold CDS contracts, in effect, "
        "insurance policies, guaranteeing trillions of dollars of CDOs against default. "
        "Because CDS contracts were not classified as insurance under the regulations "
        "of the time, AIG was not required to hold reserves against the policies it had "
        "written. When CDOs began defaulting in 2007-08, AIG faced obligations it had "
        "no capacity to honour. On September 16, 2008, the day after Lehman Brothers "
        "filed for bankruptcy, the US government announced an $85 billion emergency "
        "bailout of AIG, subsequently increased to $182 billion. AIG was too interconnected "
        "to fail: its collapse would have triggered the simultaneous failure of every "
        "major bank in the United States and Europe that had bought CDS protection "
        "from it. The instrument designed to distribute and hedge risk had concentrated "
        "it in a single institution.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The ultimate economic cost of the crisis was staggering. US GDP contracted by "
        "2.5% in 2009, the deepest recession since the Great Depression. An estimated "
        "$22 trillion in household wealth was destroyed in the United States between "
        "2007 and 2009, the equivalent of wiping out the entire economic output of the "
        "country for one and a half years. Approximately 10 million American homeowners "
        "lost their homes to foreclosure or were forced to sell at a loss. The "
        "unemployment rate peaked at 10% in October 2009. The Troubled Asset Relief "
        "Programme (TARP), which spent approximately $700 billion purchasing toxic "
        "assets from banks, generated its own cascade: the perception that large banks "
        "would always be bailed out by the government created a moral hazard that "
        "encouraged future risk-taking. Goldman Sachs paid $16.2 billion in bonuses in "
        "2010 (the year after receiving $10 billion in TARP funds) triggering the "
        "Occupy Wall Street movement and contributing to a decade of political anger "
        "at financial institutions that has not fully dissipated.",
        S['body']))
    story.append(SP(14))

    story.append(fig_fed_balance_sheet())
    story.append(P(
        "Figure 6.3: The Federal Reserve balance sheet from 2000 to 2023. QE expanded "
        "the balance sheet from $900 billion to $9 trillion in four rounds. The asset "
        "price inflation this produced: S&P 500 from 666 (March 2009) to 4,796 "
        "(January 2022) was the primary driver of the wealth inequality that became "
        "the dominant political issue of the following decade.",
        S['caption']))

    # ------------------------------------------------------------------
    # Section 5: Quantitative Easing
    # ------------------------------------------------------------------
    story.append(SP(22))
    story.append(P('Quantitative Easing and the Inequality Cascade', S['section']))
    story.append(SP(14))

    story.append(P(
        "Ben Bernanke, appointed chairman of the Federal Reserve by President George W. "
        "Bush in 2006, had spent much of his academic career studying the Great Depression. "
        "His 2000 book 'Essays on the Great Depression' argued that the Federal Reserve's "
        "failure to prevent bank failures and deflation in 1929-33 had transformed a "
        "severe but manageable recession into a decade-long catastrophe. When the 2008 "
        "financial crisis struck, Bernanke was determined to apply the lessons he had "
        "spent twenty years studying. The Federal Reserve cut interest rates to "
        "effectively zero by December 2008. When conventional monetary policy had been "
        "exhausted and the financial system was still contracting, the Fed implemented "
        "quantitative easing: the large-scale purchase of financial assets, initially "
        "mortgage-backed securities and Treasury bonds: using newly created money, "
        "injecting liquidity directly into the financial system.",
        S['body0']))
    story.append(SP(14))

    story.append(P(
        "QE1, announced in November 2008, involved $600 billion of MBS purchases. "
        "QE2 (November 2010) added $600 billion of Treasury purchases. QE3 (September "
        "2012) was open-ended — $85 billion per month until economic conditions "
        "improved, ultimately totalling approximately $1.7 trillion. QE4, implemented "
        "in response to the Covid-19 pandemic beginning in March 2020, was the largest: "
        "the Federal Reserve purchased approximately $3.3 trillion of assets in 2020 "
        "alone, expanding its balance sheet from approximately $4 trillion to over "
        "$7 trillion in twelve months. By early 2022, the Fed's balance sheet had "
        "reached $9 trillion, more than thirteen times its pre-crisis level of $900 "
        "billion in 2006. The European Central Bank, Bank of England, and Bank of Japan "
        "conducted parallel QE programmes on comparable scales.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "QE worked in its primary objective: the deflationary spiral that had "
        "devastated the 1930s economy was averted. Credit began flowing; banks "
        "stabilised; the economy grew. The S&P 500 stock index, which had fallen "
        "to 666 on March 9, 2009 (its lowest point in twelve years) rose to 4,796 "
        "by January 3, 2022, a 620% increase over twelve years. US corporate profits "
        "reached record levels. Unemployment fell to historic lows by 2019. By "
        "conventional macroeconomic measures, QE was a success.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The cascade arrived through the distribution of the gains. The asset price "
        "inflation produced by QE accrued overwhelmingly to those who already owned "
        "assets (equities, real estate, bonds) which in the United States are "
        "concentrated in the wealthiest households. The top 1% of American households "
        "own approximately 53% of equities; the top 10% own approximately 89%. Wage "
        "growth for the bottom half of the income distribution remained subdued "
        "throughout the QE period. Housing prices in major metropolitan areas, driven "
        "by the same low-interest-rate environment QE produced, increased faster than "
        "wages for several years, pricing a generation out of homeownership. The Gini "
        "coefficient of US wealth inequality, the standard measure, where 0 represents "
        "perfect equality and 1 represents one person owning everything, rose from "
        "approximately 0.80 in 2007 to approximately 0.87 by 2020, approaching the "
        "highest levels recorded since before the Great Depression.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The unwinding of QE generated its own cascade. When the Federal Reserve "
        "began raising interest rates in March 2022 to combat the inflation that had "
        "been building since 2021 — itself partly a consequence of the monetary "
        "expansion, the decade-long regime of near-zero interest rates ended abruptly. "
        "Silicon Valley Bank, which had accumulated a portfolio of long-dated Treasury "
        "bonds during the zero-rate environment, found those bonds sharply devalued "
        "when rates rose. A bank run triggered by social media amplification of the "
        "bank's losses caused SVB to fail on March 10, 2023, the second-largest "
        "bank failure in US history, requiring the Federal Deposit Insurance Corporation "
        "to guarantee all deposits including those above the $250,000 insurance limit. "
        "Signature Bank failed two days later. Credit Suisse, one of Europe's largest "
        "banks, was forced into an emergency merger with UBS in March 2023 as confidence "
        "in its stability collapsed. The solution to the 2008 financial crisis had "
        "created a decade of asset price inflation, wealth inequality, and financial "
        "fragility that manifested in the next round of bank failures. The cascade "
        "was not finished.",
        S['body']))
    story.append(SP(14))

    story.append(P(
        "The political consequences of the QE-induced inequality cascade are still "
        "unfolding. The perception that the financial system was structured to bail out "
        "the wealthy while ordinary households faced foreclosure, stagnant wages, and "
        "unaffordable housing drove significant political realignment across the "
        "developed world in the decade following 2008. Populist movements of both "
        "left and right: Occupy Wall Street, the Tea Party, Brexit, the Sanders "
        "campaign, Trumpism, Jeremy Corbyn's Labour leadership, the gilets jaunes "
        "in France — drew on a common grievance: that the rules of the economic system "
        "were arranged to benefit those at the top at the expense of those below. "
        "Whether this perception accurately describes the underlying causal chain is "
        "a matter of legitimate debate; what is harder to argue with is that the "
        "perception itself, regardless of its precise accuracy, has become a "
        "first-order political force in its own right — a cascade not from the "
        "original financial solution but from the way its costs and benefits were "
        "distributed in the decade that followed.",
        S['body']))

    story.append(SP(18))
    story.append(P('The Economics of Cascade: Why Markets Cannot Self-Correct', S['section']))
    story.append(P('A persistent argument against the cascade thesis in economic domains is the self-correction argument: markets, it is said, will identify and price cascade effects as they emerge, creating incentives for agents to avoid cascade-generating solutions and adopt cascade-aware ones. The argument has theoretical merit but empirical fragility. It depends on conditions: complete information, internalised externalities, long-time-horizon agents, that are systematically absent in the economic environments where the most severe financial and policy cascades have originated.', S['body0']))
    story.append(P('The information condition fails first. Market participants can only price cascade risks they know about. The CDO cascade, the opioid cascade, and the agricultural subsidy cascade were all invisible to market pricing mechanisms until after the cascade had become catastrophic, not because market participants were irrational, but because the cascade risks were genuinely outside the information sets of the agents making decisions. A CDO trader who correctly assessed the correlation risk in the 2006-vintage CDO pools and refused to buy them lost money in the short run (as CDO prices continued to rise) and was correct in the long run (when the cascade arrived). The market was pricing the cascade wrong not because of irrationality but because of rational behaviour under information constraints. The argument from market self-correction fails precisely when the cascade is most severe: when the cascade is systemic and the information about systemic risk is not available to any individual market participant.', S['body']))
    story.append(P('The externality condition fails next. The cascade from the cobra bounty (the release of farmed cobras into the street) was an externality: the cobra farmers bore none of the cost of the increased snake population they created. The cascade from antibiotic overuse (the selection pressure for resistant bacteria) is an externality: individual prescribing physicians and patients bear none of the cost of the increased resistance that their prescriptions generate, which is borne diffusely by future patients globally. The cascade from carbon emissions (the contribution to global warming) is the largest externality in human history. In each case, the market cannot self-correct the cascade because the cascade costs are borne by parties who have no contractual relationship with the cascade generators and no legal mechanism for claiming compensation. Market self-correction requires that cascade costs be internalised, which requires either regulatory intervention (carbon taxes, antibiotic stewardship programs, prescription monitoring systems) or private contracting (liability regimes that hold cascade generators responsible for cascade costs). Neither mechanism has been implemented at the scale and speed required by the cascade dynamics in any of the domains examined in this book.', S['body']))
    story.append(P('The time horizon condition fails last, and most decisively. Markets discount the future: a cost in ten years is worth less, in present market terms, than the same cost today. The cascade\'s characteristic structure: immediate, concentrated benefits followed by delayed, diffuse costs is specifically calibrated to exploit this discounting. The benefit of an opioid prescription is received immediately: the patient experiences pain relief today. The cascade cost, the patient\'s potential addiction, the diversion of prescription pills into street markets, the selection pressure for illicit fentanyl supply — arrives over years or decades and is distributed across thousands of people none of whom were party to the original prescription. No market mechanism can internalise costs that arrive decades later, fall on diffuse populations, and are mediated by multiple causal chains. The cascade is, at its economic core, an inter-temporal and inter-personal externality that no purely market-based mechanism can manage.', S['body']))
    story.append(callout('<b>The Market Self-Correction Fallacy:</b> Markets can self-correct cascade effects only when (1) cascade risks are known in advance, (2) cascade costs are borne by cascade generators, and (3) cascade costs arrive within the time horizon of market pricing. In practice, severe cascades violate all three conditions simultaneously. The conditions under which markets fail to self-correct are the same conditions that produce the most severe cascades.', S))

    story.append(SP(18))
    story.append(P('Agricultural Subsidies: The Accidental Food System', S['section']))
    story.append(P('Agricultural subsidies, introduced in the United States as an emergency response to the Depression-era farm crisis of the 1930s and extended subsequently in most developed-world countries, represent one of the most consequential and least examined cascade stories in the economics of the twentieth century. The original problem was genuine and acute: farm commodity prices had collapsed to levels below the cost of production, threatening the food security of the nation and the economic survival of millions of farm families. The solution: price supports, acreage controls, and income supplements designed to stabilise farm incomes above the cost of production — achieved its immediate objectives. The cascade it generated has reshaped global agriculture, food systems, and public health in ways that are still accelerating.', S['body0']))
    story.append(P('The first-generation cascade of the US farm subsidy system is overproduction. When the government guarantees a minimum price above the cost of production, it is rational for farmers to produce as much as possible, regardless of market demand, because every unit of production is guaranteed to recover its cost. The accumulation of surplus commodities, the "butter mountains" and "grain mountains" of Western agricultural policy — began within a decade of the policies\' introduction and continues to the present. By 2023, the US government was spending approximately $20 billion annually in direct farm subsidies, predominantly for corn, soybeans, wheat, cotton, and rice — commodities in chronic oversupply. The subsidy system simultaneously discourages crop diversification (subsidised crops are always safer to grow than unsubsidised ones), rewards the largest farms disproportionately (the top 10% of farm subsidy recipients receive approximately 70% of total subsidy payments), and depresses world market prices for the subsidised commodities to levels that are below the cost of production for unsubsidised farmers in developing countries, generating a second-generation cascade in global agricultural development.', S['body']))
    story.append(P('The second-generation cascade of developed-world agricultural subsidies is the destruction of subsistence farming in the developing world. When US corn is dumped on world markets at prices below its cost of production (made possible by the $20 billion subsidy), Mexican farmers who grow corn without subsidies cannot compete. This effect was documented systematically following NAFTA\'s implementation in 1994: an estimated 2 million Mexican small farmers were pushed out of corn farming between 1994 and 2008 by competition from subsidised US corn. The displaced farmers did not disappear; they migrated, to Mexican cities, where they created or expanded slum populations, and to the United States, where they became undocumented immigrants. The political cascade of undocumented immigration from Mexico to the United States, a significant driver of US domestic political conflict from the 1990s to the present has multiple causes, but subsidised agricultural competition is among the documented ones. The solution to the 1930s US farm crisis generated, seventy years later, a migration and political cascade that the architects of the New Deal could not have anticipated.', S['body']))
    story.append(P('The third-generation cascade of agricultural subsidies is the food system health cascade. The commodities most heavily subsidised (corn, soybeans, wheat) are also the inputs for the ultra-processed food products that nutritional epidemiology has linked to the obesity epidemic, type 2 diabetes, and cardiovascular disease that are the leading causes of morbidity and mortality in the developed world. High-fructose corn syrup (from subsidised corn) and partially hydrogenated soybean oil (from subsidised soybeans) became the dominant caloric inputs to the American diet between 1970 and 2000, correlating with a obesity prevalence increase from 13% to 30%. The direct causal link between specific subsidised commodities and specific diet-related health outcomes is contested in nutritional science, as it should be, given the complexity of dietary causation. But the structural relationship is not contested: agricultural subsidies make the ingredients of ultra-processed food systematically cheaper than the ingredients of whole food, creating a persistent economic gradient that disadvantages healthy food relative to processed food for price-sensitive consumers. The health consequences of this gradient are borne by the consumers, not by the agricultural subsidy system that created it. The externality structure is identical to the other economic cascades examined in this chapter.', S['body']))

    story.append(SP(22))
    story.append(P('Cryptocurrency: The Decentralisation Cascade', S['section']))
    story.append(SP(14))
    story.append(P(
        "Satoshi Nakamoto's 2008 whitepaper, 'Bitcoin: A Peer-to-Peer Electronic Cash "
        "System,' introduced a technical solution to a genuine problem: the dependence "
        "of digital financial transactions on trusted third parties (banks, payment "
        "processors) that charged fees, imposed restrictions, and were vulnerable to "
        "government seizure, censorship, and failure. Bitcoin's blockchain technology "
        "solved this problem through a cryptographic mechanism that established "
        "consensus about transaction history without requiring any trusted central "
        "authority, a genuine cryptographic breakthrough. The cascade from this "
        "solution has been extraordinary in both its scale and its diversity.",
        S['body0']))
    story.append(SP(14))
    story.append(P(
        "The energy cascade is the most immediate and measurable. Bitcoin's Proof-of-Work "
        "consensus mechanism, the algorithm by which the blockchain achieves consensus "
        "without a central authority — requires participants to perform computationally "
        "intensive calculations (the 'mining' process) to validate transactions. The "
        "difficulty of these calculations is calibrated to ensure that new Bitcoin is "
        "added to the supply at a controlled rate. As the value of Bitcoin increased and "
        "more miners competed for the reward, the total computational power devoted to "
        "mining (the 'hashrate') increased from approximately 10 million hashes per second "
        "in 2009 to approximately 600 quintillion hashes per second in 2024. The energy "
        "required to sustain this computation is estimated at approximately 130 terawatt-hours "
        "per year — comparable to the annual electricity consumption of Argentina. A "
        "single Bitcoin transaction has a carbon footprint equivalent to approximately "
        "1.7 million Visa transactions, according to calculations by Digiconomist. The "
        "technology designed to create a trustless, decentralised financial system "
        "generates a carbon footprint for each transaction that exceeds by orders of "
        "magnitude the carbon footprint of the centralised financial system it was "
        "designed to replace.",
        S['body']))
    story.append(SP(14))
    story.append(P(
        "The crime cascade emerged from Bitcoin's pseudonymity, the property that "
        "transactions are linked to cryptographic addresses rather than identities. "
        "This property, which was essential to Bitcoin's value proposition as a "
        "censorship-resistant payment system, also made it the preferred payment "
        "mechanism for ransomware attackers, darknet drug markets, money launderers, "
        "and sanctions evaders. The Colonial Pipeline ransomware payment of $4.4 million "
        "(partially recovered by the FBI); the $2.4 billion Bitfinex hack (where "
        "stolen Bitcoin sat for years before the perpetrators attempted to launder it); "
        "the $625 million Ronin Network hack; and the estimated $20 billion in "
        "cryptocurrency transactions annually through services specifically designed "
        "to obscure transaction traceability, all are cascades from the pseudonymity "
        "feature that made Bitcoin's decentralisation possible. The solution to the "
        "trusted third party problem created the problem of trustless criminal finance.",
        S['body']))
    story.append(SP(14))
    story.append(P(
        "The investor protection cascade is the most socially diffuse consequence. "
        "The speculative investment demand for cryptocurrencies, driven by media "
        "coverage of extraordinary returns in 2017 and 2020-2021 — drew millions "
        "of retail investors into a market with no regulatory protections, no "
        "investor compensation schemes, and mechanisms specifically designed to "
        "facilitate fraud. The Bitconnect Ponzi scheme extracted approximately "
        "$2.4 billion from retail investors before collapsing in 2018. The FTX "
        "exchange, which at its peak processed $10 billion in daily transactions "
        "and whose founder Sam Bankman-Fried was celebrated on magazine covers as "
        "a visionary, collapsed in November 2022 after the discovery that customer "
        "funds had been used to cover losses at an affiliated trading firm — "
        "a straightforward act of fraud that caused approximately $8 billion in "
        "customer losses. A 2022 survey by the Federal Reserve found that "
        "approximately 13% of US adults had used or invested in cryptocurrency "
        "in the previous year; a subsequent survey found that approximately "
        "20% of those had experienced fraud or theft. The decentralised finance "
        "system's freedom from trusted third parties is also freedom from the "
        "regulatory protections that trusted third parties provide.",
        S['body']))
    story.append(SP(14))
    story.append(P(
        "The monetary policy cascade is the most economically sophisticated. "
        "Bitcoin's fixed supply cap (21 million coins) was designed as a solution "
        "to the inflation generated by central bank money creation. The cascade "
        "is that fixed supply makes Bitcoin pro-cyclically deflationary: as "
        "economic output grows and the demand for the medium of exchange grows, "
        "the fixed supply causes its value to increase, rewarding holding over "
        "spending and creating the hoarding dynamic that conventional economics "
        "identifies as the central failure of commodity money standards. The "
        "gold standard's abandonment in the twentieth century was driven by this "
        "same property: a fixed monetary base cannot accommodate the growth "
        "needs of a modern economy without deflationary spirals. Bitcoin's "
        "solution to inflation has recreated, in digital form, the monetary "
        "system that the twentieth century abandoned for empirically observed "
        "reasons. The cascade from the solution to inflation is deflation — "
        "a problem that economic history has repeatedly shown to be more "
        "destructive than moderate inflation.",
        S['body']))
    story.append(SP(14))

    story.append(SP(22))
    story.append(P('Trade Liberalisation: The Displacement Cascade', S['section']))
    story.append(SP(14))
    story.append(P(
        "The economic case for free trade, grounded in David Ricardo's principle "
        "of comparative advantage (1817), is one of the strongest theoretical "
        "results in all of economics: when countries specialise in goods they "
        "produce most efficiently and trade with each other, total global production "
        "exceeds what would be produced under autarky, and every participating "
        "country can consume more than it could produce alone. The empirical "
        "evidence for the global gains from trade liberalisation is substantial. "
        "The World Trade Organisation estimates that merchandise trade growth "
        "since 1948 has expanded global real income by several times what it "
        "would have been without liberalisation. China's accession to the WTO "
        "in 2001 contributed to the largest rapid poverty reduction in human "
        "history: approximately 800 million Chinese citizens escaped extreme "
        "poverty between 1990 and 2015, a development that would not have been "
        "possible without access to Western markets. The aggregate benefit of "
        "trade liberalisation is not in serious dispute.",
        S['body0']))
    story.append(SP(14))
    story.append(P(
        "The cascade is in the distribution. Ricardo's comparative advantage "
        "theorem proves that the gains from trade exceed the losses but it "
        "does not guarantee that the gains and losses fall on the same people. "
        "The economic research of David Autor, David Dorn, and Gordon Hanson "
        "on the 'China shock', the impact of Chinese import competition on "
        "US manufacturing workers following China's WTO accession — documents "
        "the distributional cascade with quantitative precision. Counties with "
        "high exposure to Chinese import competition experienced sharp, persistent "
        "declines in manufacturing employment; the jobs that were lost were "
        "concentrated among workers without college education; these workers "
        "did not, contrary to standard economic prediction, transition to "
        "comparable employment in other sectors. Autor et al. estimated that "
        "Chinese import competition eliminated approximately 2.4 million US "
        "manufacturing jobs between 1999 and 2011, a localised, concentrated "
        "loss that fell on specific communities whose entire economic identity "
        "had been built around the industries that were displaced.",
        S['body']))
    story.append(SP(14))
    story.append(P(
        "The political cascade from the distributional shock is the most "
        "consequential consequence of trade liberalisation's distributional "
        "failure. Autor, Dorn, and Hanson's 2020 paper 'Importing Political "
        "Polarisation' demonstrated that counties with the highest exposure to "
        "Chinese import competition experienced the largest swings toward "
        "political extremism, both toward far-right candidates (Trump in 2016) "
        "and, to a lesser extent, far-left candidates (Sanders in the Democratic "
        "primary). The communities whose manufacturing base was eliminated by "
        "trade liberalisation responded politically by supporting candidates who "
        "explicitly promised to reverse it. The economic cascade from comparative "
        "advantage theory became a political cascade that threatened the "
        "institutional framework of the liberal international order within "
        "which trade liberalisation operates. The solution to the problem of "
        "inefficient production allocation generated a political crisis for "
        "the institutions that maintain the conditions under which the solution "
        "operates.",
        S['body']))
    story.append(SP(14))
    story.append(P(
        "The infrastructure cascade from trade liberalisation is less visible "
        "but economically significant. When manufacturing moves offshore, it "
        "takes with it the supply chain infrastructure, the engineering knowledge, "
        "the skilled trades education, and the institutional knowledge about "
        "how to make things that accumulated over generations of industrial "
        "production. This knowledge is not simply transferable back. When the "
        "COVID-19 pandemic disrupted global supply chains in 2020-2021, the "
        "United States discovered that its domestic manufacturing capability "
        "in critical sectors: personal protective equipment, semiconductor chips, "
        "pharmaceuticals, rare earth metals was insufficient to meet demand "
        "even at crisis levels. The CHIPS Act (2022) and the Inflation Reduction "
        "Act (2022) represented the US government's most significant attempt "
        "in decades to reverse the supply chain vulnerability cascade, at a "
        "combined cost of over $750 billion in subsidies and tax incentives. "
        "The reshoring of manufacturing capacity that had been offshored over "
        "thirty years of trade liberalisation will, itself, generate cascades: "
        "in the countries whose export industries will contract, in the trade "
        "agreements that will be strained by subsidy competition, and in the "
        "industries that will now face import competition from resurgent domestic "
        "producers in their export markets.",
        S['body']))
    story.append(SP(14))

    # ── Chapter 6 Synthesis ────────────────────────────────────────────────
    story.append(SP(18))
    story.append(P('The Universal Market and Its Discontents', S['section']))
    story.append(P(
        'The common thread running through the economic cascades documented in '
        'this chapter is the systematisation of a single, powerful idea: that '
        'markets aggregate information and allocate resources more efficiently '
        'than any central planner. This idea is not wrong. The evidence that '
        'market economies outperform centrally planned economies in most measures '
        'of material welfare is overwhelming. But the evidence also shows, with '
        'equal clarity, that the application of this idea, the construction of '
        'markets where markets did not previously exist, the extension of market '
        'logic into domains previously governed by other principles, and the '
        'removal of constraints on market behaviour, generates cascades that '
        'are not self-correcting within any politically tolerable time frame.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The Cobra Effect, the archetypal example with which this chapter began '
        '— illustrates the fundamental mechanism: when a market incentive is '
        'introduced into a system where actors can manipulate the measured '
        'variable, the incentive generates behaviour that defeats its own purpose. '
        'This mechanism recurs throughout economic history because it is a '
        'consequence of the structure of any incentive system. Goodhart\'s '
        'Law, when a measure becomes a target, it ceases to be a good measure '
        '— is a precise statement of the Cobra Effect in general form. Every '
        'economic incentive system is subject to Goodhart\'s Law because every '
        'incentive system involves actors who have information that the incentive '
        'designer does not, and who have motives to optimise for the measured '
        'variable rather than the underlying goal.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The financial cascade of 2008 illustrates the same mechanism operating '
        'at civilisational scale. The incentive to originate loans and sell them '
        'as securities solved the problem of geographic capital mismatch. The '
        'cascade was the elimination of the originator\'s incentive to assess '
        'borrower creditworthiness, the entire point of mortgage underwriting. '
        'The measure (loan volume, security issuance) became the target; the '
        'underlying goal (efficient allocation of capital to creditworthy borrowers) '
        'was abandoned. The result was a $22 trillion destruction of household '
        'wealth, a global recession, and fifteen years of monetary policy '
        'experimentation whose own cascades: asset price inflation, wealth '
        'concentration, zero-interest-rate dependency are still being managed '
        'by central banks around the world.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The quantitative easing cascade deserves further examination as an '
        'example of how economic solutions generate cascades that constrain '
        'future solutions. The Federal Reserve began QE in 2008 by purchasing '
        'government bonds and mortgage-backed securities to inject liquidity '
        'into a frozen financial system. The policy worked: the US avoided a '
        'depression. The cascades from QE include: (1) the asset price inflation '
        'cascade — low interest rates increased the present value of financial '
        'assets, generating the largest stock market and real estate boom in '
        'recorded history, disproportionately benefiting asset owners; '
        '(2) the zombie company cascade — low rates enabled companies that '
        'could not service debt at normal rates to survive indefinitely, '
        'reducing economic dynamism; (3) the interest rate trap — having '
        'driven rates to near-zero and expanded its balance sheet to over '
        '$9 trillion, the Fed found that normalising monetary policy in '
        '2022-2023 required rapid rate increases that collapsed bond portfolios '
        '(contributing to the Silicon Valley Bank failure in March 2023), '
        'sharply increased the interest cost of the US national debt, and '
        'triggered a global repricing of risk assets. The solution to the '
        '2008 crisis created a monetary policy regime from which it was '
        'difficult to exit without generating new crises.',
        S['body']))
    story.append(SP(14))
    story.append(callout(
        '<b>The Policy Lock-in Problem:</b> Economic solutions often create '
        'dependencies that constrain future policy choices. Quantitative easing '
        'solved the 2008 liquidity crisis but created a low-interest-rate regime '
        'on which financial markets, government budgets, and companies became '
        'dependent, making the exit from the solution as dangerous as '
        'the original problem it solved.',
        S))
    story.append(SP(14))

    story.append(SP(18))
    story.append(P('The Automation Cascade: From Power Looms to Artificial Intelligence', S['section']))
    story.append(P(
        'The history of automation is a cascade running for two and a half '
        'centuries, which has in every phase generated fears of technological '
        'unemployment that proved premature, while simultaneously generating '
        'social disruptions that proved real. The Luddites of 1811-1816, who '
        'destroyed textile machinery in the English Midlands, were not wrong '
        'that power looms would destroy their specific livelihoods. They were '
        'wrong that the destruction would produce permanent mass unemployment. '
        'The jobs destroyed by power looms were replaced by jobs maintaining '
        'them, building the factories that housed them, operating the railways '
        'that transported their output, and staffing the retail establishments '
        'that sold the cheap cloth. This pattern — automation destroys jobs in '
        'one sector while creating them elsewhere — repeated across every wave '
        'of automation in industrial history.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The current wave of automation — artificial intelligence displacing '
        'cognitive as well as manual labour is generating cascades that '
        'combine all features of previous waves with several new ones. The '
        'speed of AI capability growth is faster: GPT-4 (2023) demonstrated '
        'performance at or above human level on a large fraction of professional '
        'licensing examinations within three years of GPT-3 (2020). The breadth '
        'of affected occupations is greater: previous automation displaced '
        'manual and routine cognitive workers; AI systems are currently capable '
        'in law, medicine, accounting, programming, writing, and graphic design '
        '— tasks considered high-skill and automation-proof. The concentration '
        'of AI capability in a small number of very large technology companies '
        'creates a winner-take-all dynamic with no historical precedent: the '
        'marginal cost of AI labour approaches zero, but the fixed cost of '
        'developing frontier systems runs to billions of dollars.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The cascade from AI automation most directly paralleling historical '
        'patterns is the skills mismatch problem. Every previous automation '
        'wave created demand for new skills while destroying demand for old '
        'ones. The transition required retraining workers and rebuilding '
        'educational systems, processes that take twenty to thirty years '
        'under optimal conditions. The AI wave creates demand for mathematical '
        'reasoning, complex communication, interpersonal judgment, and physical '
        'dexterity in unstructured environments, while destroying demand for '
        'routine cognitive skills that happen to be what most existing '
        'educational and training institutions teach. The educational system '
        'needed to manage the AI automation cascade does not yet exist. '
        'Building it is the cascade-management problem that will define the '
        'first half of the twenty-first century.',
        S['body']))
    story.append(SP(14))

    story.append(SP(18))
    story.append(P('The Financialisation Cascade: When Finance Dominates the Economy', S['section']))
    story.append(P(
        'Financialisation, the increasing role of financial markets, institutions, '
        'and motives in the operation of the economy is a cascade from the '
        'solution to several distinct economic problems. Equity markets solved '
        'the problem of funding large enterprises. Bond markets solved the '
        'problem of borrowing at scale across time. Derivative markets solved '
        'the problem of hedging commodity price risk. Futures markets allowed '
        'producers and consumers to lock in prices in advance. Each solution '
        'worked. The cumulative effect was a financial sector that, by 2006, '
        'accounted for 40% of US corporate profits while employing 5% of the '
        'workforce and producing no physical goods or services.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The financialisation cascade operates through short-termism: corporate '
        'managers, whose compensation is tied to stock price, optimise for '
        'quarterly earnings at the expense of long-term investment. US corporate '
        'investment as a share of GDP declined from approximately 12% in the '
        '1970s to approximately 8% by the 2010s, while share buybacks increased '
        'from negligible to over $800 billion annually. Companies were returning '
        'capital to shareholders rather than investing in productive capacity '
        '— a rational response to financial incentives that is a cascade from '
        'the solution to the problem of aligning manager and shareholder '
        'interests through stock-based compensation.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The deepest cascade from financialisation is the measurement problem. '
        'When financial returns become the dominant measure of economic success, '
        'and when financial returns are measurable with great precision while '
        'other forms of value: ecosystem services, community cohesion, knowledge '
        'production, cultural vitality are not measurable in financial terms, '
        'economic decision-making systematically overvalues the financial and '
        'undervalues the non-financial. This is Goodhart\'s Law at civilisational '
        'scale. The cascade is visible in the systematic underinvestment in '
        'public goods, the degradation of non-market institutions, and the '
        'emergence of a form of decision-making in which a forest\'s value is '
        'zero until it is cut down, at which point it briefly becomes positive '
        'before disappearing into accounting history.',
        S['body']))
    story.append(SP(14))
    story += epigraph(
        'Not everything that can be counted counts, and not everything that counts can be counted.',
        'Attributed to Albert Einstein',
        S)
    story.append(SP(14))

    # ------------------------------------------------------------------ #
    # EXTENDED: The Regulatory Cascade                                     #
    # ------------------------------------------------------------------ #
    story.append(SP(18))
    story.append(P('The Regulatory Cascade: When Rules Create New Loopholes', S['section']))
    story.append(P(
        'Every significant regulation creates a new surface for regulatory '
        'arbitrage. The pattern is so reliable that financial historians have '
        'given it a name: regulatory dialectic, the cyclical process by which '
        'regulation and innovation chase each other through time, with neither '
        'achieving permanent advantage. The cycle operates as follows: a market '
        'failure or harm becomes visible; regulators design rules to address it; '
        'market participants develop innovations that comply with the letter of '
        'the rules while circumventing their spirit; new harms emerge from the '
        'innovations; new regulations are designed; and the cycle continues. '
        'Each iteration produces a more complex regulatory apparatus and a more '
        'complex market structure, with no net reduction in systemic risk.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The Glass-Steagall Act of 1933 provides the archetypal example. '
        'Enacted in response to the bank failures of the Great Depression, '
        'failures attributed in part to commercial banks using depositor funds '
        'to speculate in securities markets, the Act separated commercial '
        'banking from investment banking. The separation worked for four '
        'decades. The cascade came in the 1970s and 1980s as financial '
        'innovation created instruments that did not neatly fit the '
        'commercial/investment distinction: money market funds, which functioned '
        'like bank deposits but were technically securities; commercial paper '
        'markets, which allowed corporations to borrow short-term without bank '
        'intermediation; mortgage-backed securities, which blended '
        'commercial lending with securities issuance. By the time Glass-Steagall '
        'was formally repealed by the Gramm-Leach-Bliley Act in 1999, it had '
        'been substantially circumvented by innovation for two decades. The '
        'repeal was, in this sense, the regulatory system formally acknowledging '
        'a cascade that had already occurred.',
        S['body']))
    story.append(SP(14))
    story.append(callout(
        '<b>Regulatory Dialectic:</b> The cyclical process in which each new '
        'regulation generates market innovations designed to circumvent it, '
        'producing more complex markets and more complex regulation with no '
        'net reduction in systemic risk. Described by economist Edward Kane '
        'as the "regulatory dialectic" in 1977.',
        S))
    story.append(SP(18))
    story.append(P(
        'The Basel accords, the international banking regulations negotiated '
        'through the Bank for International Settlements — demonstrate the '
        'regulatory cascade across three generations. Basel I (1988) introduced '
        'risk-weighted capital requirements to ensure banks held adequate capital '
        'against loan losses. The cascade from Basel I was the shadow banking '
        'system: by moving assets off balance sheet into structured investment '
        'vehicles, banks could maintain lending volume while reducing their '
        'measured capital requirements. Basel II (2004) addressed this by '
        'introducing more sophisticated risk measurement, including allowing '
        'banks to use their own internal models to calculate risk weights. '
        'The cascade from Basel II was model risk: banks had incentives to '
        'build models that minimised measured risk, and the complexity of the '
        'models made it difficult for regulators to verify their accuracy. '
        'Basel III (2010), designed in response to the 2008 crisis, addressed '
        'model risk by imposing additional capital buffers and liquidity '
        'requirements. The cascade from Basel III is currently unfolding: '
        'the complexity of compliance has accelerated the concentration of '
        'the banking sector (as only large banks can afford compliance '
        'infrastructure), increased the cost of credit for small businesses, '
        'and pushed lending activity further into the non-bank financial '
        'sector, where Basel III does not apply.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The pharmaceutical regulatory cascade follows a structurally identical '
        'pattern. The 1962 Kefauver-Harris Amendment, enacted in response to '
        'the thalidomide tragedy, required drug manufacturers to demonstrate '
        'efficacy as well as safety before approval, a major advance in '
        'consumer protection. The cascade from the 1962 Amendment was the '
        'clinical trial arms race: as approval requirements became more '
        'stringent, the cost of drug development increased, favouring large '
        'pharmaceutical companies with capital to fund Phase III trials '
        'and disadvantaging academic researchers and small biotechnology '
        'firms. Drug approval times lengthened from an average of 8 months '
        'in 1960 to over 30 months by 1980. The regulatory response, '
        'the Prescription Drug User Fee Act of 1992 (PDUFA), which '
        'allowed the FDA to collect fees from drug manufacturers to fund '
        'faster review, introduced a new cascade: a regulator financially '
        'dependent on industry fees, creating at minimum the appearance '
        'of regulatory capture and contributing to the approval of drugs '
        'like Vioxx, which was withdrawn in 2004 after causing an '
        'estimated 38,000 heart attacks. Each regulatory solution '
        'generated the conditions for the next regulatory failure.',
        S['body']))
    story.append(SP(14))

    story.append(SP(18))
    story.append(P('Intellectual Property and the Innovation Paradox', S['section']))
    story.append(P(
        'Patent law solved the problem of the public goods dilemma in '
        'innovation: without intellectual property protection, inventors '
        'cannot capture the returns to their inventions, and rational '
        'actors will underinvest in innovation. The solution was the '
        'patent bargain, a time-limited monopoly granted to inventors '
        'in exchange for public disclosure of the invention. The theory '
        'is elegant; the practice has generated cascades that now threaten '
        'the very innovation the system was designed to encourage.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'Software patents provide the most vivid illustration. The '
        'extension of patent protection to software algorithms in the '
        '1980s and 1990s, through judicial decisions rather than '
        'legislative choice, created a new class of property that '
        'previous legal frameworks had not anticipated. The cascade '
        'was the patent troll ecosystem: entities that acquire patents '
        'not to practice them but to extract licensing fees from '
        'operating companies. By 2012, US companies were spending more '
        'on patent litigation and licensing than on research and '
        'development in several technology sectors. A study by Bessen '
        'and Meurer (2014) estimated that patent trolls cost the US '
        'economy $29 billion annually in direct costs alone, not '
        'counting the chilling effect on innovation from the threat '
        'of litigation.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'Pharmaceutical patents generate a cascade of a different type: '
        'evergreening. Drug companies, facing the expiration of '
        'profitable patents, make minor modifications to existing '
        'drugs, a new dosage form, a new delivery mechanism, a '
        'combination with another drug, and apply for new patents '
        'that extend the period of monopoly pricing. An analysis '
        'published in JAMA Internal Medicine (2018) found that of '
        '100 best-selling drugs studied, 74 had been evergreened, '
        'with an average of 4.7 patents per drug added after the '
        'original patent. The evergreening cascade means that '
        'drugs remain off-patent, and therefore available as '
        'low-cost generics, for far less time than the statutory '
        '20-year patent term would suggest. Insulin, first '
        'synthesised in 1921 and in continuous use for over a '
        'century, costs approximately $98 per vial in Canada and '
        'approximately $98 per vial in Germany; it costs '
        'approximately $98 in Australia. In the United States, '
        'the same insulin costs approximately $275-450 per vial, '
        'a difference attributable almost entirely to a cascade '
        'of secondary patents, regulatory exclusivities, and '
        'pharmacy benefit manager contracts that collectively '
        'replicate the economic effect of patent monopoly long '
        'after the original patents expired.',
        S['body']))
    story.append(SP(14))
    story += epigraph(
        'The patent system added the fuel of interest to the fire of genius.',
        'Abraham Lincoln, 1858',
        S)
    story.append(SP(14))
    story.append(P(
        'Lincoln\'s metaphor was prescient in ways he did not intend. '
        'Fire, once established, generates its own dynamics. '
        'The fuel of interest (the profit motive in innovation) '
        'has generated not only the fire of genius but also the '
        'smoke of litigation, the ash of evergreening, the '
        'structural smoke of patent thickets that block follow-on '
        'research in biotechnology and genomics. The Myriad '
        'Genetics case, in which the company held patents on '
        'the BRCA1 and BRCA2 genes associated with breast '
        'cancer risk, blocking other researchers from developing '
        'diagnostic tests, illustrates how intellectual property '
        'designed to incentivise innovation can cascade into '
        'intellectual property that blocks innovation. The '
        'Supreme Court\'s 2013 ruling in Association for '
        'Molecular Pathology v. Myriad Genetics, which '
        'invalidated gene patents, was a regulatory response '
        'to a cascade that had taken decades to become visible '
        'and costly.',
        S['body']))
    story.append(SP(14))

    story.append(SP(18))
    story.append(P('Chapter 6 Synthesis: Economics as the Study of Cascade', S['section']))
    story.append(P(
        'Economics is, at its core, the study of how solutions to problems '
        'of resource allocation generate new resource allocation problems. '
        'The market is a cascade engine: every price signal solved by '
        'one actor creates new coordination challenges for others. Every '
        'institutional innovation designed to improve market function '
        'creates new surfaces for exploitation. Every regulatory '
        'intervention generates new strategies for circumvention.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The examples in this chapter are not failures of economics as a '
        'discipline or of markets as institutions. They are the predictable '
        'outputs of complex adaptive systems operating exactly as described '
        'by cascade theory. The Cobra Effect, Jevons Paradox, Goodhart\'s '
        'Law, the regulatory dialectic, the distributional cascade of trade '
        'liberalisation, each represents a case where a solution worked '
        'as designed, and the working of the solution generated the '
        'conditions for the next problem. What distinguishes economics '
        'from other domains of cascade generation is that economic actors '
        'are explicitly strategic: they anticipate regulation and innovate '
        'to circumvent it; they arbitrage price differences; they optimise '
        'for measurable targets. This strategic adaptation accelerates the '
        'cascade cycle. In biology, evolution works on timescales of '
        'generations. In economics, adaptation works on timescales of '
        'quarters. The cascade cycle is correspondingly faster.',
        S['body']))
    story.append(SP(14))
    story.append(callout(
        '<b>Key Insight:</b> Economic actors are unique cascade generators '
        'because they are explicitly strategic; they anticipate and adapt '
        'to solutions faster than regulators can design them. This strategic '
        'adaptation compresses the cascade cycle from decades to quarters, '
        'making economic cascades among the most rapidly-evolving in the '
        'entire taxonomy of cascade types.',
        S))
    story.append(SP(14))
    story.append(P(
        'The deepest insight from economic cascades is the measurement '
        'problem. Economies are too complex to measure fully; the '
        'statistics we use: GDP, unemployment, inflation, trade '
        'balances are representations of economic reality, not '
        'economic reality itself. When policy is designed to '
        'optimise for measured statistics, and when economic actors '
        'respond to policy by shifting activity from measured to '
        'unmeasured categories, the measured statistics improve '
        'while the underlying reality may deteriorate. GDP growth '
        'is compatible with declining life expectancy, worsening '
        'mental health, environmental degradation, and '
        'infrastructure decay, as has been observed in the '
        'United States between approximately 2000 and 2020. '
        'The cascade from the solution of GDP as a comprehensive '
        'measure of national welfare is a governing class '
        'optimising for a statistic that has become progressively '
        'less representative of the welfare it was designed to measure.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The twenty-first century faces an economic cascade of unusual '
        'severity: the automation cascade from artificial intelligence. '
        'Unlike previous automation, which displaced physical labour '
        'while creating new demand for cognitive labour — AI automation '
        'threatens cognitive labour directly. The historical evidence '
        'that technology creates more jobs than it destroys is based '
        'on two centuries of mechanisation of physical tasks. Whether '
        'the same pattern holds when the mechanised tasks are '
        'cognitive: writing, analysis, diagnosis, legal reasoning, '
        'creative work is not established by historical precedent. '
        'The cascade from the solution to the problem of cognitive '
        'labour costs may be without historical analogue.',
        S['body']))
    story.append(SP(18))

    # ------------------------------------------------------------------ #
    # EXTENDED: The Housing Crisis as Cascade Archetype                    #
    # ------------------------------------------------------------------ #
    story.append(SP(18))
    story.append(P('The Housing Crisis: When Affordability Becomes a Cascade System', S['section']))
    story.append(P(
        'The housing affordability crisis in major cities worldwide '
        'is among the most consequential economic cascades of the '
        'twenty-first century. It is not, however, a single cascade '
        '— it is a convergence of multiple independent cascades, '
        'each generated by a different solution, that have '
        'interacted to produce a housing market in which '
        'ownership is beyond reach for median-income earners '
        'in virtually every major global city.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The first cascade is the mortgage securitisation cascade. '
        'The development of mortgage-backed securities in the '
        '1970s solved the problem of geographic constraints '
        'on mortgage lending, local savings banks could '
        'only lend as much as local depositors had saved, '
        'limiting credit availability in high-demand areas. '
        'Securitisation allowed mortgages to be pooled, '
        'rated, and sold to investors globally, '
        'dramatically expanding the availability '
        'of mortgage credit. The cascade was the '
        '2008 housing bubble and its aftermath. '
        'As documented in Chapter 6, the crisis '
        'cost approximately $22 trillion in '
        'global wealth. Less discussed is its '
        'cascade on housing supply: the crisis '
        'caused a decade-long collapse in '
        'residential construction that created '
        'a structural housing shortage in '
        'many major markets, directly contributing '
        'to the affordability crisis of the 2010s.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The second cascade is the zoning and planning '
        'restriction cascade. Single-family zoning, '
        'height restrictions, parking minimums, '
        'setback requirements, and environmental '
        'review processes, each designed to '
        'solve a specific problem (neighbourhood '
        'character preservation, fire safety, '
        'traffic management, environmental '
        'protection) have collectively '
        'created a regulatory environment '
        'that makes new housing construction '
        'extraordinarily difficult in '
        'high-demand areas. San Francisco '
        'issued approximately 1,400 new '
        'housing units annually in the '
        '2010s, against a metropolitan area '
        'of 4 million people and job growth '
        'of tens of thousands per year. '
        'The cascade from the solutions to '
        'neighbourhood, traffic, and '
        'environmental problems is a '
        'housing supply that cannot '
        'respond to demand.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The third cascade is the investment vehicle cascade. '
        'Low interest rates following the 2008 crisis, '
        'themselves a solution to the post-crisis '
        'demand deficiency — made residential property '
        'an increasingly attractive investment vehicle '
        'compared to bonds and savings accounts. '
        'Institutional investors, individuals '
        'purchasing buy-to-let properties, '
        'and real estate investment trusts '
        'expanded their holdings of residential '
        'property, competing with first-time '
        'buyers for the same scarce housing '
        'stock. The cascade from the '
        'monetary policy solution to the '
        '2008 crisis is the further '
        'restriction of housing access '
        'for first-time buyers, compounding '
        'the supply cascade.',
        S['body']))
    story.append(SP(14))
    story.append(callout(
        '<b>The Housing Cascade Convergence:</b> The housing affordability crisis '
        'is produced by the interaction of at least three independent cascades, '
        'securitisation, zoning restriction, and investment vehicle '
        'financialisation, each generated by a different solution to a '
        'different problem. No single cascade-management intervention '
        'addresses all three simultaneously.',
        S))
    story.append(SP(14))
    story.append(P(
        'The political cascade from housing unaffordability '
        'is visible across generations. In countries '
        'where home ownership has historically been '
        'the primary vehicle for household wealth '
        'accumulation, the United Kingdom, '
        'Australia, Canada, declining home '
        'ownership rates among younger cohorts '
        'represent a structural shift in the '
        'distribution of wealth. Homeowners '
        '— who benefit from rising prices, '
        'have strong incentives to support '
        'zoning restrictions that limit '
        'new housing supply; renters have '
        'opposite incentives but, historically, '
        'lower political mobilisation. '
        'The political economy of housing '
        'systematically favours the cascade '
        'perpetuation: each cycle of rising '
        'prices increases the wealth of '
        'incumbent homeowners and their '
        'incentive to preserve the system, '
        'while increasing the hardship of '
        'those excluded from ownership. '
        'The cascade from the housing '
        'cascade is intergenerational '
        'wealth stratification that may '
        'prove as durable as any '
        'economic cascade in the '
        'historical record.',
        S['body']))
    story.append(SP(14))

    story.append(SP(18))
    story.append(P('The Gig Economy and the Labour Market Cascade', S['section']))
    story.append(P(
        'The gig economy, the model of engaging workers as '
        'independent contractors rather than employees, '
        'mediated by digital platforms, solved the '
        'problem of rigid labour markets. Traditional '
        'employment contracts imposed fixed costs '
        '(benefits, severance, minimum hours), '
        'which limited employers\' ability to '
        'adjust labour supply to variable '
        'demand. Platform-mediated gig work '
        'allowed flexible labour supply '
        'without fixed costs, enabling '
        'new business models (ride-sharing, '
        'food delivery, freelance services) '
        'that were not viable under '
        'traditional employment structures.',
        S['body0']))
    story.append(SP(14))
    story.append(P(
        'The cascade from gig work is the erosion of the '
        'employment relationship as the foundation of '
        'social insurance. The employment contract '
        'was the institutional vehicle through which '
        'the twentieth century delivered social '
        'protections: health insurance, pension '
        'contributions, unemployment insurance, '
        'workers\' compensation, paid leave, '
        'to the workforce. By reclassifying '
        'workers as independent contractors, '
        'platform companies shifted those '
        'costs onto workers (who must '
        'fund their own insurance and '
        'retirement) and onto the public '
        '(whose safety net programmes '
        'support workers without employer '
        'contributions). A 2021 study '
        'estimated that Uber drivers '
        'in the United States earn '
        'approximately $9.21 per hour '
        'after vehicle costs, below '
        'the minimum wage in many '
        'jurisdictions, and receive '
        'no benefits. The cascade '
        'from the solution to '
        'labour market rigidity is '
        'the decoupling of work '
        'from social protection.',
        S['body']))
    story.append(SP(14))
    story.append(P(
        'The automation cascade from the gig economy creates '
        'a second-order cascade: having established '
        'a business model based on flexible human '
        'labour, gig economy companies have a '
        'strong incentive to replace that labour '
        'with automation as soon as the technology '
        'allows. Autonomous vehicle technology '
        'would make Uber\'s entire driver '
        'network redundant. The gig economy '
        'has thus created a workforce '
        'that is both economically precarious '
        'in the present and facing '
        'technological displacement in '
        'the foreseeable future, a '
        'cascade-on-cascade structure '
        'that makes it one of the '
        'most consequential labour '
        'market developments since '
        'the original industrial '
        'transition.',
        S['body']))
    story.append(SP(14))

    story.append(SP(18))
    story.append(P('Google: Organising the World\'s Information — and Its Attention', S['section']))
    story.append(P(
        'In 1998, two PhD students at Stanford — Sergey Brin and Larry Page '
        '— solved a problem that the early web had made urgent: the explosion '
        'of online information had outpaced every existing method for organising '
        'it. Yahoo\'s human-curated directory could not scale. AltaVista\'s '
        'keyword matching was easily gamed. The problem was a genuine crisis '
        'of knowledge navigation. Brin and Page\'s solution: PageRank, '
        'an algorithm that ranked pages by the quality and quantity of other '
        'pages linking to them was elegant, mathematically sound, and '
        'almost immediately superior to every alternative. By 2004, Google '
        'had processed more searches than any previous information retrieval '
        'system in history. By 2023, it handled approximately 8.5 billion '
        'search queries per day, roughly one per second for every person '
        'alive on earth. Google did not just solve the information discovery '
        'problem. It became the primary interface between humanity and its '
        'accumulated knowledge. That achievement is genuinely historic. '
        'Its cascade is equally so.',
        S['body0']))
    story.append(P(
        '<b>The Advertising Cascade.</b> Google solved the problem of funding '
        'its search infrastructure by inventing AdWords in 2000, an '
        'auction-based system that sold advertising placements alongside '
        'search results, targeted to the keywords users were searching for. '
        'AdWords was a cascade event in the history of commerce: within a '
        'decade it had generated a $100 billion advertising market that '
        'systematically transferred advertising revenue from print media, '
        'television, and radio to Google, simultaneously destroying the '
        'financial model of local and national journalism. By 2019, '
        'Google and Facebook together captured approximately 61% of all '
        'digital advertising revenue in the United States. The cascade from '
        'this advertising concentration was the decimation of the news '
        'industry: US newsroom employment fell by 57% between 2008 and '
        '2020, with approximately 2,100 local newspapers closing entirely '
        'during the same period. The solution to information discovery '
        'funding generated a cascade that destroyed the institutions '
        '— investigative journalism, local news, the adversarial press '
        '— that had been the democratic ecosystem\'s primary mechanism '
        'for holding power accountable.',
        S['body']))
    story.append(P(
        '<b>The Search Quality Cascade.</b> Google\'s original PageRank '
        'algorithm ranked pages based on genuine link authority. '
        'The cascade from PageRank was search engine optimisation (SEO): '
        'an entire industry — employing hundreds of thousands of practitioners '
        'and generating over $80 billion in annual revenue by 2022, '
        'dedicated to gaming the algorithm rather than improving the content '
        'it was designed to surface. Google\'s response to the SEO cascade '
        'was algorithmic: hundreds of changes to the ranking algorithm '
        'over two decades, each designed to penalise the gaming behaviour '
        'of the previous era. The SEO industry adapted to each change '
        'and resumed gaming. By the 2020s, a significant fraction of '
        'the top-ranked pages for many commercial search queries were '
        'algorithmically generated content designed to rank, not to inform. '
        'The solution to information quality (PageRank) generated the '
        'information pollution cascade (SEO content farms), which generated '
        'the algorithmic response cascade (frequent algorithm updates), '
        'which generated the volatility cascade (businesses whose entire '
        'revenue depended on Google rankings facing ruin with each update). '
        'The cascade regenerates itself with each turn of the loop.',
        S['body']))
    story.append(P(
        '<b>The Map Cascade.</b> Google Maps solved the problem of navigation '
        'with such comprehensiveness that it became the de facto global '
        'mapping infrastructure: trusted by governments, emergency services, '
        'logistics companies, and two billion individual users. The cascade '
        'from that ubiquity is multi-dimensional. The privacy cascade: '
        'Google Maps\' real-time location tracking of users generates '
        'a continuous stream of location data that is among the most '
        'commercially and governmentally sensitive information ever '
        'systematically collected. US law enforcement agencies obtained '
        'Google location data in "geofence warrants" — requesting information '
        'on every device present in a given location at a given time, '
        'at a rate that grew by over 1,500% between 2018 and 2021. '
        'The navigation cascade: traffic redirection by Google Maps '
        'has demonstrably changed the routing patterns of millions of '
        'vehicles, sending traffic into residential neighbourhoods '
        'that were not designed for it, creating exactly the kind of '
        'second-order consequence that residents and local governments '
        'experience as an infuriating imposition with no clear author '
        'and no obvious remedy.',
        S['body']))
    story.append(callout(
        '<b>The Search Giant\'s Paradox:</b> Google\'s mission is to '
        '"organise the world\'s information and make it universally '
        'accessible and useful." In pursuit of that mission, it has '
        'simultaneously destroyed the journalism industry that produced '
        'much of the world\'s most important information, built the '
        'world\'s largest surveillance infrastructure, and created '
        'the SEO industry that pollutes the information ecosystem '
        'it was designed to organise. The mission is real and the '
        'achievement is genuine. The cascade is inseparable from both.',
        S))
    story.append(SP(14))
    story.append(fig_to_image(fig_google_journalism(), w=5.5*72, h=3.6*72))
    story.append(P(
        'Figure 6.1: Google advertising revenue versus US newsroom employment (2006–2023). '
        'As Google captured the global advertising market, local and national journalism '
        'lost the revenue base that sustained investigative reporting. By 2023, the US '
        'had lost over 60% of the newsroom jobs that existed in 2006, the same period '
        'in which Google generated over $237 billion in annual ad revenue.',
        S['caption']))

    story.append(SP(14))
    story.append(PageBreak())
    return story
