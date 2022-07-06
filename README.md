# Reflections of Idiographic Model Parameters in Resting-State Electrophysiological Signals

This repository contains the data, analysis, and results of the
"Antelope" project, carried out by Peiyun Zhou and Andrea Stocco at
the University of Washington and [Florian Sense](https://fsense.github.io/) and [Hedderik van Rijn](http://www.van-rijn.org/) at the University of Groningen, The Netherlands.

For more information about the project, please refer to the following publications:

>   Zhou, P., Sense, F., Van Rijn, H., & Stocco, A. (2021). Reflections of idiographic long-term memory characteristics in resting-state neuroimaging data. _Cognition_, 212, 104660.

## Rationale

In a series of papers, Sense and van Rijn demonstrated that the rate
of forgetting in long-term memory is stable across time and materials
within an individual---it is, thus, akin to what personality
psychologists would call a _trait_, and to what computational
neuroscientists and statisticians would call an _idiographic
parameter_.

It is likely that such idiographic characteristics reflect the
underlying biology of an individual. If this is true, then the
parameter should be reflected in some measures of recordable
electropshyiological activity, such as fMRI, EEG, or PET recordings.

## Resting State Neuroimaging

For this project, we focused on _resting state_ neuroimaging. It is
now accepted that a large part of the brain's activity occurs
spontaneusly and can be captured at rest. This resting state activity
is stable within an individual and highly predictive and individual
characteristics. It provides an ideal ground to identify idiographic
parameters because it does not depend on task-based assumptions.

### Resting State EEG

Specifically, in this project, we focused on resting-state EEG, 5-min
continuous recordings of EEG activity collected while participants
were relaxing (but not asleep) on a chair with their eyes
closed.

EEG data were collected using inexpensive, easily available,
over-the-counter Emotiv headsets, thus making this project a litmus
test for this type of approach: If idiographic parameters can be
identified with this type of headsets, then surely much better can be
done with higher-quality equipment.

## Results

We found that the rate of forgetting in long term declarative memory
(as estimated by the alpha parameter in Pavlik & Anderson's model),
with the strongest correlations found in the beta frequency band over
frontal (AF3 and AF4) and right parietal (P8) lolcations, as shown in
these topological maps.

Here are the correlations found for eyes-closed EEG recordings:

![Topological map of the correlations with rate of
 forgetting](images/topo_correlations_eyes_closed.png)

And here are the correlations found for eyes-open EEG recordings:

![Topological map of the correlations with rate of
 forgetting](images/topo_correlations_eyes_open.png)


