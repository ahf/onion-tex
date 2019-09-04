---
title: The Design and Implementation of Tor
subtitle: A Gentle Introduction
date: June 13, 2019
author:
  - name: Alexander Færøy
slides:
    aspect-ratio: 169
    font-size: 14pt
    table-of-contents: false
---

## Snowflake {.t}

\centering
\begin{tikzpicture}
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{relay}=[circle, draw, thin, fill=OnionDarkPurple!80, scale=0.8]

    %% Alice.
    \node[] at (-6, 2.5) {Alice};
    \node[alice, monitor, minimum size=1.6cm] (alice) at (-6, 0.5) {};

    %% The Anonymity Network cloud.
    \node[cloud, fill=OnionPurple!40, cloud puffs=16, cloud puff arc=100, minimum width=5.5cm, minimum height=2.6cm, aspect=1] at (4, 1.5) {};

    %% Helper lines for debugging.
    %% \draw[help lines] (-7,-3) grid (7,3);
\end{tikzpicture}

