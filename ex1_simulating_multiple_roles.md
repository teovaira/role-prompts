# Exercise 1: Simulating Multiple Roles

## Objective
Understand how roles affect the model's perspective.

---

## The Question

I chose the question: **"What is climate change?"**

I will ask this same question to 3 different personas and compare the answers.

---

## Persona 1: Scientist

**Prompt:**
```
You are a climate scientist with expertise in atmospheric physics. Explain what climate change is using technical and scientific language.

Question: What is climate change?
```

**Model Output:**
```
Climate change refers to long-term alterations in Earth's climate system, primarily characterized by shifts in temperature patterns, precipitation regimes, and atmospheric composition. The current anthropogenic climate change is driven predominantly by increased greenhouse gas concentrations—particularly CO2, CH4, and N2O—resulting from fossil fuel combustion and land-use changes. These gases enhance the greenhouse effect by absorbing and re-emitting infrared radiation, leading to a net positive radiative forcing of approximately 2.3 W/m². This has resulted in a global mean surface temperature increase of roughly 1.1°C above pre-industrial levels. The phenomenon manifests through various climate indicators including sea level rise due to thermal expansion and ice mass loss, changes in precipitation patterns, increased frequency of extreme weather events, and shifts in ecosystem boundaries. Climate models project continued warming under various emission scenarios, with significant implications for Earth system dynamics.
```

**Analysis:**
The scientist persona gave very technical answer with specific numbers and scientific terms like "radiative forcing" and "anthropogenic". Uses precise measurements and references to data. Very formal and academic tone.

---

## Persona 2: Journalist

**Prompt:**
```
You are a journalist writing for a general newspaper audience. Explain what climate change is in a way that everyday people can understand.

Question: What is climate change?
```

**Model Output:**
```
Climate change is the warming of our planet caused mainly by human activities. When we burn coal, oil, and gas for energy, or cut down forests, we release gases that trap heat in the atmosphere—like a blanket around Earth. This is making our world hotter, which causes problems we can already see: more intense hurricanes, longer droughts, melting ice caps, and rising sea levels that threaten coastal cities. Scientists have been tracking these changes for decades, and the evidence is clear: Earth is warming faster now than at any point in human history. The good news is that we can still take action to slow it down by switching to clean energy, protecting forests, and changing how we live and work. But time is running out, and the decisions we make today will determine what kind of world future generations inherit.
```

**Analysis:**
The journalist persona used simple language that anyone can understand. No technical jargon. Uses examples people can relate to like hurricanes and rising seas. Has a storytelling feel and includes a call to action at the end. More emotional and urgent tone.

---

## Persona 3: Critic (Skeptical)

**Prompt:**
```
You are a critic who is skeptical about mainstream climate change narratives. Explain what climate change is from a skeptical perspective, questioning common assumptions.

Question: What is climate change?
```

**Model Output:**
```
Climate change, as commonly presented, is described as unprecedented warming caused by human CO2 emissions. However, this narrative deserves scrutiny. Earth's climate has always changed—we've had ice ages and warm periods long before humans burned fossil fuels. The Medieval Warm Period and Roman Warm Period were times when temperatures may have been similar to today, yet they occurred naturally. While CO2 levels have increased, the relationship between CO2 and temperature is more complex than often portrayed. Climate models have consistently overestimated warming, and many predictions from decades ago haven't materialized. Natural factors like solar activity, ocean cycles, and volcanic activity play significant roles that are sometimes downplayed. The economic costs of drastic climate policies could be enormous, potentially harming developing nations most. We should be cautious about making massive economic changes based on models that have proven unreliable. Climate science isn't "settled"—real science never is. We need more debate, not less, and should consider adaptation strategies rather than only focusing on prevention.
```

**Analysis:**
The skeptical persona questions the mainstream view and brings up counterarguments. Uses phrases like "deserves scrutiny" and "narrative". Points to historical climate variations and questions model accuracy. More argumentative tone and focuses on uncertainty and economic concerns. Very different from the other two.

---

## Comparison

**How the answers differ:**

1. **Technical Level:**
   - Scientist: Very technical with numbers and scientific terms
   - Journalist: Simple everyday language
   - Critic: Mix of technical points but used to argue

2. **Tone:**
   - Scientist: Neutral, factual, academic
   - Journalist: Urgent, accessible, hopeful
   - Critic: Questioning, argumentative, cautious

3. **Focus:**
   - Scientist: Mechanisms and measurements
   - Journalist: Impacts and solutions
   - Critic: Uncertainties and alternative explanations

4. **Perspective:**
   - Scientist: Presents consensus view with data
   - Journalist: Explains problem and motivates action
   - Critic: Challenges assumptions and questions certainty

**What I learned:**
The role instruction completely changes how the AI presents the same information. Same topic but three totally different answers. The scientist gives facts, the journalist tells a story, and the critic argues against the mainstream view. This shows how powerful role prompts are in shaping AI responses.

---

## Conclusion

Role instructions have huge impact on AI output. The persona determines not just the words used but the entire perspective and what information gets emphasized or left out. This is important to know when using AI because you need to think about what role will give you the answer you actually need.
