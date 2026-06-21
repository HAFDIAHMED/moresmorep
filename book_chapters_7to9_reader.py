from generate_book import *
from io import BytesIO


def fig_antibiotic_resistance_timeline():
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.5, 4.0))
        pairs=[('Penicillin\n1943',1943,0.78),('Resistance\n1947',1947,0.28),
               ('Methicillin\n1959',1959,0.78),('MRSA\n1961',1961,0.28),
               ('Vancomycin\n1958',1958,0.78),('VRE\n1987',1987,0.28),
               ('Linezolid\n2000',2000,0.78),('Linezolid\nRes. 2001',2001,0.28)]
        ax.axhline(0.5,color='black',lw=1.5)
        for label,yr,ypos in pairs:
            col='black' if ypos>0.5 else '#888'
            ax.plot(yr,0.5,'o',color=col,markersize=8)
            ax.plot([yr,yr],[0.5,ypos+(0.04 if ypos>0.5 else -0.04)],'-',color=col,lw=0.8)
            ax.text(yr,ypos,label,ha='center',fontsize=7,color=col,
                   bbox=dict(boxstyle='round,pad=0.2',facecolor='white',edgecolor=col))
        ax.set_xlim(1938,2010); ax.set_ylim(0,1); ax.axis('off')
        ax.set_title('Antibiotic Introduction -> Resistance: The Arms Race Timeline',fontsize=10)
        buf=BytesIO(); fig.savefig(buf,format='png',dpi=150,bbox_inches='tight'); buf.seek(0); plt.close(fig)
    return Image(buf,width=5.5*inch,height=3.6*inch)


def fig_opioid_deaths():
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.5, 3.5))
        years=list(range(1999,2024))
        # CDC WONDER: total drug overdose deaths, ICD-10 X40-X44/X60-X64/X85/Y10-Y14
        # Source: https://www.cdc.gov/drugoverdose/data/statedeaths.html
        deaths=[16849,17415,19394,23518,25785,29813,36010,38371,36450,38329,
                40393,43982,47055,52404,52898,63632,70237,68557,70630,81230,
                75673,80411,80816,81083,80000]
        ax.fill_between(years,deaths,alpha=0.3,color='black')
        ax.plot(years,deaths,'k-',lw=2)
        # OxyContin FDA approval: December 1995 — annotated at 1999 (first data year)
        for yr,val,label in [(1999,16849,'OxyContin\napproved\n(1996)'),(2010,38329,'Reformulation\n->heroin shift'),
                             (2013,47055,'Fentanyl\nbegins'),(2016,63632,'National\nemergency')]:
            ax.annotate(label,(yr,val),xytext=(yr+0.5,val+8000),
                       arrowprops=dict(arrowstyle='->',color='black'),fontsize=7)
        ax.set_xlabel('Year'); ax.set_ylabel('Drug Overdose Deaths')
        ax.set_title('US Drug Overdose Deaths 1999-2023 (CDC WONDER)')
        buf=BytesIO(); fig.savefig(buf,format='png',dpi=150,bbox_inches='tight'); buf.seek(0); plt.close(fig)
    return Image(buf,width=5.5*inch,height=3.2*inch)


def fig_crispr_cascade():
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.5, 3.8))
        ax.text(0.5,0.92,'CRISPR (2012): "Cure genetic disease"',
               ha='center',va='top',fontsize=10,fontweight='bold',zorder=5,
               bbox=dict(boxstyle='round',facecolor='white',edgecolor='black',lw=2))
        probs=[(0.12,0.58,'Off-target\nedits'),(0.35,0.58,'Mosaicism\n(incomplete)'),(0.62,0.58,'Germline\nchanges'),(0.88,0.58,'Designer\nbabies')]
        for x,y,text in probs:
            ax.annotate('',xy=(x,y+0.10),xytext=(0.5,0.82),zorder=1,arrowprops=dict(arrowstyle='->',color='black'))
            ax.text(x,y,text,ha='center',va='top',fontsize=8,zorder=5,
                   bbox=dict(boxstyle='round',facecolor='#f0f0f0',edgecolor='black'))
        subs=[(0.12,0.28,'Cancer\nrisk?'),(0.35,0.28,'Unknown\ncell mix'),(0.62,0.28,'Eugenics\nfear'),(0.88,0.28,'Genetic\ninequality')]
        for (x,y,text),(px,_,_) in zip(subs,probs):
            ax.annotate('',xy=(x,y+0.08),xytext=(px,0.52),zorder=1,arrowprops=dict(arrowstyle='->',color='#666'))
            ax.text(x,y,text,ha='center',va='top',fontsize=7,zorder=5,bbox=dict(boxstyle='round',facecolor='#e0e0e0',edgecolor='#888'))
        ax.set_xlim(0,1); ax.set_ylim(0.18,1.0); ax.axis('off')
        ax.set_title('The CRISPR Cascade: Each Benefit Creates New Risks',fontsize=10)
        buf=BytesIO(); fig.savefig(buf,format='png',dpi=150,bbox_inches='tight'); buf.seek(0); plt.close(fig)
    return Image(buf,width=5.5*inch,height=3.6*inch)


def fig_microbiome_cascade():
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.5, 3.5))
        ax.text(0.5,0.92,'ANTIBIOTICS (solving infection)',ha='center',va='top',fontsize=11,fontweight='bold',zorder=5,
               bbox=dict(boxstyle='round',facecolor='white',edgecolor='black',lw=2))
        effects=[(0.15,0.60,'C. diff\n30K deaths/yr'),(0.4,0.60,'Gut\ndysbiosis'),(0.65,0.60,'Immune\ndysregulation'),(0.88,0.60,'Resistance\nspread')]
        downstream=[(0.15,0.28,'FMT\n(poop pills)'),(0.4,0.28,'Allergy\nAsthma\nObesity'),(0.65,0.28,'Type 1\nDiabetes(+)'),(0.88,0.28,'Untreatable\ninfections')]
        for (x,y,text),(dx,dy,dt) in zip(effects,downstream):
            ax.annotate('',xy=(x,y+0.09),xytext=(0.5,0.82),zorder=1,arrowprops=dict(arrowstyle='->',color='black'))
            ax.text(x,y,text,ha='center',va='top',fontsize=8,zorder=5,bbox=dict(boxstyle='round',facecolor='#f0f0f0',edgecolor='black'))
            ax.annotate('',xy=(dx,dy+0.08),xytext=(x,y-0.01),zorder=1,arrowprops=dict(arrowstyle='->',color='#555'))
            ax.text(dx,dy,dt,ha='center',va='top',fontsize=7,zorder=5,bbox=dict(boxstyle='round',facecolor='#e0e0e0',edgecolor='#888'))
        ax.set_xlim(0,1); ax.set_ylim(0.18,1.0); ax.axis('off')
        ax.set_title('The Antibiotic-Microbiome Cascade',fontsize=10)
        buf=BytesIO(); fig.savefig(buf,format='png',dpi=150,bbox_inches='tight'); buf.seek(0); plt.close(fig)
    return Image(buf,width=5.5*inch,height=3.4*inch)


def fig_prohibition_homicide():
    import numpy as np
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.5, 3.5))
        years=list(range(1910,1942))
        homicides=[4.6,5.5,5.4,6.1,6.2,5.9,6.3,6.9,6.5,7.2,6.8,7.2,8.0,8.8,9.7,8.3,7.4,6.5,6.2,5.8,5.3,5.1,4.8,4.5,4.5,4.6,4.8,4.7,5.0,4.9,4.9,4.8]
        ax.plot(years,homicides,'k-',lw=2)
        ax.axvspan(1920,1933,alpha=0.15,color='black')
        ax.axvline(1920,color='black',lw=1.5,linestyle='--')
        ax.axvline(1933,color='black',lw=1.5,linestyle='--')
        ax.text(1926.5,9.5,'PROHIBITION\n1920-1933',ha='center',fontsize=9,fontweight='bold')
        ax.set_xlabel('Year'); ax.set_ylabel('Homicide Rate per 100,000')
        ax.set_title("US Homicide Rates: Prohibition's Unintended Consequence")
        buf=BytesIO(); fig.savefig(buf,format='png',dpi=150,bbox_inches='tight'); buf.seek(0); plt.close(fig)
    return Image(buf,width=5.5*inch,height=3.2*inch)


def fig_war_on_drugs_incarceration():
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.5, 3.5))
        years=[1972,1975,1980,1985,1990,1995,2000,2005,2008,2012,2016,2020,2023]
        prisoners=[300,380,503,744,1148,1585,1937,2186,2307,2228,2162,2019,1900]
        ax.fill_between(years,prisoners,alpha=0.25,color='black')
        ax.plot(years,prisoners,'k-o',lw=2,markersize=5)
        ax.axvline(1971,color='black',lw=1,linestyle='--')
        ax.text(1972,2350,'War on\nDrugs\n1971',fontsize=8)
        ax.set_xlabel('Year'); ax.set_ylabel('Prison Population (thousands)')
        ax.set_title('US Prison Population 1972-2023: The Mass Incarceration Cascade')
        buf=BytesIO(); fig.savefig(buf,format='png',dpi=150,bbox_inches='tight'); buf.seek(0); plt.close(fig)
    return Image(buf,width=5.5*inch,height=3.2*inch)


def fig_drug_policy_comparison():
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.5, 3.8))
        countries=['USA\n(War on Drugs)','Sweden\n(Strict)','Netherlands\n(Tolerance)','Portugal\n(Decrim 2001)']
        # USA: CDC WONDER 2022, ~107k drug overdose deaths / 332M pop = 322/million;
        # using EMCDDA-comparable ICD coding (~75% of total) -> ~240/million
        # EU countries: EMCDDA 2022, drug-induced deaths per million total population
        # Sweden: 87/million (15-64) -> ~62/million total pop (EMCDDA 2022)
        # Netherlands: 15/million total pop (EMCDDA 2022)
        # Portugal: 3.1/million total pop (EMCDDA 2022, lowest in EU)
        drug_deaths=[240.0, 62.0, 15.0, 3.1]
        bars=ax.bar(range(len(countries)),drug_deaths,color=['black','#555','#aaa','#ccc'])
        ax.set_xticks(range(len(countries))); ax.set_xticklabels(countries,fontsize=8)
        ax.set_ylabel('Drug-induced deaths per million population')
        ax.set_title('Drug Policy Outcomes: Deaths per Million Population\n'
                     'USA (CDC 2022) vs EU Alternatives (EMCDDA 2022)', fontsize=9)
        for bar,val in zip(bars,drug_deaths):
            ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+2,
                    f'{val:.0f}', ha='center', fontsize=9, fontweight='bold')
        ax.set_ylim(0, 270)
        fig.tight_layout()
        buf=BytesIO(); fig.savefig(buf,format='png',dpi=150,bbox_inches='tight'); buf.seek(0); plt.close(fig)
    return Image(buf,width=5.5*inch,height=3.4*inch)


def fig_social_media_mental_health():
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.5, 3.5))
        years=[2005,2007,2009,2011,2013,2015,2017,2019,2021]
        sm=[5,15,30,50,65,72,78,81,85]
        depression=[26,27,28,32,35,38,44,50,57]
        ax.plot(years,sm,'k--o',lw=2,label='Teen Social Media Use (%)')
        ax.plot(years,depression,'k-s',lw=2.5,label='Teen Girls: Persistent Sadness (%)')
        ax.axvline(2009,color='black',lw=1,linestyle=':')
        ax.text(2009.2,55,'Like button\n2009',fontsize=8)
        ax.set_xlabel('Year'); ax.set_ylabel('Percentage (%)')
        ax.set_title('Social Media Adoption vs. Teen Mental Health (2005-2021)')
        ax.legend(fontsize=8,loc='upper left')
        buf=BytesIO(); fig.savefig(buf,format='png',dpi=150,bbox_inches='tight'); buf.seek(0); plt.close(fig)
    return Image(buf,width=5.5*inch,height=3.2*inch)


def fig_green_revolution_tradeoffs():
    import numpy as np
    with plt.xkcd():
        fig, axes = plt.subplots(1,2,figsize=(6.5,3.2))
        years=[1961,1970,1980,1990,2000,2010,2020]
        axes[0].plot(years,[1.2,1.7,2.3,2.7,2.7,3.1,3.5],'k-o',lw=2)
        axes[0].fill_between(years,[1.2,1.7,2.3,2.7,2.7,3.1,3.5],alpha=0.2,color='black')
        axes[0].set_title('Wheat Yields (t/ha)\nThe Success'); axes[0].set_ylabel('Tonnes/hectare')
        axes[1].plot(years,[50,100,150,200,300,380,400],'k-o',lw=2,label='Dead zones')
        ax2=axes[1].twinx()
        ax2.plot(years,[10,15,20,28,35,38,40],'k--s',lw=2,label='Degraded land %')
        axes[1].set_ylabel('Coastal dead zones'); ax2.set_ylabel('Degraded land (%)')
        axes[1].set_title('Environmental Costs\nThe Cascade')
        fig.suptitle('The Green Revolution: Undeniable Success, Compounding Cascade',fontsize=9)
        plt.tight_layout()
        buf=BytesIO(); fig.savefig(buf,format='png',dpi=150,bbox_inches='tight'); buf.seek(0); plt.close(fig)
    return Image(buf,width=5.5*inch,height=3.0*inch)


def fig_ac_heat_island():
    import numpy as np
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.5, 3.5))
        years=np.array([1950,1960,1970,1980,1990,2000,2010,2020])
        ac_pct=np.array([0.1,5,25,50,65,75,87,91])
        temp_rise=np.array([0,0.5,1.0,2.0,3.5,5.5,6.5,8.0])
        ax.bar(years,ac_pct,color='#aaa',alpha=0.5,width=7,label='% US Homes with AC')
        ax2=ax.twinx()
        ax2.plot(years,temp_rise,'k-o',lw=2.5,label='Phoenix avg low temp increase (\u00b0F)')
        ax.set_xlabel('Year'); ax.set_ylabel('% US Homes with AC')
        ax2.set_ylabel('Phoenix Temperature Increase (\u00b0F from 1950)')
        ax.set_title('Air Conditioning -> Urban Heat Island Feedback Loop')
        ax.legend(loc='upper left',fontsize=8); ax2.legend(loc='center left',fontsize=8)
        buf=BytesIO(); fig.savefig(buf,format='png',dpi=150,bbox_inches='tight'); buf.seek(0); plt.close(fig)
    return Image(buf,width=5.5*inch,height=3.2*inch)


def fig_healthcare_spiral():
    """US health spending vs life expectancy vs OECD peers."""
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.5, 3.8))
        countries = ['US', 'UK', 'Germany', 'France', 'Japan', 'Canada', 'Australia']
        spending  = [12530, 4264, 6731, 5468, 4717, 5905, 5765]   # USD per capita 2022
        life_exp  = [76.4, 81.3, 81.1, 82.3, 84.3, 82.2, 83.3]   # years 2022
        ax.scatter(spending, life_exp, s=100, color='black', zorder=5)
        for i, c in enumerate(countries):
            offset = (120, 0.1) if c != 'US' else (-400, -0.4)
            ax.annotate(c, (spending[i], life_exp[i]),
                        xytext=(spending[i]+offset[0], life_exp[i]+offset[1]),
                        fontsize=8)
        ax.set_xlabel('Health expenditure per capita (USD, 2022)')
        ax.set_ylabel('Life expectancy at birth (years)')
        ax.set_title('The Healthcare Paradox: More Spending, Less Life')
        ax.set_xlim(3000, 14000)
        ax.set_ylim(74, 86)
        # trend line excluding US
        xs = np.array(spending[1:])
        ys = np.array(life_exp[1:])
        m, b = np.polyfit(xs, ys, 1)
        xfit = np.linspace(3000, 13000, 100)
        ax.plot(xfit, m*xfit + b, 'k--', lw=1.2, alpha=0.5)
        fig.tight_layout()
    return fig


def fig_surveillance_cascade():
    """Post-9/11 surveillance: agencies + budget cascade bars."""
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(6.5, 3.5))
        categories = ['Intelligence\nagencies', 'Private\ncontractors\n(000s)',
                      'Annual intel\nbudget ($B)', 'Data centres\n(major)']
        pre  = [8,  50,  40,  2]
        post = [17, 500, 85, 17]
        x = np.arange(len(categories))
        w = 0.35
        ax.bar(x - w/2, pre,  w, label='Pre-9/11 (2000)', color='black', alpha=0.45)
        ax.bar(x + w/2, post, w, label='Post-9/11 (2023)', color='black', alpha=0.85)
        ax.set_xticks(x); ax.set_xticklabels(categories, fontsize=8)
        ax.set_ylabel('Scale (normalised units)')
        ax.set_title('The Security Cascade: Solving Terrorism Created a Surveillance State')
        ax.legend(fontsize=8)
        fig.tight_layout()
    return fig


def fig_attention_economy():
    """Circular dopamine loop diagram for social media attention economy."""
    with plt.xkcd():
        fig, ax = plt.subplots(figsize=(5.5, 5.5))
        ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.6, 1.6)
        ax.set_aspect('equal'); ax.axis('off')
        ax.set_title('The Attention Economy Loop', pad=18)
        # nodes
        nodes = [
            ('Platform\nOptimises\nEngagement', 0, 1.1),
            ('User Gets\nDopamine Hit', 1.0, 0.3),
            ('Tolerance\nBuilds', 0.6, -0.9),
            ('More\nScrolling\nNeeded', -0.6, -0.9),
            ('Mental\nHealth\nDeclines', -1.0, 0.3),
        ]
        for label, nx, ny in nodes:
            ax.text(nx, ny, label, ha='center', va='center', fontsize=8, zorder=5,
                    bbox=dict(boxstyle='round,pad=0.4', fc='white', ec='black', lw=1.5))
        # arrows in a circle
        angles = [90, 90-72, 90-144, 90-216, 90-288]
        r = 1.05
        for i in range(5):
            a1 = np.radians(angles[i] - 28)
            a2 = np.radians(angles[(i+1) % 5] + 28)
            x1, y1 = r*np.cos(a1), r*np.sin(a1)
            x2, y2 = r*np.cos(a2), r*np.sin(a2)
            ax.annotate('', xy=(x2, y2), xytext=(x1, y1), zorder=1,
                        arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
        fig.tight_layout()
    return fig


def chapter7(S):
    story = []
    story += chapter_opener('Chapter Seven',
        'Medicine \u2014 The Healing Paradox',
        'Every medical advance creates the conditions for the next medical crisis', S)
    story += epigraph(
        'First, do no harm.',
        'Attributed to Hippocrates, though absent from his actual writings \u2014 '
        'itself an unintended consequence of attribution cascades', S)
    story += [SP(12)]
    story.append(Mark(chapter='Medicine \u2014 The Healing Paradox'))

    # ------------------------------------------------------------------ #
    # Section 1: Antibiotic Resistance                                     #
    # ------------------------------------------------------------------ #
    story.append(SP(22))
    story.append(P('The Antibiotic Revolution \u2014 and Its Reversal', S['section']))
    story.append(SP(14))

    story.append(P(
        'September 28, 1928. Alexander Fleming comes back from a summer holiday to a '
        'contaminated petri dish on his bench at St Mary\'s Hospital in London. A mould \u2014 '
        '<i>Penicillium notatum</i> \u2014 is growing on a <i>Staphylococcus</i> culture plate '
        'he had left exposed. Around the spreading colony of mould, the bacteria are dead. '
        'Fleming later wrote that he nearly threw the dish away. Something about the '
        'halo of dead bacteria made him pause. He subcultured the mould, called the '
        'antibacterial substance it produced "penicillin," and in 1929 published a paper '
        'in the <i>British Journal of Experimental Pathology</i>. The paper attracted '
        'almost no attention. A decade later, Howard Florey and Ernst Chain at Oxford '
        'purified penicillin to a usable form and showed it could cure otherwise fatal '
        'bacterial infections in mice \u2014 and, within a year, in humans. By 1943 the drug '
        'was being mass-produced in the United States and shipped to Allied armies in '
        'North Africa and Europe. Wound infections that had killed more soldiers than '
        'enemy action in every previous war were suddenly survivable. Pneumonia, '
        'septicaemia, syphilis, scarlet fever, bacterial endocarditis \u2014 diseases that had '
        'been death sentences \u2014 became curable in days. Fleming, Florey, and Chain shared '
        'the Nobel in 1945.',
        S['body0']))
    story.append(SP(14))

    story.append(P(
        'Fleming saw the cascade before it arrived. In his Nobel acceptance lecture in '
        'December 1945 he said this: <i>The time may come when penicillin can be bought '
        'by anyone in the shops. Then there is the danger that the ignorant man may easily '
        'under-dose himself and by exposing his microbes to non-lethal quantities of the '
        'drug make them resistant.</i> He was right about the mechanism, right about the '
        'timeline, and catastrophically right about the scale. Penicillin-resistant '
        '<i>Staphylococcus aureus</i> had been isolated in laboratory settings in 1940, '
        'before the drug was even in clinical use. By 1947 \u2014 just four years after '
        'penicillin reached patients at scale \u2014 resistant strains were appearing in '
        'hospitals across Britain and the United States. The gap between solution and '
        'cascade was measured not in decades but in years.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The resistance timeline that followed is one of the most precisely documented '
        'cascades in all of medicine, and its acceleration is the feature that should '
        'most alarm us. Methicillin, a penicillin-resistant form of penicillin designed '
        'specifically to defeat the resistance mechanism of Staphylococcus aureus, was '
        'introduced in 1959. Methicillin-resistant Staphylococcus aureus \u2014 MRSA, '
        'the "superbug" that now haunts hospitals worldwide \u2014 was identified in 1961: '
        'just two years after the drug\'s introduction. Vancomycin, the antibiotic of '
        'last resort for gram-positive infections for most of the late twentieth century, '
        'was introduced in 1958 and remained effective for nearly three decades before '
        'vancomycin-resistant Enterococcus (VRE) emerged in 1987. Linezolid, approved by '
        'the FDA in 2000 as a treatment for MRSA and VRE infections, met resistance within '
        'a single year: linezolid-resistant strains were documented in 2001. The pattern '
        'is unambiguous and worsening: each new antibiotic generates resistance faster than '
        'its predecessor, because the bacterial ecosystem has been under continuous '
        'antibiotic selection pressure for decades and has become progressively more '
        'sophisticated at deploying and spreading resistance mechanisms. The evolutionary '
        'arms race has a structural asymmetry: bacteria can evolve new resistance '
        'mechanisms in months; humans require ten to fifteen years and over a billion '
        'dollars to develop a new antibiotic.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The cascade was dramatically amplified by a second-order decision that the '
        'antibiotic pioneers did not foresee: the mass use of antibiotics in agriculture. '
        'Farmers discovered in the 1950s that sub-therapeutic doses of antibiotics \u2014 '
        'doses too low to treat infection \u2014 promoted faster growth in livestock, '
        'apparently by suppressing the low-level bacterial infections that waste metabolic '
        'energy in densely confined animals. By 2011, the US Food and Drug Administration '
        'estimated that 80 percent of all antibiotics sold in the United States were used '
        'in agriculture, the vast majority for growth promotion rather than disease '
        'treatment. Factory farms \u2014 in which tens of thousands of animals are '
        'confined in conditions ideal for bacterial transmission \u2014 became the world\'s '
        'largest incubators of antibiotic-resistant bacteria. Resistant strains colonise '
        'farm workers, enter the food supply through meat products, and spread through '
        'water and soil contamination. The European Union banned growth-promotion antibiotic '
        'use in 2006; the United States did not formally restrict it until 2017. By then, '
        'the resistance cascade in agricultural settings had been running at industrial '
        'scale for sixty years.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The scale of the coming mortality cascade was quantified by the O\'Neill Review '
        'on Antimicrobial Resistance, commissioned by the UK government and chaired by '
        'economist Jim O\'Neill, whose final report was published in 2016. The review '
        'found that antibiotic-resistant infections were then killing around 700,000 '
        'people a year worldwide; the more rigorous 2019 estimate \u2014 the Lancet GRAM '
        'study (2022) \u2014 put the toll far higher, at 1.27 million deaths directly '
        'attributable and nearly 5 million associated. On current trends, the review '
        'projected that resistance could kill 10 million people annually by 2050 (a widely '
        'cited but much-debated forecast), surpassing cancer as the world\'s '
        'leading cause of death, with cumulative economic losses of more than $100 trillion. '
        'The WHO\'s 2023 priority pathogen list identifies nineteen bacterial families '
        'posing the greatest threat, including carbapenem-resistant Acinetobacter '
        'baumannii \u2014 described by WHO as "critical" priority \u2014 which is now '
        'resistant to nearly all available antibiotics and kills up to 50 percent of '
        'infected patients in intensive care settings.',
        S['body']))
    story.append(SP(14))

    story.append(callout(
        '<b>The O\'Neill Report (2016):</b> If no action is taken, antimicrobial resistance will kill 10 million people '
        'per year by 2050 \u2014 more than cancer. The cumulative cost to global GDP '
        'would exceed $100 trillion. At the time of the report some 700,000 people died annually from '
        'drug-resistant infections; no new classes of antibiotics have reached the '
        'market since 1987.',
        S))
    story.append(SP(14))

    story.append(P(
        'The pipeline paradox is the cascade\'s cruelest feature. The pharmaceutical '
        'industry has largely abandoned antibiotic development because the economics are '
        'structurally incompatible with drug-company business models. A new antibiotic '
        'takes ten to fifteen years and over a billion dollars to develop, test, and '
        'bring to market. Once approved, responsible use requires holding it in reserve '
        '\u2014 using it rarely, only for infections where no other option works, to '
        'delay the emergence of resistance. A drug used rarely generates minimal revenue. '
        'The financial return on antibiotic development is therefore far lower than the '
        'return on drugs taken daily for chronic conditions: statins, antidepressants, '
        'antihypertensives. Between 1980 and 2000, eighteen new classes of antibiotics '
        'reached the market. Between 2000 and 2020, just two did. The last truly new '
        'antibiotic class \u2014 one with a novel mechanism of action against gram-negative '
        'bacteria \u2014 reached the market in 1987. The solution to the antibiotic '
        'resistance cascade requires precisely the drugs that the market system generated '
        'by the original antibiotic cascade cannot profitably produce.',
        S['body']))
    story.append(SP(14))

    story.append(fig_antibiotic_resistance_timeline())
    story.append(SP(8))
    story.append(P(
        'Figure 7.1: The antibiotic arms race timeline. Each drug introduced (above the '
        'line) generated resistance within years \u2014 and the gap between introduction '
        'and resistance has narrowed from four years (penicillin) to one year (linezolid). '
        'The solution to bacterial infection has created an accelerating cascade that '
        'threatens to eliminate the entire antibiotic toolkit.',
        S['caption']))

    # ------------------------------------------------------------------ #
    # Section 2: The Opioid Crisis                                         #
    # ------------------------------------------------------------------ #
    story.append(SP(22))
    story.append(P('The Opioid Crisis \u2014 A Pharmaceutical Cascade', S['section']))
    story.append(SP(14))

    story.append(P(
        'December 12, 1995. The US Food and Drug Administration approves OxyContin \u2014 a '
        'controlled-release formulation of the opioid oxycodone, manufactured by Purdue '
        'Pharma, a privately held company owned by the Sackler family. The drug was '
        'approved to solve a genuine problem. Chronic pain was massively undertreated in '
        'the United States. Millions of Americans with chronic non-cancer pain were '
        'receiving inadequate analgesia, in part because physicians were reluctant to '
        'prescribe opioids for non-terminal conditions out of concern for addiction and '
        'regulatory scrutiny. In 1996 the American Pain Society introduced the idea of '
        'pain as "the fifth vital sign" \u2014 to be assessed and documented as routinely as '
        'blood pressure and temperature. The Joint Commission began rating hospitals on '
        'pain management. A cultural shift was under way. Undertreated pain was being '
        'redefined as a public health crisis requiring aggressive pharmaceutical '
        'intervention. Into that opening, OxyContin was launched.',
        S['body0']))
    story.append(SP(14))

    story.append(P(
        'Purdue\'s marketing campaign was on a scale and of a sophistication that '
        'pharmaceutical promotion had never seen. The company built a network of 671 '
        'paid speakers \u2014 physicians giving talks to other physicians at dinners, '
        'conferences, and "pain management education" weekends at resorts \u2014 to promote '
        'the drug\'s safety and efficacy for non-cancer chronic pain. Sales reps were '
        'trained to minimise addiction risk by citing a single document: a 1980 letter '
        'to the editor in the <i>New England Journal of Medicine</i>, by Porter and Jick, '
        'reporting low addiction rates among hospitalised patients receiving opioids for '
        '<i>acute</i> pain. The letter ran to five sentences. It had never been intended '
        'as a clinical study of addiction in chronic-pain patients. It was a brief '
        'observation about short-term hospital use. Between 1980 and 2017 it was cited '
        'over 600 times in the medical literature, almost always as evidence that '
        'opioids were minimally addictive in chronic-pain populations \u2014 populations the '
        'original observation had not studied and could not speak to. A five-sentence '
        'letter, cited out of context and amplified through 671 paid speakers, helped '
        'rewrite the prescribing practices of an entire country.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The geographic targeting of OxyContin marketing was precise and devastating. '
        'Purdue sales representatives concentrated their efforts in communities with '
        'high rates of physical labor employment \u2014 coal mining communities in '
        'Appalachia, timber communities in the Pacific Northwest, agricultural communities '
        'in the rural Midwest \u2014 where chronic musculoskeletal pain was common and '
        'healthcare options were limited. Some counties in Appalachia were prescribed '
        'opioids at rates ten times the national average. Prescription opioid dispensing '
        'in the United States grew from 76 million prescriptions in 1991 to 219 million '
        'in 2011, a three-fold increase in twenty years. The Drug Enforcement Administration, '
        'which sets annual production quotas for controlled substances, consistently raised '
        'oxycodone production quotas throughout this period \u2014 increasing from '
        '3.5 million grams in 1993 to 105 million grams in 2015, a thirty-fold increase. '
        'The regulatory apparatus that was supposed to prevent diversion of controlled '
        'substances was systematically calibrated to enable it.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The addiction cascade unfolded with the mechanical inevitability of a biological '
        'process, because it was a biological process. Physical dependence on opioids '
        'develops within weeks of regular use; the brain\'s endogenous opioid system '
        'downregulates in response to exogenous opioid supply, creating a physiological '
        'requirement for the drug to maintain normal function. When the FDA required Purdue '
        'to reformulate OxyContin in 2010 \u2014 adding a polyethylene oxide matrix that '
        'made the tablets difficult to crush or dissolve \u2014 the reformulation was '
        'intended to prevent abuse by eliminating the ability to deliver the full dose '
        'immediately. It succeeded in this narrow objective. The cascade it generated was '
        'that the several million Americans already addicted to OxyContin, suddenly unable '
        'to access their drug of dependency, turned to heroin: cheaper, more readily '
        'available, and producing the same opioid effect. Heroin overdose deaths, which '
        'had been declining for years, doubled between 2010 and 2012. The solution to the '
        'abuse of OxyContin had created a bridge to the street heroin market.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The fentanyl cascade followed from the heroin cascade with the same logic. '
        'Fentanyl is a synthetic opioid 50 to 100 times more potent than morphine and '
        '50 times more potent than heroin. A lethal dose is measured in micrograms \u2014 '
        'the size of a few grains of salt. This extreme potency makes fentanyl vastly '
        'easier to smuggle than bulkier opioids: a kilogram of fentanyl has the same '
        'effect as 50 kilograms of heroin. Drug enforcement interdiction \u2014 seizing '
        'shipments, disrupting supply chains \u2014 creates a powerful evolutionary '
        'selection pressure toward more potent, more easily concealed drugs. Fentanyl '
        'began appearing in the illicit opioid supply around 2013. By 2016, it accounted '
        'for the majority of opioid overdose deaths. Carfentanil \u2014 100 times more '
        'potent than fentanyl, 10,000 times more potent than morphine, developed as a '
        'large-animal veterinary tranquilizer \u2014 began appearing in 2016. Each '
        'enforcement intervention had selected for a more dangerous drug, in a cascade '
        'that had its own internal accelerating logic.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The mortality statistics are almost incomprehensible at human scale. From 1999 '
        'to 2023, more than 500,000 Americans died of opioid overdoses \u2014 more than '
        'the entire US military death toll in the Second World War, Korea, Vietnam, Iraq, '
        'and Afghanistan combined. In 2023 alone, approximately 80,000 Americans died '
        'of opioid overdoses, a figure greater than the total US military deaths in the '
        'entire Vietnam War. Life expectancy in the United States declined for three '
        'consecutive years \u2014 2015, 2016, and 2017 \u2014 a phenomenon without '
        'precedent in a developed country during peacetime, driven primarily by the opioid '
        'crisis. Total opioid litigation settlements have exceeded $50 billion, including '
        '$4.5 billion from members of the Sackler family personally. Purdue Pharma filed '
        'for bankruptcy in 2019. None of the settlements have reversed the cascade; '
        'opioid overdose deaths in 2023 remained at approximately 80,000, as fentanyl '
        'and its analogues have become embedded in the illicit drug supply in ways that '
        'are structurally disconnected from the pharmaceutical prescribing cascade '
        'that initiated the crisis.',
        S['body']))
    story.append(SP(14))

    story.append(fig_opioid_deaths())
    story.append(SP(8))
    story.append(P(
        'Figure 7.2: US opioid overdose deaths, 1999\u20132023. OxyContin\'s 1995 approval '
        'initiated a cascade from prescription opioids to heroin to fentanyl. The 2010 '
        'reformulation \u2014 intended to reduce abuse \u2014 accelerated the transition '
        'to heroin and fentanyl, generating the steepest portion of the mortality curve.',
        S['caption']))

    # ------------------------------------------------------------------ #
    # Section 3: Thalidomide                                               #
    # ------------------------------------------------------------------ #
    story.append(SP(22))
    story.append(P('Thalidomide \u2014 The Drug That Keeps Cascading', S['section']))
    story.append(SP(14))

    story.append(P(
        '1957. The West German pharmaceutical company Chemie Gr\u00fcnenthal introduces '
        'thalidomide under the brand name Contergan. It is marketed as a sedative and '
        'an antiemetic \u2014 a drug for anxiety, insomnia, and nausea \u2014 and described by '
        'the company as "completely safe" and "non-toxic," even for long-term use. It '
        'is sold without prescription across forty-six countries in Europe, Africa, '
        'Asia, and South America. It is marketed aggressively for morning sickness in '
        'pregnant women, a population for whom it works reliably on a genuinely '
        'miserable symptom that affects millions of women in the first trimester. In '
        'the United States, it does not get approved. An FDA medical officer named '
        'Frances Oldham Kelsey withholds her signature on the grounds that the data '
        'submitted by the American licensee, Richardson-Merrell, are inadequate and '
        'that the drug\'s safety in pregnancy has not been shown. She holds her line '
        'for over a year, under intense commercial pressure, and the President of the '
        'United States hands her an award for it in 1962. Her refusal is one of the '
        'most celebrated acts of bureaucratic courage in the history of medicine. The '
        'rest of the world does not have a Frances Kelsey.',
        S['body0']))
    story.append(SP(14))

    story.append(P(
        'The cascade from thalidomide was the worst drug-induced disaster in medical '
        'history up to that point. Thalidomide passes easily through the placental barrier '
        'and is a powerful teratogen: taken between the twenty-fourth and sixty-fourth '
        'day of pregnancy \u2014 exactly the window when morning sickness is worst and '
        'when many women do not yet know they are pregnant \u2014 it disrupts the '
        'development of fetal limbs, ears, eyes, and internal organs with near-certain '
        'effect. The characteristic damage is phocomelia: severely shortened or absent '
        'limbs, producing children whose hands and feet attach near the shoulders and '
        'hips. Approximately 10,000 children were born worldwide with severe thalidomide-'
        'induced abnormalities; some estimates place the total at closer to 20,000 when '
        'stillbirths and deaths in the first year of life are included. In West Germany '
        'alone, approximately 2,000 affected children survived to adulthood. The drug '
        'was withdrawn in November 1961 after the Australian obstetrician William McBride '
        'and the German paediatrician Widukind Lenz independently identified the link '
        'between thalidomide and birth defects in the same month. Gr\u00fcnenthal had '
        'received reports of peripheral neuropathy from physicians as early as 1959 and '
        'had not withdrawn the drug.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The regulatory cascade from thalidomide transformed global drug approval '
        'systems. In the United States, the Kefauver-Harris Drug Amendments of 1962 '
        'required for the first time that pharmaceutical companies demonstrate not only '
        'safety but efficacy before receiving FDA approval \u2014 a requirement that did '
        'not previously exist. Clinical trials became mandatory. The FDA was given expanded '
        'authority to demand pre-market testing and post-market surveillance. Similar '
        'reforms swept through European regulatory agencies. The thalidomide cascade '
        'directly created the modern clinical trial infrastructure that governs all drug '
        'development today: the randomised controlled trial, the ethics committee, the '
        'informed consent requirement, the post-market adverse event reporting system. '
        'Every drug approved since 1962 has been tested within a framework created by '
        'the thalidomide disaster. The cascade generated a regulatory system of genuine '
        'and lasting value \u2014 but only after it killed and damaged tens of thousands.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'Thalidomide\'s cascade has a second, stranger phase that no one could have '
        'predicted. In 1964, Israeli physician Jacob Sheskin found that thalidomide, '
        'administered as a sedative to a leprosy patient in severe pain, dramatically '
        'resolved the patient\'s erythema nodosum leprosum \u2014 a painful and '
        'potentially fatal inflammatory complication of leprosy. Further research '
        'established that thalidomide had potent anti-inflammatory and immunomodulatory '
        'properties, and in 1998 the FDA approved it for treatment of ENL in leprosy '
        'patients. More significantly, thalidomide was found to be highly effective '
        'against multiple myeloma, a cancer of plasma cells in the bone marrow that '
        'had been essentially untreatable in advanced stages. The STEPS programme '
        '(System for Thalidomide Education and Prescribing Safety) was developed to '
        'enable thalidomide prescribing while preventing fetal exposure: mandatory '
        'pregnancy testing, mandatory contraception, mandatory patient registration, '
        'and monthly monitoring. Thalidomide\'s more potent analogues \u2014 lenalidomide '
        '(Revlimid, approved 2006) and pomalidomide (Pomalyst, approved 2013) \u2014 are '
        'now among the most important treatments for multiple myeloma and certain other '
        'haematological malignancies. The drug responsible for the worst pharmaceutical '
        'disaster of the twentieth century is now saving thousands of lives annually. '
        'The cascade has not ended; it has transformed.',
        S['body']))

    # ------------------------------------------------------------------ #
    # Section 4: CRISPR                                                    #
    # ------------------------------------------------------------------ #
    story.append(SP(22))
    story.append(P('CRISPR and the Gene Editing Cascade', S['section']))
    story.append(SP(14))

    story.append(P(
        'August 2012. Jennifer Doudna of UC Berkeley and Emmanuelle Charpentier of '
        'the Helmholtz Centre for Infection Research publish a paper in <i>Science</i> '
        'describing a molecular system \u2014 CRISPR-Cas9 \u2014 that can be programmed to cut '
        'DNA at any specific location in any genome with unprecedented precision and '
        'simplicity. The system was borrowed from biology. Bacteria use CRISPR '
        'sequences as a kind of genetic memory of past viral infections, storing '
        'fragments of viral DNA so that Cas9 enzymes can recognise and cut those '
        'sequences if the virus attacks again. Doudna and Charpentier showed that the '
        'targeting could be redirected by simply changing a short "guide RNA" sequence '
        '\u2014 a process that takes days rather than the months earlier gene-editing '
        'techniques required. The biomedical community immediately recognised that '
        'this technology had the potential to correct the genetic mutations responsible '
        'for thousands of hereditary diseases: cystic fibrosis, sickle cell, '
        'Huntington\'s, Duchenne muscular dystrophy. Doudna and Charpentier won the '
        'Nobel in Chemistry in 2020. By that point, the cascade had already begun.',
        S['body0']))
    story.append(SP(14))

    story.append(P(
        'The precision of CRISPR-Cas9 is real but fundamentally incomplete in ways that '
        'create a cascade of their own. The Cas9 enzyme is directed to a specific DNA '
        'sequence by the guide RNA, but it will also cut sequences elsewhere in the '
        'genome that closely resemble the target sequence \u2014 "off-target" edits that '
        'the researcher did not intend. The human genome contains 3.2 billion base pairs, '
        'and similar sequences appear at thousands of locations throughout this enormous '
        'text. Off-target editing rates in human cells vary by experimental design and '
        'target sequence, but studies have consistently found unintended cuts at rates '
        'between 0.1 and 1 percent of the intended edit rate \u2014 which, in a genome '
        'of 3.2 billion base pairs, means potentially thousands of unintended genomic '
        'alterations per edited cell. These off-target edits can disrupt gene function '
        'in any of several hundred known oncogenes or tumour suppressor genes, potentially '
        'initiating a carcinogenic cascade years or decades after treatment. In a patient '
        'treated with CRISPR to correct a single-gene disease, the edited cells may '
        'number in the billions, and the long-term genomic consequences of those edits '
        'will unfold over a lifetime.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'Mosaicism creates a second category of cascade. When CRISPR is used to edit '
        'a fertilized egg or early embryo, the editing does not necessarily reach all '
        'cells: some cells receive the intended edit, some receive an off-target edit, '
        'and some receive no edit at all, producing a "mosaic" individual with a genetic '
        'patchwork that is impossible to characterize fully. The individual appears '
        'clinically normal but carries an unknown mix of edited and unedited cell '
        'lineages throughout their body. If the edited cells include germ cells \u2014 '
        'the cells that produce eggs or sperm \u2014 the genetic alterations, both '
        'intended and unintended, will be transmitted to any children the individual '
        'conceives. The cascade from a single CRISPR edit in an embryo can therefore '
        'propagate not only through an individual\'s body but through their descendants '
        'across generations, in ways that cannot be predicted or recalled once the edit '
        'has been made.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'In November 2018, the Chinese scientist He Jiankui announced at the Second '
        'International Summit on Human Genome Editing in Hong Kong that he had used '
        'CRISPR to edit the germline DNA of human embryos that had been implanted and '
        'carried to term \u2014 resulting in the birth of twin girls, whom he called '
        'Lulu and Nana, with edits to the CCR5 gene. He\'s stated rationale was that '
        'disabling CCR5 \u2014 which encodes a co-receptor that HIV uses to enter '
        'cells \u2014 would make the children resistant to HIV infection. The scientific '
        'community\'s reaction was nearly universal condemnation. CCR5 is a pleiotropic '
        'gene: it is involved not only in HIV entry but in immune function, '
        'neurological recovery from stroke and traumatic brain injury, and resistance to '
        'West Nile virus and influenza. The full consequences of eliminating CCR5 '
        'function in a developing human are unknown. He had also performed the edits '
        'without adequate informed consent, without proper ethics review, and without '
        'the oversight mechanisms that germline editing of this kind requires. He Jiankui '
        'was sentenced to three years in prison and fined three million yuan by a Chinese '
        'court in December 2019. The twins exist. Their genomic cascade is unfolding.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The social cascade from CRISPR follows the technical cascade with its own '
        'accelerating logic. The technical possibility of correcting genetic disease '
        'generates pressure to deploy it; deployment generates familiarity; familiarity '
        'generates extension to less severe conditions; extension generates the question '
        'of enhancement rather than treatment; enhancement generates equity concerns '
        'about who can access genetic advantage; equity concerns generate the spectre '
        'of genetic stratification between those who can afford to give their children '
        'optimized genomes and those who cannot. This cascade from therapeutic CRISPR '
        'to designer babies to genetic inequality does not require bad actors at any '
        'step; it follows from the ordinary logic of technological adoption, market '
        'incentives, and parental desire. The first therapeutic CRISPR treatment '
        '\u2014 exa-cel (Casgevy), for sickle cell disease and beta-thalassaemia \u2014 '
        'was approved by the FDA in December 2023, at a price of $2.2 million per '
        'patient. The cascade has taken its next step.',
        S['body']))
    story.append(SP(14))

    story.append(fig_crispr_cascade())
    story.append(SP(8))
    story.append(P(
        'Figure 7.3: The CRISPR cascade. Each branch of the intended benefit \u2014 curing '
        'genetic disease \u2014 generates a second-order risk, and each second-order risk '
        'generates a third-order consequence. The cascade is not hypothetical; each node '
        'shown has been documented in clinical or experimental settings.',
        S['caption']))

    # extension sections cut in v63 trim
    story.append(PageBreak())
    return story


def chapter8(S):
    story = []
    story += chapter_opener('Chapter Eight',
        'Politics \u2014 The Policy Boomerang',
        'Why government solutions so often return to strike the governments that launched them', S)
    story += epigraph(
        'The nine most terrifying words in the English language are: '
        '"I\'m from the government and I\'m here to help."',
        'Ronald Reagan \u2014 himself a cascade generator', S)
    story += [SP(12)]
    story.append(Mark(chapter='Politics \u2014 The Policy Boomerang'))

    # ------------------------------------------------------------------ #
    # Section 1: Prohibition                                               #
    # ------------------------------------------------------------------ #
    story.append(SP(22))
    story.append(P('Prohibition \u2014 The American Cautionary Tale', S['section']))
    story.append(SP(14))

    story.append(P(
        'American Prohibition was not the work of cranks. The temperance movement was '
        'serious, sustained, and evidence-based \u2014 a campaign against a real social '
        'problem. The Woman\'s Christian Temperance Union, founded in Cleveland in 1874, '
        'documented in exhaustive detail the role of alcohol in domestic violence, '
        'poverty, and industrial accidents in a society where adult male drinking was '
        'heavy, public, and culturally normalised. The Anti-Saloon League, founded in '
        '1893, became one of the most effective political lobbying organisations in '
        'American history, systematically electing dry legislators at the state and '
        'federal level for three decades. By 1916, twenty-three states had already '
        'enacted some form of prohibition. On January 16, 1919, the Eighteenth Amendment '
        'banning <i>the manufacture, sale, or transportation of intoxicating liquors</i> '
        'was ratified. The Volstead Act implementing it took effect a year later. This '
        'was not the act of fanatics. It was the considered judgment of a democratic '
        'supermajority that alcohol was doing more harm than its benefits justified. '
        'Most of what they said was true. What they did about it was a catastrophe.',
        S['body0']))
    story.append(SP(14))

    story.append(P(
        'The first-order cascade was the instantaneous creation of organised crime on '
        'an industrial scale. Before Prohibition, American criminal enterprises were '
        'local, small, and structurally disorganised. The moment Prohibition created a '
        'nationwide market for an illegal commodity \u2014 alcohol \u2014 with mass consumer '
        'demand, enormous profit margins, and no legal competition, the economic '
        'preconditions for criminal organisations of unprecedented scale were in place. '
        'Al Capone\'s Chicago Outfit, at its peak in 1927, ran on roughly six hundred '
        'employees \u2014 including politicians, police officers, and judges on the payroll \u2014 '
        'and grossed an estimated $60 million a year, roughly $1 billion in today\'s '
        'money, with beer and spirits the bulk of it. The structures Prohibition forced '
        'these organisations to build \u2014 interstate distribution networks, wholesale '
        'corruption of law enforcement, money-laundering operations, vertically '
        'integrated supply chains from still to retail \u2014 were not dissolved when '
        'Prohibition ended in 1933. They were redirected. The architecture is what '
        'mattered, and the architecture survived.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The violence cascade was documented in real time. The homicide rate in the '
        'United States stood at 6.8 per 100,000 population in 1920, the year Prohibition '
        'began. It rose steadily through the Prohibition years, reaching 9.7 per 100,000 '
        'in 1933, the year Prohibition ended \u2014 a 43 percent increase over thirteen '
        'years. The Chicago gang wars of 1927 to 1930 produced over 500 murders, including '
        'the St. Valentine\'s Day Massacre of February 14, 1929, in which seven members '
        'of a rival gang were executed by Capone\'s men. The violence was not incidental '
        'to Prohibition; it was structural. Alcohol was a commodity that could not be '
        'protected by contract law, trademark law, or property rights. The only mechanism '
        'for enforcing market boundaries and protecting distribution territories was '
        'physical force. The solution to the alcohol problem had created a market '
        'structure in which violence was the rational tool of commerce.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The public health cascade was perverse in the specific way that prohibition '
        'cascades tend to be: the intervention harmed most severely the population it '
        'was most trying to help. Before Prohibition, 15,000 licensed saloons operated '
        'in New York City alone. By 1927, an estimated 30,000 illegal speakeasies had '
        'replaced them. Alcohol consumption among moderate drinkers \u2014 those for '
        'whom the price increase and social stigma of illegal purchasing were meaningful '
        'deterrents \u2014 declined. Alcohol consumption among heavy, chronic drinkers '
        '\u2014 those whose dependency made them willing to pay premium prices and take '
        'legal risks \u2014 proved far more elastic. The group least affected by '
        'Prohibition was the group most targeted by the reformers. Meanwhile, the '
        'prohibition of legal alcohol created a market for dangerously adulterated '
        'bootleg spirits. The federal government, in a catastrophic secondary cascade, '
        'deliberately denatured industrial alcohol with methanol, kerosene, benzene, '
        'and other poisons to prevent its use as beverage alcohol \u2014 a policy '
        'that killed an estimated 10,000 people between 1926 and 1933. The government\'s '
        'solution to bootleggers using industrial alcohol produced a government policy '
        'of poisoning citizens.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The corruption cascade transformed American institutions in ways that outlasted '
        'Prohibition by decades. Systematic bribery of police, prosecutors, judges, and '
        'politicians was not an aberration during Prohibition; it was the operational '
        'foundation of the bootlegging industry. A 1926 investigation found that '
        'approximately half of Chicago\'s police force had accepted payments from '
        'bootleggers. The corruption model \u2014 identifying the price at which law '
        'enforcement could be purchased and building it into operating costs \u2014 '
        'was institutionalised during Prohibition and survived repeal intact, transferred '
        'to the narcotics, gambling, and extortion operations that Prohibition-era '
        'criminal organisations pivoted to after 1933. The Prohibition cascade created '
        'the institutional and financial architecture of organised crime in America; the '
        'subsequent history of American organised crime is largely a history of that '
        'architecture being applied to successive markets.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The cultural cascade was equally consequential and entirely unanticipated. '
        'Prohibition generated the Roaring Twenties as a counter-cultural reaction. '
        'Jazz clubs, which served as speakeasies, became the crucibles of American '
        'popular music. Cocktail culture \u2014 the mixing of spirits with other '
        'ingredients to mask the taste of poorly distilled bootleg alcohol \u2014 was '
        'invented during Prohibition and persists today. The social ritual of mixed-sex '
        'drinking, previously confined to a narrow upper-class milieu, became '
        'democratised in the speakeasy culture that Prohibition created. Women, '
        'barred from the masculine saloon culture that the temperance movement had '
        'targeted, entered the speakeasy as social equals and drank publicly in mixed '
        'company for the first time. The solution to the alcohol problem created the '
        'social infrastructure for a drinking culture far more pervasive and socially '
        'integrated than the one it had displaced.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The Twenty-First Amendment, ratified on December 5, 1933, repealed the '
        'Eighteenth Amendment \u2014 the only time in American history that a '
        'constitutional amendment has been repealed by another. The repeal solved '
        'some of Prohibition\'s cascade effects (bootlegging, government poisoning) '
        'and entrenched others. The organised crime families established during '
        'Prohibition \u2014 the Genovese, Gambino, Lucchese, Bonanno, and Colombo '
        'families in New York; the Outfit in Chicago \u2014 survived repeal by '
        'diversifying into heroin importation, gambling, and union corruption. The '
        'heroin epidemic of the 1960s and 1970s that contributed to the Nixon '
        'administration\'s declaration of a War on Drugs was supplied in significant '
        'part through distribution networks whose infrastructure had been built during '
        'Prohibition. The cascade from the solution to the problem of alcohol ran '
        'continuously from 1920 to the present day, through organised crime, through '
        'the heroin epidemic, through the War on Drugs, to the fentanyl crisis of '
        'the twenty-first century.',
        S['body']))
    story.append(SP(14))

    story.append(fig_prohibition_homicide())
    story.append(SP(8))
    story.append(P(
        'Figure 8.1: US homicide rates during Prohibition, 1910\u20131941. The homicide '
        'rate rose 43 percent during the Prohibition years (shaded) and fell after repeal. '
        'The solution to alcohol\'s social harms directly caused a cascade of violence '
        'not present in the problem it was solving.',
        S['caption']))

    # ------------------------------------------------------------------ #
    # Section 2: War on Drugs                                              #
    # ------------------------------------------------------------------ #
    story.append(SP(22))
    story.append(P('The War on Drugs \u2014 Policy in a Feedback Loop', S['section']))
    story.append(SP(14))

    story.append(P(
        'June 17, 1971. President Richard Nixon stands before reporters at the White '
        'House and declares drug abuse "public enemy number one in the United States." '
        'He announces a total offensive against it: more federal drug-control agencies, '
        'mandatory-sentencing proposals, expanded no-knock warrant authority. The '
        'context was real. Heroin addiction among returning Vietnam veterans was a '
        'visible public-health crisis. LSD and marijuana had become symbols of a '
        'counterculture the administration found politically threatening. Urban crime, '
        'associated in the public mind with drug use, was rising. The theory underlying '
        'the policy was coherent on paper. Suppress supply through enforcement; prices '
        'rise; access becomes difficult; demand falls. It was a supply-chain disruption '
        'theory applied to an inelastic good, designed by people who had not yet '
        'understood why supply-chain disruption does not work on drugs. It was, in the '
        'language of this book, a Type-II cascade in the making \u2014 the moment a policy '
        'announcement creates the architecture of the catastrophe that will follow.',
        S['body0']))
    story.append(SP(14))

    story.append(P(
        'In 2016, John Ehrlichman, Nixon\'s domestic policy advisor, gave an interview '
        'to journalist Dan Baum of Harper\'s Magazine that provided the most explicit '
        'documentation of the political motivation behind the War on Drugs. Ehrlichman '
        'stated: "The Nixon campaign in 1968, and the Nixon White House after that, had '
        'two enemies: the antiwar left and Black people. We knew we couldn\'t make it '
        'illegal to be either against the war or Black, but by getting the public to '
        'associate the hippies with marijuana and Blacks with heroin, and then '
        'criminalizing both heavily, we could disrupt those communities. We could '
        'arrest their leaders, raid their homes, break up their meetings, and vilify '
        'them night after night on the evening news." The War on Drugs was not conceived '
        'primarily as a public health policy; it was conceived as a political strategy '
        'that happened to use drug enforcement as its instrument. This political origin '
        'explains features of the policy that its public-health rationale cannot: the '
        'dramatic racial disparity in enforcement, the emphasis on incarceration over '
        'treatment, and the consistent prioritisation of enforcement metrics over '
        'outcomes metrics.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The scale of spending on the War on Drugs defies easy comprehension. Federal '
        'expenditure on drug control has exceeded $1 trillion since 1971, according to '
        'analysis by the Drug Policy Alliance, with an additional estimated $1 trillion '
        'in state and local spending. Annual federal drug control spending grew from '
        '$100 million in 1971 to $35 billion in 2023. The policy tools deployed include '
        'the Controlled Substances Act (1970), mandatory minimum sentencing laws (1986), '
        'the Anti-Drug Abuse Act (1988) with its 100:1 sentencing disparity between '
        'crack and powder cocaine, the DARE programme (introduced 1983, evaluated as '
        'ineffective by the US Government Accountability Office in 2003 yet still '
        'operating in schools), asset forfeiture laws, Plan Colombia ($10 billion '
        'between 1999 and 2016), and the Merida Initiative in Mexico. The policy '
        'infrastructure has been elaborate, expensive, and sustained across nine '
        'presidential administrations of both parties.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The primary metric \u2014 drug use rates \u2014 has not responded to fifty years '
        'of interventions. The National Survey on Drug Use and Health, which has tracked '
        'drug use continuously since 1979, shows no sustained decline in overall '
        'illicit drug use attributable to enforcement. The price of cocaine, adjusted '
        'for inflation and purity, fell by approximately 80 percent between 1982 and '
        '2012 despite enormous interdiction efforts \u2014 the opposite of what supply-'
        'side theory predicts. Drug use rates in the United States are among the highest '
        'in the developed world despite the most expensive drug enforcement programme '
        'in history, while Portugal \u2014 which decriminalised possession of all drugs '
        'in 2001 and redirected resources from enforcement to treatment \u2014 saw '
        'drug-induced deaths fall from 80 per million in 2001 to 3 per million in 2017, '
        'an 85 percent reduction, and HIV infections among drug users fall by 95 percent. '
        'The evidence from the comparative experiment run across different countries '
        'is unambiguous: the War on Drugs does not achieve its stated objectives and '
        'decriminalisation with treatment investment achieves them far better.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The incarceration cascade is the War on Drugs\' most thoroughly documented '
        'consequence. The US prison population stood at approximately 300,000 in 1972, '
        'the year after the War on Drugs was declared. By 2008, it had grown to 2.3 '
        'million \u2014 a 7.5-fold increase in thirty-six years, making the United '
        'States the world\'s largest incarcerating nation both in absolute terms and per '
        'capita. Drug offences account for approximately 45 percent of federal prisoners. '
        'The annual cost of mass incarceration exceeds $80 billion at the federal and '
        'state level. Black Americans, who constitute 13 percent of the US population '
        'and use drugs at approximately the same rates as white Americans, account for '
        '37 percent of drug arrests and 56 percent of drug incarcerations \u2014 a '
        'racial disparity that has been consistently documented across fifty years of '
        'enforcement data and cannot be explained by differential drug use rates. The '
        'cascade from racially disparate incarceration includes disrupted families, '
        'reduced employment prospects, disenfranchisement from political participation, '
        'concentrated neighborhood disadvantage, and the criminogenic conditions that '
        'increase future offending \u2014 each of which generates more enforcement, '
        'which generates more incarceration, in a reinforcing loop that the policy '
        'architects of 1971 could not have modelled and that fifty years of subsequent '
        'policy has not broken.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The interdiction cascade illustrates the specific mechanism by which enforcement '
        'generates the next crisis. Plan Colombia, a $10 billion US-funded programme '
        'launched in 1999 to suppress Colombian cocaine production through aerial '
        'herbicide spraying, military interdiction, and counter-narcotics operations, '
        'succeeded in weakening the Colombian cartels \u2014 the Cali and Medell\u00edn '
        'organisations that had dominated cocaine production since the 1970s. The '
        'supply gap created by their disruption was filled by Mexican cartels, which '
        'had previously served primarily as transportation intermediaries. The Sinaloa '
        'Cartel, the Jalisco New Generation Cartel, and their competitors grew to '
        'control not only cocaine distribution but heroin, methamphetamine, and '
        'fentanyl production. The Mexican drug war that erupted from this reorganisation '
        'has killed over 200,000 people since 2006. The cartels are now larger, more '
        'violent, more sophisticated, and more deeply embedded in Mexican state '
        'institutions than the Colombian cartels they replaced. The solution to the '
        'Colombian cartel problem created a Mexican cartel problem of greater scale '
        'and greater lethality.',
        S['body']))
    story.append(SP(14))

    story.append(fig_war_on_drugs_incarceration())
    story.append(SP(8))
    story.append(P(
        'Figure 8.2: US prison population 1972\u20132023. The 7.5-fold increase following '
        'the 1971 War on Drugs declaration has produced the world\'s largest prison '
        'population without reducing drug use rates. The slight decline since 2008 '
        'reflects sentencing reforms at the state level, not any reduction in the '
        'enforcement infrastructure.',
        S['caption']))
    story.append(SP(10))
    story.append(fig_drug_policy_comparison())
    story.append(SP(8))
    story.append(P(
        'Figure 8.3: Drug policy outcomes: drug-induced deaths per million population, 2022. '
        'USA: CDC WONDER total drug overdose deaths (~240/million using EMCDDA-comparable ICD coding). '
        'EU countries: EMCDDA 2022 European Drug Report. The United States records drug-induced '
        'deaths approximately 80 times higher than Portugal, which decriminalised all drug possession '
        'in 2001 and redirected enforcement resources to treatment. Sweden\'s strict enforcement '
        'approach produces 20 times Portugal\'s rate. The comparative evidence constitutes the '
        'strongest natural experiment in drug policy.',
        S['caption']))

    # ------------------------------------------------------------------ #
    # Section 4: GDPR                                                      #
    # ------------------------------------------------------------------ #
    story.append(SP(22))
    story.append(P('GDPR and the Regulatory Cascade', S['section']))
    story.append(SP(14))

    story.append(P(
        'The General Data Protection Regulation, which came into force across the '
        'European Union on May 25, 2018, was the most ambitious privacy law ever enacted. '
        'Its context was the Cambridge Analytica scandal, in which data harvested from '
        '87 million Facebook profiles without meaningful consent had been used to build '
        'psychographic profiles of American and British voters and deliver micro-targeted '
        'political advertising in the 2016 US presidential election and the Brexit '
        'referendum. The underlying business model that enabled Cambridge Analytica \u2014 '
        'surveillance capitalism, in which technology platforms collect detailed personal '
        'data on billions of users and sell access to advertisers and political campaigns '
        '\u2014 had been operating at scale for a decade with minimal regulatory oversight. '
        'GDPR was a serious and sophisticated regulatory response: it gave individuals '
        'the right to access, correct, and delete their personal data; required explicit, '
        'informed consent for data processing; imposed fines of up to 4 percent of global '
        'annual revenue for violations; and created a comprehensive accountability '
        'framework for data controllers across the EU. The objective was clearly stated '
        'and genuinely important.',
        S['body0']))
    story.append(SP(14))

    story.append(P(
        'The most immediately visible cascade from GDPR was the proliferation of cookie '
        'consent banners. Every website that collects data from EU users \u2014 which '
        'includes virtually every commercial website in the world \u2014 is required to '
        'obtain consent before placing tracking cookies. The consent interface that '
        'emerged across the industry features a prominent "Accept All" button and a '
        'significantly less prominent "Manage Preferences" option requiring multiple '
        'additional clicks to exercise. The Nielsen Norman Group and multiple academic '
        'researchers have documented that approximately 95 percent of users click '
        '"Accept All" without reading or engaging with the consent options. The consent '
        'is formally obtained. The "informed" element of informed consent is not achieved. '
        'An entire industry \u2014 the consent management platform (CMP) market, '
        'comprising more than 1,000 registered vendors by 2023 (IAB Europe\'s '
        'Transparency and Consent Framework registry) \u2014 has been created to '
        'generate formally compliant consent that achieves the legal form of GDPR '
        'compliance while systematically undermining its substantive objective. This is Goodhart\'s Law '
        'operating at EU regulatory scale: the metric (consent obtained) is optimised '
        'in ways that divorce it entirely from the objective (meaningful user control).',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The compliance industrial complex generated by GDPR represents a transfer of '
        'resources from productive activity to regulatory overhead on an extraordinary '
        'scale. A 2019 survey of Fortune 500 companies found average GDPR compliance '
        'costs of $1.3 million for the initial implementation phase. By 2023, the global '
        'privacy compliance market was estimated at $8 billion annually, growing at '
        'over 20 percent per year, encompassing law firms, consultancies, software '
        'vendors, data protection officers (a new mandatory role under GDPR), and '
        'training companies. Small and medium-sized businesses, which cannot afford '
        'dedicated compliance departments, are proportionally far more burdened than '
        'large companies with legal teams already in place. The regulatory cascade has '
        'therefore had the paradoxical effect of improving the competitive position of '
        'Google, Facebook, and Amazon \u2014 the large technology companies that GDPR '
        'was partly designed to constrain \u2014 relative to the smaller competitors '
        'that might otherwise challenge them. The solution to surveillance capitalism '
        'has reinforced the market dominance of the largest surveillance capitalists.',
        S['body']))

    # extension sections cut in v63 trim — keep the page break so Ch9 starts fresh
    story.append(PageBreak())
    return story


def chapter9(S):
    story = []
    story += chapter_opener('Chapter Nine',
        'Social \u2014 Systems That Remember',
        'How social and ecological systems store and amplify the cascades we send into them', S)
    story += epigraph(
        'We do not inherit the earth from our ancestors; we borrow it from our children.',
        'Antoine de Saint-Exup\u00e9ry (often attributed; actual origin disputed)', S)
    story += [SP(12)]
    story.append(Mark(chapter='Social \u2014 Systems That Remember'))

    # ------------------------------------------------------------------ #
    # Section 1: Social Media                                              #
    # ------------------------------------------------------------------ #
    story.append(SP(22))
    story.append(P('Social Media \u2014 Connecting Humanity, Disconnecting Minds', S['section']))
    story.append(SP(14))

    story.append(P(
        'February 4, 2004. Mark Zuckerberg, a nineteen-year-old Harvard sophomore, '
        'launches thefacebook.com from his dormitory in Kirkland House. The original '
        'purpose was modest: let Harvard students see who was in their classes and '
        'their dormitories. A digital version of the paper "face books" the university '
        'used to hand to incoming students. Within twenty-four hours, twelve hundred '
        'Harvard students had signed up. Within a month, the site had spread to Yale, '
        'Columbia, and Stanford. In September 2006 it opened to anyone over thirteen '
        'with an email address. By 2012, it had a billion users. By 2024, 3.1 billion '
        'monthly active users \u2014 more than a third of the human species \u2014 making it '
        'the largest social network in the history of civilisation, by an enormous '
        'margin. The benefit was real. Families separated by migration stayed in '
        'daily contact. Political movements organised in hours rather than years. News '
        'reached ordinary people at unprecedented speed. The connection was authentic. '
        'The cascade it generated was equally authentic.',
        S['body0']))
    story.append(SP(14))

    story.append(P(
        'The Like button arrived on February 9, 2009. It is the single design decision '
        'most consequential for the cascade. Before the Like button, Facebook was a '
        'primarily connective platform \u2014 users posted, others responded with comments. '
        'The Like button added a number to every piece of content. A real-time, '
        'quantified, public score of social reception. For adolescent users, whose '
        'brains are developmentally tuned to social approval, the Like count became a '
        'proxy for social standing. For the platform, the Like button and the '
        'aggregated engagement data it generated became the raw material for the '
        'engagement-optimisation algorithms that defined the next decade. The algorithm '
        'had a single instruction: maximise time-on-platform. Operationalised, that '
        'meant maximise engagement signals. Facebook\'s own internal research found '
        'what any reader could guess from the outside \u2014 the content that most reliably '
        'maximises engagement is the content that provokes strong emotion: outrage, '
        'fear, disgust, tribal solidarity. The algorithm did not invent human '
        'tribalism. It discovered that human tribalism was the most reliable engagement '
        'driver, and optimised for it at the scale of billions of users.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The mental health cascade has been most precisely documented in the adolescent '
        'population. The US Centers for Disease Control\'s Youth Risk Behavior Survey, '
        'which has tracked adolescent health behaviours continuously since 1991, found '
        'that the proportion of teenage girls reporting persistent feelings of sadness '
        'or hopelessness stood at 36 percent in 2011 and had risen to 57 percent by '
        '2021 \u2014 a 21 percentage point increase in ten years. Among teenage boys, '
        'the increase was 21 to 29 percent over the same period. The inflection point '
        'in both trends falls between 2011 and 2013 \u2014 precisely when smartphone '
        'adoption reached majority penetration among American teenagers and when '
        'Instagram, with its emphasis on curated visual self-presentation and follower '
        'counts, emerged as the dominant platform for adolescent social life. '
        'Instagram\'s own internal research, leaked to the Wall Street Journal in '
        'September 2021, found that Instagram made body image issues worse for '
        'one in three teenage girls and that among teenagers who reported suicidal '
        'ideation, 13 percent in the United States traced the desire to Facebook '
        'and Instagram. The company had this research. It did not change the product.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The loneliness paradox \u2014 the finding that the most heavily connected '
        'generation in history reports the highest levels of loneliness \u2014 has been '
        'documented across multiple independent data sources. The Cigna Loneliness Index '
        'of 2020 found that 61 percent of Americans reported feeling lonely, with '
        'Generation Z (born 1997-2012, the generation that grew up with smartphones '
        'and social media from early adolescence) reporting the highest loneliness '
        'scores of any age group \u2014 higher than the elderly, who are typically '
        'assumed to be most vulnerable to social isolation. A 2017 study by Primack '
        'et al. in the American Journal of Preventive Medicine found that the highest '
        'quartile of social media use was associated with approximately twice the odds '
        'of perceived social isolation compared to the lowest quartile. The mechanism '
        'proposed by researchers is not that social media directly causes loneliness '
        'but that it displaces the activities most associated with genuine social '
        'connection \u2014 face-to-face interaction, shared physical activity, '
        'sustained conversation \u2014 while providing the sensation of social '
        'engagement through notifications, likes, and comments, creating a signal '
        'of social sufficiency that suppresses the motivation to seek the deeper '
        'connections that would actually alleviate loneliness.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The information cascade from social media has restructured the epistemological '
        'foundations of democratic politics. A 2018 study by Vosoughi, Roy, and Aral '
        'published in Science analysed 126,000 news stories shared on Twitter over '
        'twelve years and found that false news spread six times faster than true news, '
        'reached ten times as many people, and penetrated further into the network '
        'structure. The mechanism is the engagement algorithm: false news, which is '
        'typically more emotionally provocative, more novel, and more affirmatively '
        'validating of tribal beliefs than true news, generates more engagement signals '
        'and is therefore amplified more aggressively by algorithms optimised for '
        'engagement. The Pew Research Center has tracked partisan polarisation in '
        'American politics continuously since 1994: the proportion of Americans holding '
        '"very unfavorable" views of the opposing political party stood at 17 percent '
        'in 1994 and rose to 62 percent by 2022. The rise of extreme partisan hostility '
        'tracks social media adoption almost precisely, with the steepest increase '
        'occurring in the decade after 2010 when smartphone-mediated social media '
        'became the primary political information environment for most Americans.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The content moderation cascade illustrates how the solution to the harms '
        'of unmoderated social media generates its own cascade. Facebook employed '
        'approximately 15,000 content moderators worldwide by 2021, reviewing '
        'flagged content for violation of community standards. Researchers at the '
        'University of Haifa and Trauma Research UK found that content moderators '
        'develop PTSD at rates comparable to combat veterans and emergency service '
        'workers, with exposure to mass violence, child abuse, and extremist content '
        'producing clinically significant psychological damage in the majority of '
        'moderators after sustained exposure. The AI-based moderation systems deployed '
        'to supplement human moderators produce simultaneous over-moderation \u2014 '
        'removing legitimate political speech, news reporting, and artistic expression '
        '\u2014 and under-moderation \u2014 failing to detect harmful content that '
        'violates community standards at scale. Every expansion of moderation generates '
        'new disputes about censorship, new adversarial content designed to evade '
        'detection, and new questions about who decides what is acceptable discourse '
        'on a platform used by a third of the human population.',
        S['body']))
    story.append(SP(14))

    story.append(fig_social_media_mental_health())
    story.append(SP(8))
    story.append(P(
        'Figure 9.1: Social media adoption versus teen mental health, 2005\u20132021. '
        'The inflection in persistent sadness among teenage girls (solid line) '
        'corresponds almost exactly to the period of smartphone mass adoption and '
        'Instagram\'s emergence as the dominant adolescent social platform. '
        'Correlation does not establish causation, but the mechanisms are documented '
        'in the platform\'s own internal research.',
        S['caption']))

    # ------------------------------------------------------------------ #
    # Section 2: GPS                                                       #
    # ------------------------------------------------------------------ #
    story.append(SP(22))
    story.append(P('GPS \u2014 Navigating Away from Our Own Minds', S['section']))
    story.append(SP(14))

    story.append(P(
        'On May 1, 2000, President Bill Clinton signed an executive order removing '
        '"Selective Availability" from the civilian GPS signal \u2014 the intentional '
        'degradation of positioning accuracy that the US military had maintained since '
        'the system\'s civilian opening to prevent adversaries from using GPS-guided '
        'precision. The removal improved civilian GPS accuracy from approximately '
        '100 metres to within 10 metres, effectively transforming GPS from a rough '
        'navigation aid into a precision positioning system usable for turn-by-turn '
        'navigation, survey-grade mapping, precision agriculture, and autonomous '
        'vehicle guidance. The cascade of beneficial applications was immediate and '
        'enormous: logistics networks achieved new levels of precision, emergency '
        'services response times improved, aviation safety was enhanced, and a global '
        'industry of location-based services \u2014 from Google Maps to Uber to '
        'Deliveroo \u2014 was made possible. The benefit is real and quantifiable: '
        'GPS is estimated to contribute $68 billion annually to the US economy and '
        '$1.4 trillion globally. The cognitive cascade is slower, subtler, and '
        'not yet fully measured.',
        S['body0']))
    story.append(SP(14))

    story.append(P(
        'Eleanor Maguire and her colleagues at University College London published '
        'a landmark study in 2000 in the Proceedings of the National Academy of '
        'Sciences documenting that London taxi drivers \u2014 who acquire detailed '
        'spatial knowledge of London\'s 25,000 streets through "The Knowledge," '
        'a qualification process that typically requires three to four years of '
        'intensive study \u2014 have measurably larger posterior hippocampi than '
        'control subjects matched for age, education, and intelligence. The posterior '
        'hippocampus is the brain region most associated with spatial navigation and '
        'the formation of cognitive maps. The taxi drivers\' hippocampal enlargement '
        'correlated with years of experience \u2014 longer-serving drivers had '
        'larger posterior hippocampi. The implication was clear: the hippocampus '
        'is responsive to navigational demand, expanding with use and presumably '
        'shrinking with disuse. In 2011, Maguire\'s group found that London taxi '
        'drivers who had qualified before GPS navigation became widespread showed '
        'greater hippocampal volume than those who qualified after GPS adoption. '
        'The brain\'s navigational infrastructure is use-dependent. GPS removes '
        'the demand.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'Hugo Spiers\' research group at UCL, studying navigation in 24 global cities '
        'and published in Nature in 2017, found that GPS users show significantly '
        'reduced hippocampal activity during navigation compared to people navigating '
        'without GPS assistance. A 2020 study by Dahmani and Bohbot in Scientific '
        'Reports found that habitual GPS users performed significantly worse on '
        'spatial memory tasks than non-GPS users and showed reduced hippocampal '
        'grey matter volume. The hippocampus is not involved only in spatial '
        'navigation: it is the central hub for episodic memory formation, contextual '
        'learning, and what neuroscientists call "cognitive mapping" of abstract '
        'as well as physical space. Reduced hippocampal volume is associated with '
        'increased risk of Alzheimer\'s disease, depression, and post-traumatic '
        'stress disorder. Whether habitual GPS use causes hippocampal atrophy or '
        'whether people with smaller hippocampi are simply more likely to use GPS '
        'remains methodologically contested. The mechanistic plausibility is '
        'well-established; the causal direction in human populations requires '
        'longer follow-up than the technology has existed for.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'GPS navigation is the cobra effect for traffic. In 1968, the German '
        'mathematician Dietrich Braess proved a result that defies common sense: '
        'adding a road to a traffic network can, under quite ordinary conditions, '
        'make travel times <i>worse</i> for every driver on it. Each driver, choosing '
        'the route that is individually best, lands the whole system in a Nash '
        'equilibrium that is collectively worse than the equilibrium without the new '
        'road. This is Braess\'s Paradox. GPS navigation systems reproduce it at '
        'urban scale every day, by routing tens of thousands of drivers to the same '
        '"currently optimal" road at the same moment \u2014 at which point it is no '
        'longer optimal. The cascade leaks out of the main road and into the side '
        'streets. Waze has been documented sending thousands of drivers per hour '
        'through residential streets in Los Angeles, Montclair, and dozens of other '
        'municipalities, generating safety hazards and noise pollution in '
        'neighbourhoods whose residents had chosen them specifically for being quiet. '
        'The solution to navigation uncertainty turns out to be a traffic '
        'redistribution cascade that affects millions of households who do not even '
        'own a smartphone.',
        S['body']))
    story.append(SP(14))

    story.append(callout(
        '<b>The Braess Paradox:</b> Adding a road to a network \u2014 or a navigation shortcut to all drivers simultaneously '
        '\u2014 can slow everyone down. When GPS directs thousands of drivers to the same '
        '"optimal" route, it destroys the optimality that made the route attractive. '
        'Dietrich Braess first demonstrated this counterintuitive result mathematically in 1968; '
        'GPS systems produce it empirically every day.',
        S))
    story.append(SP(14))

    story.append(P(
        'The GPS overreliance cascade has produced documented safety failures of a '
        'specific character: drivers who follow GPS instructions into physically '
        'impossible or dangerous situations without exercising independent judgment. '
        'In 2009, three Japanese tourists followed GPS instructions onto a dirt track '
        'on the Hinchinbrook Island coast of Australia and drove into the Pacific Ocean '
        '\u2014 insisting to the GPS that they were "going to the island" as the tide '
        'rose around their vehicle. Similar incidents have been documented in Scotland, '
        'Wales, the United States, and Canada, in which drivers have followed GPS '
        'routing into rivers, off boat ramps, down pedestrian paths, and into '
        'structural collapses. These incidents are not failures of GPS technology; '
        'they are failures of the cognitive handoff between human judgment and '
        'technological guidance \u2014 a cascade in which the existence of the '
        'guidance system has eroded the capacity for independent judgment that would '
        'be needed to catch the guidance system\'s errors.',
        S['body']))

    # ------------------------------------------------------------------ #
    # Section 4: Green Revolution                                          #
    # ------------------------------------------------------------------ #
    story.append(SP(22))
    story.append(P('The Green Revolution \u2014 Feeding Billions, Depleting the Earth', S['section']))
    story.append(SP(14))

    story.append(P(
        'In the 1940s and 1950s, Norman Borlaug, an American plant pathologist working '
        'at a research station in Sonora, Mexico funded by the Rockefeller Foundation, '
        'developed a series of semi-dwarf, high-yield wheat varieties that would '
        'transform world food production. The conventional wheat varieties of the '
        'time grew tall, and when given high doses of nitrogen fertiliser to maximise '
        'yield, lodged \u2014 fell over under the weight of the grain, destroying '
        'the harvest. Borlaug\'s semi-dwarf varieties had shorter, stronger stems '
        'that could bear heavy grain heads without lodging, enabling farmers to apply '
        'large amounts of nitrogen fertiliser and achieve yields four to five times '
        'higher than traditional varieties. He introduced these varieties to India '
        'and Pakistan in 1965, at a moment when both countries faced the prospect '
        'of catastrophic famine: India\'s grain reserves had fallen to a two-week '
        'supply. Within five years, India\'s wheat production had doubled. Within '
        'ten years, India was a net exporter of grain. Pakistan achieved food '
        'self-sufficiency by the early 1970s. Borlaug was awarded the Nobel Peace '
        'Prize in 1970, and his citation credited him with saving one billion lives. '
        'The figure is impossible to verify precisely; the order of magnitude is not '
        'contested.',
        S['body0']))
    story.append(SP(14))

    story.append(P(
        'The scale of the achievement is genuinely staggering and must be understood '
        'before the cascade is examined. India\'s wheat production grew from 12 million '
        'tons in 1964 to 73 million tons in 2010 \u2014 a six-fold increase in '
        'forty-six years on approximately the same area of cultivated land. Global '
        'food production per capita increased continuously from 1961 to 2020 despite '
        'world population more than doubling, entirely overturning the Malthusian '
        'predictions of imminent famine that were the consensus of demographic '
        'scholarship in the 1960s. Paul Ehrlich\'s The Population Bomb (1968) predicted '
        'that "hundreds of millions of people will starve to death in spite of any '
        'crash programs embarked upon now" in the 1970s and 1980s. The prediction '
        'was wrong. The Green Revolution\'s cascade of benefits was real, was '
        'enormous, and is not diminished by examining the cascade of costs that '
        'accompanied and followed it.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The nitrogen cascade is the most extensively studied second-order consequence '
        'of Green Revolution agriculture. The high-yield varieties require substantial '
        'synthetic nitrogen fertiliser, produced through the Haber-Bosch process that '
        'Fritz Haber developed in 1909 \u2014 a process that has been described as '
        'the most consequential chemical invention in history, enabling the production '
        'of synthetic ammonia from atmospheric nitrogen and thereby making possible '
        'the feeding of approximately half the current human population. The cascade '
        'from synthetic nitrogen fertiliser is that a significant fraction \u2014 '
        'estimates range from 30 to 70 percent, depending on soil type, application '
        'method, and crop \u2014 runs off into waterways rather than being absorbed '
        'by crops. Nitrogen and phosphorus runoff from agricultural land creates '
        'algal blooms in coastal waters; the algae consume oxygen as they decompose, '
        'creating hypoxic zones where marine life cannot survive. The Gulf of Mexico '
        'dead zone, created by nitrogen runoff from the Mississippi River basin, '
        'covers approximately 6,500 square miles in peak summer conditions \u2014 '
        'larger than Connecticut. Over 400 coastal dead zones have been documented '
        'worldwide, all attributable to the agricultural nitrogen cascade.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The monoculture cascade concentrates risk in ways that traditional agricultural '
        'diversity distributed. The high-yield varieties of the Green Revolution are, '
        'by design, genetically uniform: the trait that makes them high-yielding is '
        'the same trait in every plant of that variety, and the genetic uniformity '
        'that enables consistent performance also means that a pathogen that can '
        'defeat one plant can defeat all of them simultaneously. In 1970, the Southern '
        'Corn Leaf Blight devastated the United States maize harvest: approximately '
        '15 percent of the entire US corn crop \u2014 worth $1 billion at 1970 prices '
        '\u2014 was destroyed in a single season because approximately 80 percent of '
        'US corn acreage had been planted with hybrids sharing a single genetic '
        'element (Texas cytoplasm male sterility) that gave the blight pathogen a '
        'uniformly vulnerable target. The Food and Agriculture Organisation estimates '
        'that 75 percent of the genetic diversity in crop plants has been lost since '
        '1900, as traditional diverse landraces were replaced by genetically uniform '
        'high-yield varieties. Each generation of Green Revolution success reduces '
        'the genetic diversity available to breed the next generation of resilient '
        'varieties.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The soil cascade is the consequence most existential in its long-term '
        'implications. Topsoil \u2014 the biologically active upper layer of soil '
        'in which plant roots grow and from which crops extract nutrients \u2014 '
        'forms at a rate of approximately one inch per 500 years through the '
        'decomposition of organic matter and the weathering of mineral particles '
        'by soil organisms. Intensive agriculture erodes topsoil at a rate of '
        'approximately one inch per 20 years through tillage, water erosion, and '
        'wind erosion \u2014 25 times faster than it is formed. A 2015 report by '
        'the UN Food and Agriculture Organisation estimated that 40 percent of '
        'global agricultural land is now degraded, and that at current rates of '
        'degradation, the world has approximately 60 harvests of topsoil remaining. '
        'The Ogallala Aquifer, which underlies the Great Plains of the United States '
        'and supplies 30 percent of US groundwater used for irrigation, is being '
        'depleted at 10 to 100 times its natural recharge rate. In parts of India\'s '
        'Punjab \u2014 the heartland of the Green Revolution \u2014 the water table '
        'has fallen by up to 30 centimetres per year. When these aquifers are '
        'exhausted and when degraded soils can no longer support current yields, '
        'the food production system that has fed the world for sixty years will face '
        'a structural crisis that the Green Revolution itself helped to create.',
        S['body']))
    story.append(SP(14))

    story.append(P(
        'The seed sovereignty cascade has concentrated control over the global food '
        'system in ways that create both economic and biological fragility. The Green '
        'Revolution accelerated the commercialisation of seed, as farmers who had '
        'previously saved and replanted their own seeds were encouraged to purchase '
        'high-yield commercial varieties that often could not be saved effectively '
        'due to hybrid genetics or intellectual property restrictions. Monsanto\'s '
        'introduction of herbicide-tolerant Roundup Ready soybeans in 1996 and the '
        'subsequent development of the trait licensing model \u2014 in which farmers '
        'pay annual fees for the right to plant patented seed and sign contracts '
        'prohibiting seed saving \u2014 transformed the seed supply from a commons '
        'maintained by millions of farmers to a commercial commodity controlled by '
        'a small number of corporations. Following the merger of Bayer and Monsanto '
        'in 2018 and ChemChina\'s acquisition of Syngenta, three companies \u2014 '
        'Bayer-Monsanto, ChemChina-Syngenta, and Corteva \u2014 control approximately '
        '60 percent of the global commercial seed market. The cascade from the '
        'Green Revolution\'s success has produced a food system whose biological '
        'foundation is controlled by fewer companies than could fit in a '
        'boardroom.',
        S['body']))
    story.append(SP(14))

    story.append(fig_green_revolution_tradeoffs())
    story.append(SP(8))
    story.append(P(
        'Figure 9.3: The Green Revolution: success and cascade. Left panel: wheat '
        'yields in tonnes per hectare have nearly tripled since 1961, representing '
        'one of the greatest humanitarian achievements in history. Right panel: '
        'the environmental costs \u2014 coastal dead zones and degraded land \u2014 '
        'have grown in near-parallel, representing the cascade embedded in the solution.',
        S['caption']))

    # extension sections cut in v63 trim
    story.append(PageBreak())
    return story
