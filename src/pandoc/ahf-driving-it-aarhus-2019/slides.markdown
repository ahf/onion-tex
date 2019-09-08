---
title: Censorship Circumvention with Tor
date: September 5, 2019
institute: Driving IT Aarhus
author:
  - name: Alexander Færøy
    email: ahf@torproject.org
slides:
    aspect-ratio: 169
    font-size: 14pt
    table-of-contents: false
---

## About Me

\begin{columns}
    \begin{column}{0.65\textwidth}
        \begin{itemize}
            \item Core Developer at The Tor Project since early 2017.
            \item Free Software developer since 2006.
            \item Worked with distributed systems in the Erlang programming
                  language, WebKit-based mobile web browsers, consulting, and firmware
                  development.
            \item Co-organizing the annual Danish hacker festival
                  \href{https://bornhack.dk/}{BornHack} on Funen.
        \end{itemize}
    \end{column}

    \begin{column}{0.35\textwidth}
        \begin{center}
            \includegraphics[width=0.95\textwidth]{images/tor_man.png}
        \end{center}
    \end{column}
\end{columns}

## What is Tor?

\begin{columns}
    \begin{column}{0.6\textwidth}
        \begin{itemize}
            \item Online anonymity, and censorship circumvention.
                \begin{itemize}
                    \item Free software.
                    \item Open network.
                \end{itemize}
            \item Community of researchers, developers, users, and relay operators.
            \item U.S. 501(c)(3) non-profit organization.
        \end{itemize}
    \end{column}

    \begin{column}{0.4\textwidth}
        \begin{center}
            \includegraphics[width=0.95\textwidth]{images/what_is_tor.jpg}
        \end{center}
    \end{column}
\end{columns}

## History

**1990s**
  : Onion routing for privacy online.

**Early 2000s**
  : Working with the U.S. Naval Research Laboratory.

**2004**
  : Sponsorship by the Electronic Frontier Foundation.

**2006**
  : The Tor Project, Inc. became a non-profit.

**2007**
  : \highlight{Expansion to anti-censorship.}

**2008**
  : Tor Browser development.

**2010**
  : The Arab spring.

**2013**
  : The summer of Snowden.

**2018**
  : \highlight{Dedicated anti-censorship team created.}

## {.plain}

\begin{tikzpicture}[remember picture,overlay, background rectangle/.style={fill=OnionDarkPurple}, show background rectangle]
    \node[text=white, at=(current page.north), yshift=-2.5cm, font=\bfseries] {Somewhere between 2,000,000 and 8,000,000 daily users.};
    \node[at=(current page.center), yshift=-2.5cm, align=center] {\input{images/tor_group.tex}};
\end{tikzpicture}

## {.plain}

\begin{tikzpicture}[remember picture,overlay]
    \node[at=(current page.center)] {\includegraphics[width=\paperwidth, height=\paperheight]{images/tor_browser.png}};
\end{tikzpicture}

## {.plain}

\begin{tikzpicture}[remember picture,overlay, background rectangle/.style={fill=OnionDarkPurple}, show background rectangle]
    \node[at=(current page.center)] {\includegraphics[scale=0.20]{images/tor_browser_android.png}};
\end{tikzpicture}

## Threat Model {.t}

\centering
\begin{tikzpicture}
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{relay}=[circle, draw, thin, fill=OnionDarkPurple!80, text=white, font=\scriptsize, scale=0.8]

    %% Alice.
    \node[] at (-6, 2.5) {Alice};
    \node[alice, monitor, minimum size=1.6cm] (alice) at (-6, 0.5) {};

    %% Bob.
    \node[] at (6, 2.5) {Bob};
    \node[bob, mirrored, monitor, minimum size=1.6cm] (bob) at (6, 0.5) {};

    %% The Anonymity Network cloud.
    \node[] at (0, 2) {Anonymity Network};
    \node[cloud, fill=OnionPurple!40, cloud puffs=16, cloud puff arc=100, minimum width=5.5cm, minimum height=2.6cm, aspect=1] at (0,0) {};

    %% The relay nodes inside the Anonymity Network cloud.
    \node[relay] (r1) at (-1.9, 0.2)  {$R_{1}$};
    \node[relay] (r2) at (0.0, 0.1)   {$R_{2}$};
    \node[relay] (r3) at (1.8, -0.4)  {$R_{3}$};
    \node[relay] (r4) at (-0.7, 0.7)  {$R_{4}$};
    \node[relay] (r5) at (-1.0, -0.7) {$R_{5}$};
    \node[relay] (r6) at (0.8, -0.6)  {$R_{6}$};
    \node[relay] (r7) at (1.2, 0.5)   {$R_{7}$};

    %% Paths between our three relays.
    \path[thick] (r1) edge (r2);
    \path[thick] (r2) edge (r3);

    %% Path between Alice and R1.
    \path[thick] (-4.4, -0.4) edge (r1);

    %% Path between R3 and Bob.
    \path[thick] (r3) edge (4.4, -0.4);

    %% Helper lines for debugging.
    %% \draw[help lines] (-7,-3) grid (7,3);
\end{tikzpicture}

\large{What can the attacker do?}

## Threat Model {.t}

\centering
\begin{tikzpicture}
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{relay}=[circle, draw, thin, fill=OnionDarkPurple!80, text=white, font=\scriptsize, scale=0.8]
    \tikzstyle{wiretap}=[circle, draw, thin, fill=red!40, scale=0.8]

    %% Alice.
    \node[] at (-6, 2.5) {Alice};
    \node[alice, monitor, minimum size=1.6cm] (alice) at (-6, 0.5) {};

    %% Bob.
    \node[] at (6, 2.5) {Bob};
    \node[bob, mirrored, monitor, minimum size=1.6cm] (bob) at (6, 0.5) {};

    %% The Anonymity Network cloud.
    \node[] at (0, 2) {Anonymity Network};
    \node[cloud, fill=OnionPurple!40, cloud puffs=16, cloud puff arc=100, minimum width=5.5cm, minimum height=2.6cm, aspect=1] at (0,0) {};

    %% The relay nodes inside the Anonymity Network cloud.
    \node[relay] (r1) at (-1.9, 0.2)  {$R_{1}$};
    \node[relay] (r2) at (0.0, 0.1)   {$R_{2}$};
    \node[relay] (r3) at (1.8, -0.4)  {$R_{3}$};
    \node[relay] (r4) at (-0.7, 0.7)  {$R_{4}$};
    \node[relay] (r5) at (-1.0, -0.7) {$R_{5}$};
    \node[relay] (r6) at (0.8, -0.6)  {$R_{6}$};
    \node[relay] (r7) at (1.2, 0.5)   {$R_{7}$};

    %% Paths between our three relays.
    \path[thick] (r1) edge (r2);
    \path[thick] (r2) edge (r3);

    %% Path between Alice and R1.
    \path[thick] (-4.4, -0.4) edge (r1);

    %% Path between R3 and Bob.
    \path[thick] (r3) edge (4.4, -0.4);

    %% Adversary.
    \node[maninblack, monitor, minimum size=1.3cm] (adversary) at (-5, -2) {};

    %% Adversary wiretap.
    \node[wiretap] (wiretap) at (-3.4, -0.15) {};

    %% Adversary path.
    \path[thick, red!40] (adversary) edge (wiretap);

    %% Helper lines for debugging.
    %% \draw[help lines] (-7,-3) grid (7,3);
\end{tikzpicture}

## Threat Model {.t}

\centering
\begin{tikzpicture}
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{relay}=[circle, draw, thin, fill=OnionDarkPurple!80, text=white, font=\scriptsize, scale=0.8]
    \tikzstyle{wiretap}=[circle, draw, thin, fill=red!40, scale=0.8]

    %% Alice.
    \node[] at (-6, 2.5) {Alice};
    \node[alice, monitor, minimum size=1.6cm] (alice) at (-6, 0.5) {};

    %% Bob.
    \node[] at (6, 2.5) {Bob};
    \node[bob, mirrored, monitor, minimum size=1.6cm] (bob) at (6, 0.5) {};

    %% The Anonymity Network cloud.
    \node[] at (0, 2) {Anonymity Network};
    \node[cloud, fill=OnionPurple!40, cloud puffs=16, cloud puff arc=100, minimum width=5.5cm, minimum height=2.6cm, aspect=1] at (0,0) {};

    %% The relay nodes inside the Anonymity Network cloud.
    \node[relay, fill=red!40, text=black] (r1) at (-1.9, 0.2)  {$R_{1}$};
    \node[relay] (r2) at (0.0, 0.1)   {$R_{2}$};
    \node[relay, fill=red!40, text=black] (r3) at (1.8, -0.4)  {$R_{3}$};
    \node[relay] (r4) at (-0.7, 0.7)  {$R_{4}$};
    \node[relay] (r5) at (-1.0, -0.7) {$R_{5}$};
    \node[relay] (r6) at (0.8, -0.6)  {$R_{6}$};
    \node[relay] (r7) at (1.2, 0.5)   {$R_{7}$};

    %% Paths between our three relays.
    \path[thick] (r1) edge (r2);
    \path[thick] (r2) edge (r3);

    %% Path between Alice and R1.
    \path[thick] (-4.4, -0.4) edge (r1);

    %% Path between R3 and Bob.
    \path[thick] (r3) edge (4.4, -0.4);

    %% Adversary.
    \node[maninblack, monitor, minimum size=1.3cm] (adversary) at (-5, -2) {};

    %% Path between our adversary and R1 and R3.
    \path[thick, red!40] (adversary) edge (r1);
    \path[thick, red!40, bend right] (-3.5, -3.0) edge (r3);

    %% Helper lines for debugging.
    %% \draw[help lines] (-7,-3) grid (7,3);
\end{tikzpicture}

## Threat Model {.t}

\centering
\begin{tikzpicture}
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{relay}=[circle, draw, thin, fill=OnionDarkPurple!80, text=white, font=\scriptsize, scale=0.8]
    \tikzstyle{wiretap}=[circle, draw, thin, fill=red!40, scale=0.8]

    %% Alice.
    \node[] at (-6, 2.5) {Alice};
    \node[alice, monitor, minimum size=1.6cm] (alice) at (-6, 0.5) {};

    %% Bob.
    \node[] at (6, 2.5) {Bob};
    \node[bob, mirrored, monitor, minimum size=1.6cm] (bob) at (6, 0.5) {};

    %% The Anonymity Network cloud.
    \node[] at (0, 2) {Anonymity Network};
    \node[cloud, fill=OnionPurple!40, cloud puffs=16, cloud puff arc=100, minimum width=5.5cm, minimum height=2.6cm, aspect=1] at (0,0) {};

    %% The relay nodes inside the Anonymity Network cloud.
    \node[relay] (r1) at (-1.9, 0.2)  {$R_{1}$};
    \node[relay] (r2) at (0.0, 0.1)   {$R_{2}$};
    \node[relay] (r3) at (1.8, -0.4)  {$R_{3}$};
    \node[relay] (r4) at (-0.7, 0.7)  {$R_{4}$};
    \node[relay] (r5) at (-1.0, -0.7) {$R_{5}$};
    \node[relay] (r6) at (0.8, -0.6)  {$R_{6}$};
    \node[relay] (r7) at (1.2, 0.5)   {$R_{7}$};

    %% Paths between our three relays.
    \path[thick] (r1) edge (r2);
    \path[thick] (r2) edge (r3);

    %% Path between Alice and R1.
    \path[thick] (-4.4, -0.4) edge (r1);

    %% Path between R3 and Bob.
    \path[thick] (r3) edge (4.4, -0.4);

    %% Adversary.
    \node[maninblack, monitor, minimum size=1.3cm] (adversary) at (-5, -2) {};

    %% Adversary wiretap.
    \node[wiretap] (wiretap) at (3.4, -0.38) {};

    %% Path between our adversary and its wiretap.
    \path[thick, red!40, bend right] (-3.5, -3.0) edge (wiretap);

    %% Helper lines for debugging.
    %% \draw[help lines] (-7,-3) grid (7,3);
\end{tikzpicture}

## Threat Model {.t}

\centering
\begin{tikzpicture}
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{relay}=[circle, draw, thin, fill=OnionDarkPurple!80, text=white, font=\scriptsize, scale=0.8]

    %% Alice.
    \node[] at (-6, 2.5) {Alice};
    \node[alice, monitor, minimum size=1.6cm] (alice) at (-6, 0.5) {};

    %% Bob.
    \node[] at (6, 2.5) {Bob};
    \node[maninblack, mirrored, monitor, minimum size=1.6cm] (bob) at (6, 0.5) {};

    %% The Anonymity Network cloud.
    \node[] at (0, 2) {Anonymity Network};
    \node[cloud, fill=OnionPurple!40, cloud puffs=16, cloud puff arc=100, minimum width=5.5cm, minimum height=2.6cm, aspect=1] at (0,0) {};

    %% The relay nodes inside the Anonymity Network cloud.
    \node[relay] (r1) at (-1.9, 0.2)  {$R_{1}$};
    \node[relay] (r2) at (0.0, 0.1)   {$R_{2}$};
    \node[relay] (r3) at (1.8, -0.4)  {$R_{3}$};
    \node[relay] (r4) at (-0.7, 0.7)  {$R_{4}$};
    \node[relay] (r5) at (-1.0, -0.7) {$R_{5}$};
    \node[relay] (r6) at (0.8, -0.6)  {$R_{6}$};
    \node[relay] (r7) at (1.2, 0.5)   {$R_{7}$};

    %% Paths between our three relays.
    \path[thick] (r1) edge (r2);
    \path[thick] (r2) edge (r3);

    %% Path between Alice and R1.
    \path[thick] (-4.4, -0.4) edge (r1);

    %% Path between R3 and Bob.
    \path[thick] (r3) edge (4.4, -0.4);

    %% Helper lines for debugging.
    %% \draw[help lines] (-7,-3) grid (7,3);
\end{tikzpicture}

## Anonymity isn't Encryption {.t}

\centering
\begin{tikzpicture}
    \tikzstyle{wiretap}=[circle, draw, thin, fill=red!40, scale=0.8]

    %% Alice.
    \node[] at (-6, 2.5) {Alice};
    \node[alice, monitor, minimum size=1.6cm] (alice) at (-6, 0.5) {};

    %% Bob.
    \node[] at (6, 2.5) {Bob};
    \node[bob, mirrored, monitor, minimum size=1.6cm] (bob) at (6, 0.5) {};

    %% Encrypted channel.
    \draw[<->,thick, OnionDarkPurple!80] (-3.5, 0) -- (3.5, 0);

    %% Encrypted data.
    \node[] at (0, 0.5) {\tiny{\texttt{\ldots RG9uJ3QgdXNlIGJhc2U2NCBmb3IgZW5jcnlwdGlvbi4\ldots}}};

    %% Adversary.
    \node[maninblack, monitor, minimum size=1.3cm] (adversary) at (-5, -2) {};
    \node[ellipse callout, draw, yshift=0.3cm, callout absolute pointer={(adversary.mouth)}, font=\scriptsize, align=center, fill=white] at (-2.7, -2.5) {Gibberish!};

    %% Adversary wiretap.
    \node[wiretap] (wiretap) at (-0.5, 0) {};

    %% Adversary path.
    \path[thick, red!40] (adversary) edge (wiretap);

    %% Helper lines for debugging.
    %% \draw[help lines] (-7,-3) grid (7,3);
\end{tikzpicture}

\large{Encryption just protects contents.}

## Metadata

\centering

\includegraphics[width=0.6\textwidth]{images/michael_hayden.jpg}

\begin{minipage}[b]{0.7\textwidth}
    \begin{quote}
        \small{"We Kill People Based on Metadata."}

        \begin{flushright}
            \footnotesize{---Michael Hayden, former director of the NSA.}
        \end{flushright}
    \end{quote}
\end{minipage}

## A Simple Design {.t}

\centering
\begin{tikzpicture}
    %% Define our styles.
    \tikzstyle{person}=[monitor, minimum size=1.0cm]
    \tikzstyle{arrow}=[->, thick, shorten >= 0.6cm, shorten <= 0.6cm]
    \tikzstyle{message}=[sloped, above, midway, font=\scriptsize]

    %% Our central relay.
    \node[circle, draw, thin, fill=OnionDarkPurple!80, text=white, minimum size=2.1cm, align=center] (relay) at (0, 0) {Relay};

    %% First couple.
    \node[alice, person] (alice_1) at (-4.5, 2.0) {};
    \node[bob, mirrored, person] (bob_3) at (4.5, -2.0) {};

    \draw[arrow, cyan!70] (alice_1) -- node [message] {$Enc(Bob_{3}, "x")$} (relay);
    \draw[arrow, cyan!70] (relay) -- node [message] {"x"} (bob_3);

    %% Second couple.
    \node[physician, female, person] (alice_2) at (-5.0, 0.0) {};
    \node[surgeon, mirrored, person] (bob_1) at (4.5, 2.0) {};

    \draw[arrow, purple!70] (alice_2) -- node [message] {$Enc(Bob_{1}, "y")$} (relay);
    \draw[arrow, purple!70] (relay) -- node [message] {"y"} (bob_1);

    %% Third couple.
    \node[police, female, person] (alice_3) at (-4.5, -2.0) {};
    \node[police, mirrored, person] (bob_2) at (5.0, 0.0) {};

    \draw[arrow, violet!70] (alice_3) -- node [message] {$Enc(Bob_{2}, "z")$} (relay);
    \draw[arrow, violet!70] (relay) -- node [message] {"z"} (bob_2);

    %% Helper lines for debugging.
    %% \draw[help lines] (-7,-3) grid (7,3);
\end{tikzpicture}

Equivalent to some commercial proxy providers.

## A Simple Design {.t}

\centering
\begin{tikzpicture}
    %% Define our styles.
    \tikzstyle{person}=[monitor, minimum size=1.0cm]
    \tikzstyle{arrow}=[->, thick, shorten >= 0.6cm, shorten <= 0.6cm]
    \tikzstyle{message}=[sloped, above, midway, font=\scriptsize]

    %% Our central evil relay.
    \node[circle, draw, thin, fill=red!40, text=black, minimum size=2.1cm, align=center] (relay) at (0, 0) {Evil \\ Relay};

    %% First couple.
    \node[alice, person] (alice_1) at (-4.5, 2.0) {};
    \node[bob, mirrored, person] (bob_3) at (4.5, -2.0) {};

    \draw[arrow, cyan!70] (alice_1) -- node [message] {$Enc(Bob_{3}, "x")$} (relay);
    \draw[arrow, cyan!70] (relay) -- node [message] {"x"} (bob_3);

    %% Second couple.
    \node[physician, female, person] (alice_2) at (-5.0, 0.0) {};
    \node[surgeon, mirrored, person] (bob_1) at (4.5, 2.0) {};

    \draw[arrow, purple!70] (alice_2) -- node [message] {$Enc(Bob_{1}, "y")$} (relay);
    \draw[arrow, purple!70] (relay) -- node [message] {"y"} (bob_1);

    %% Third couple.
    \node[police, female, person] (alice_3) at (-4.5, -2.0) {};
    \node[police, mirrored, person] (bob_2) at (5.0, 0.0) {};

    \draw[arrow, violet!70] (alice_3) -- node [message] {$Enc(Bob_{2}, "z")$} (relay);
    \draw[arrow, violet!70] (relay) -- node [message] {"z"} (bob_2);

    %% Helper lines for debugging.
    %% \draw[help lines] (-7,-3) grid (7,3);
\end{tikzpicture}

## A Simple Design {.t}

\centering
\begin{tikzpicture}
    %% Define our styles.
    \tikzstyle{person}=[monitor, minimum size=1.0cm]
    \tikzstyle{arrow}=[->, thick, shorten >= 0.6cm, shorten <= 0.6cm]
    \tikzstyle{message}=[sloped, above, midway, font=\scriptsize]

    %% Our central relay.
    \node[circle, draw, thin, fill=OnionDarkPurple!80, text=white, minimum size=2.1cm, align=center] (relay) at (0, 0) {Relay};

    %% Our wiretap
    \node[circle, draw, thick, red!40, minimum size=2.8cm, align=center] (wiretap) at (0, 0) {};

    %% First couple.
    \node[alice, person] (alice_1) at (-4.5, 2.0) {};
    \node[bob, mirrored, person] (bob_3) at (4.5, -2.0) {};

    \draw[arrow, cyan!70] (alice_1) -- node [message] {$Enc(Bob_{3}, "x")$} (relay);
    \draw[arrow, cyan!70] (relay) -- node [message] {"x"} (bob_3);

    %% Second couple.
    \node[physician, female, person] (alice_2) at (-5.0, 0.0) {};
    \node[surgeon, mirrored, person] (bob_1) at (4.5, 2.0) {};

    \draw[arrow, purple!70] (alice_2) -- node [message] {$Enc(Bob_{1}, "y")$} (relay);
    \draw[arrow, purple!70] (relay) -- node [message] {"y"} (bob_1);

    %% Third couple.
    \node[police, female, person] (alice_3) at (-4.5, -2.0) {};
    \node[police, mirrored, person] (bob_2) at (5.0, 0.0) {};

    \draw[arrow, violet!70] (alice_3) -- node [message] {$Enc(Bob_{2}, "z")$} (relay);
    \draw[arrow, violet!70] (relay) -- node [message] {"z"} (bob_2);

    %% Adversary.
    \node[maninblack, person] (adversary) at (-2, -2) {};

    %% Adversary path.
    \path[thick, red!40] (adversary) edge (wiretap);

    %% Helper lines for debugging.
    %% \draw[help lines] (-7,-3) grid (7,3);
\end{tikzpicture}

Timing analysis bridges all connections going through the relay.

## The Tor Design {.t}

\centering
\begin{tikzpicture}
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{relay}=[circle, draw, thin, fill=OnionDarkPurple!80, text=white, font=\scriptsize, scale=0.8]

    %% Alice.
    \node[] at (-6, 2.5) {Alice};
    \node[alice, monitor, minimum size=1.6cm] (alice) at (-6, 0.5) {};

    %% Bob.
    \node[] at (6, 2.5) {Bob};
    \node[bob, mirrored, monitor, minimum size=1.6cm] (bob) at (6, 0.5) {};

    %% The Anonymity Network cloud.
    \node[] at (0, 2) {Anonymity Network};
    \node[cloud, fill=OnionPurple!40, cloud puffs=16, cloud puff arc=100, minimum width=5.5cm, minimum height=2.6cm, aspect=1] at (0,0) {};

    %% The relay nodes inside the Anonymity Network cloud.
    \node[relay] (r1) at (-1.9, 0.2)  {$R_{1}$};
    \node[relay] (r2) at (0.0, 0.1)   {$R_{2}$};
    \node[relay] (r3) at (1.8, -0.4)  {$R_{3}$};
    \node[relay] (r4) at (-0.7, 0.7)  {$R_{4}$};
    \node[relay] (r5) at (-1.0, -0.7) {$R_{5}$};
    \node[relay] (r6) at (0.8, -0.6)  {$R_{6}$};
    \node[relay] (r7) at (1.2, 0.5)   {$R_{7}$};

    %% Paths between our three relays.
    \path[thick] (r1) edge (r2);
    \path[thick] (r2) edge (r3);

    %% Path between Alice and R1.
    \path[thick] (-4.4, -0.4) edge (r1);

    %% Path between R3 and Bob.
    \path[thick] (r3) edge (4.4, -0.4);

    %% Helper lines for debugging.
    %% \draw[help lines] (-7,-3) grid (7,3);
\end{tikzpicture}

Add multiple relays so that no single relay can betray Alice.

## The Tor Design {.t}

\centering
\begin{tikzpicture}
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{relay}=[circle, draw, thin, fill=OnionDarkPurple!80, text=white, font=\scriptsize, scale=0.8]

    %% Alice.
    \node[] at (-6, 2.5) {Alice};
    \node[alice, monitor, minimum size=1.6cm] (alice) at (-6, 0.5) {};

    %% Bob.
    \node[] at (6, 2.5) {Bob};
    \node[bob, mirrored, monitor, minimum size=1.6cm] (bob) at (6, 0.5) {};

    %% The Anonymity Network cloud.
    \node[] at (0, 2) {Anonymity Network};
    \node[cloud, fill=OnionPurple!40, cloud puffs=16, cloud puff arc=100, minimum width=5.5cm, minimum height=2.6cm, aspect=1] at (0,0) {};

    %% The relay nodes inside the Anonymity Network cloud.
    \node[relay,ultra thick,draw=green!80]  (r1) at (-1.9, 0.2)  {$R_{1}$};
    \node[relay,ultra thick,draw=blue!80]   (r2) at (0.0, 0.1)   {$R_{2}$};
    \node[relay,ultra thick,draw=yellow!80] (r3) at (1.8, -0.4)  {$R_{3}$};
    \node[relay] (r4) at (-0.7, 0.7)  {$R_{4}$};
    \node[relay] (r5) at (-1.0, -0.7) {$R_{5}$};
    \node[relay] (r6) at (0.8, -0.6)  {$R_{6}$};
    \node[relay] (r7) at (1.2, 0.5)   {$R_{7}$};

    %% Helper lines for debugging.
    %% \draw[help lines] (-7,-3) grid (7,3);
\end{tikzpicture}

Alice picks a path through the network: $R_{1}$, $R_{2}$, and $R_{3}$ before finally reaching Bob.

## The Tor Design {.t}

\centering
\begin{tikzpicture}
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{relay}=[circle, draw, thin, fill=OnionDarkPurple!80, text=white, font=\scriptsize, scale=0.8]

    \pgfdeclarelayer{background}
    \pgfdeclarelayer{foreground}
    \pgfsetlayers{background,main,foreground}

    %% Alice.
    \node[] at (-6, 2.5) {Alice};
    \node[alice, monitor, minimum size=1.6cm] (alice) at (-6, 0.5) {};

    %% Bob.
    \node[] at (6, 2.5) {Bob};
    \node[bob, mirrored, monitor, minimum size=1.6cm] (bob) at (6, 0.5) {};

    %% The Anonymity Network cloud.
    \begin{pgfonlayer}{background}
        \node[] at (0, 2) {Anonymity Network};
        \node[cloud, fill=OnionPurple!40, cloud puffs=16, cloud puff arc=100, minimum width=5.5cm, minimum height=2.6cm, aspect=1, on background layer] at (0,0) {};
    \end{pgfonlayer}

    %% The relay nodes inside the Anonymity Network cloud.
    \begin{pgfonlayer}{foreground}
        \node[relay,ultra thick,draw=green!80]  (r1) at (-1.9, 0.2)  {$R_{1}$};
        \node[relay,ultra thick,draw=blue!80]   (r2) at (0.0, 0.1)   {$R_{2}$};
        \node[relay,ultra thick,draw=yellow!80] (r3) at (1.8, -0.4)  {$R_{3}$};
        \node[relay] (r4) at (-0.7, 0.7)  {$R_{4}$};
        \node[relay] (r5) at (-1.0, -0.7) {$R_{5}$};
        \node[relay] (r6) at (0.8, -0.6)  {$R_{6}$};
        \node[relay] (r7) at (1.2, 0.5)   {$R_{7}$};
    \end{pgfonlayer}

    %% Alice connects to R1.
    \path[line width=4.0pt,draw=green!80] (-4.2, -0.4) edge (r1.center);

    %% Helper lines for debugging.
    %% \draw[help lines] (-7,-3) grid (7,3);
\end{tikzpicture}

Alice makes a session key with $R_{1}$.

## The Tor Design {.t}

\centering
\begin{tikzpicture}
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{relay}=[circle, draw, thin, fill=OnionDarkPurple!80, text=white, font=\scriptsize, scale=0.8]

    \pgfdeclarelayer{background}
    \pgfdeclarelayer{foreground}
    \pgfsetlayers{background,main,foreground}

    %% Alice.
    \node[] at (-6, 2.5) {Alice};
    \node[alice, monitor, minimum size=1.6cm] (alice) at (-6, 0.5) {};

    %% Bob.
    \node[] at (6, 2.5) {Bob};
    \node[bob, mirrored, monitor, minimum size=1.6cm] (bob) at (6, 0.5) {};

    %% The Anonymity Network cloud.
    \begin{pgfonlayer}{background}
        \node[] at (0, 2) {Anonymity Network};
        \node[cloud, fill=OnionPurple!40, cloud puffs=16, cloud puff arc=100, minimum width=5.5cm, minimum height=2.6cm, aspect=1, on background layer] at (0,0) {};
    \end{pgfonlayer}

    %% The relay nodes inside the Anonymity Network cloud.
    \begin{pgfonlayer}{foreground}
        \node[relay,ultra thick,draw=green!80]  (r1) at (-1.9, 0.2)  {$R_{1}$};
        \node[relay,ultra thick,draw=blue!80]   (r2) at (0.0, 0.1)   {$R_{2}$};
        \node[relay,ultra thick,draw=yellow!80] (r3) at (1.8, -0.4)  {$R_{3}$};
        \node[relay] (r4) at (-0.7, 0.7)  {$R_{4}$};
        \node[relay] (r5) at (-1.0, -0.7) {$R_{5}$};
        \node[relay] (r6) at (0.8, -0.6)  {$R_{6}$};
        \node[relay] (r7) at (1.2, 0.5)   {$R_{7}$};
    \end{pgfonlayer}

    %% Alice connects to R1.
    \path[line width=8.0pt,draw=green!80] (-4.2, -0.4) edge (r1.center);
    \path[line width=4.0pt,draw=blue!80] (-4.2, -0.4) edge (r1.center);

    %% R1 connects to R2.
    \path[line width=4.0pt,draw=blue!80] (r1.center) edge (r2.center);

    %% Helper lines for debugging.
    %% \draw[help lines] (-7,-3) grid (7,3);
\end{tikzpicture}

Alice asks $R_{1}$ to extend to $R_{2}$.

## The Tor Design {.t}

\centering
\begin{tikzpicture}
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{relay}=[circle, draw, thin, fill=OnionDarkPurple!80, text=white, font=\scriptsize, scale=0.8]

    \pgfdeclarelayer{background}
    \pgfdeclarelayer{foreground}
    \pgfsetlayers{background,main,foreground}

    %% Alice.
    \node[] at (-6, 2.5) {Alice};
    \node[alice, monitor, minimum size=1.6cm] (alice) at (-6, 0.5) {};

    %% Bob.
    \node[] at (6, 2.5) {Bob};
    \node[bob, mirrored, monitor, minimum size=1.6cm] (bob) at (6, 0.5) {};

    %% The Anonymity Network cloud.
    \begin{pgfonlayer}{background}
        \node[] at (0, 2) {Anonymity Network};
        \node[cloud, fill=OnionPurple!40, cloud puffs=16, cloud puff arc=100, minimum width=5.5cm, minimum height=2.6cm, aspect=1, on background layer] at (0,0) {};
    \end{pgfonlayer}

    %% The relay nodes inside the Anonymity Network cloud.
    \begin{pgfonlayer}{foreground}
        \node[relay,ultra thick,draw=green!80]  (r1) at (-1.9, 0.2)  {$R_{1}$};
        \node[relay,ultra thick,draw=blue!80]   (r2) at (0.0, 0.1)   {$R_{2}$};
        \node[relay,ultra thick,draw=yellow!80] (r3) at (1.8, -0.4)  {$R_{3}$};
        \node[relay] (r4) at (-0.7, 0.7)  {$R_{4}$};
        \node[relay] (r5) at (-1.0, -0.7) {$R_{5}$};
        \node[relay] (r6) at (0.8, -0.6)  {$R_{6}$};
        \node[relay] (r7) at (1.2, 0.5)   {$R_{7}$};
    \end{pgfonlayer}

    %% Alice connects to R1.
    \path[line width=12.0pt,draw=green!80] (-4.2, -0.4) edge (r1.center);
    \path[line width=8.0pt,draw=blue!80] (-4.2, -0.4) edge (r1.center);
    \path[line width=4.0pt,draw=yellow!80] (-4.2, -0.4) edge (r1.center);

    %% R1 connects to R2.
    \path[line width=8.0pt,draw=blue!80]   (r1.center) edge (r2.center);
    \path[line width=4.0pt,draw=yellow!80] (r1.center) edge (r2.center);

    %% R2 connects to R3.
    \path[line width=4.0pt,draw=yellow!80] (r2.center) edge (r3.center);

    %% Helper lines for debugging.
    %% \draw[help lines] (-7,-3) grid (7,3);
\end{tikzpicture}

Alice asks $R_{2}$ to extend to $R_{3}$.

## The Tor Design {.t}

\centering
\begin{tikzpicture}
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{relay}=[circle, draw, thin, fill=OnionDarkPurple!80, text=white, font=\scriptsize, scale=0.8]

    \pgfdeclarelayer{background}
    \pgfdeclarelayer{foreground}
    \pgfsetlayers{background,main,foreground}

    %% Alice.
    \node[] at (-6, 2.5) {Alice};
    \node[alice, monitor, minimum size=1.6cm] (alice) at (-6, 0.5) {};

    %% Bob.
    \node[] at (6, 2.5) {Bob};
    \node[bob, mirrored, monitor, minimum size=1.6cm] (bob) at (6, 0.5) {};

    %% The Anonymity Network cloud.
    \begin{pgfonlayer}{background}
        \node[] at (0, 2) {Anonymity Network};
        \node[cloud, fill=OnionPurple!40, cloud puffs=16, cloud puff arc=100, minimum width=5.5cm, minimum height=2.6cm, aspect=1, on background layer] at (0,0) {};
    \end{pgfonlayer}

    %% The relay nodes inside the Anonymity Network cloud.
    \begin{pgfonlayer}{foreground}
        \node[relay,ultra thick,draw=green!80]  (r1) at (-1.9, 0.2)  {$R_{1}$};
        \node[relay,ultra thick,draw=blue!80]   (r2) at (0.0, 0.1)   {$R_{2}$};
        \node[relay,ultra thick,draw=yellow!80] (r3) at (1.8, -0.4)  {$R_{3}$};
        \node[relay] (r4) at (-0.7, 0.7)  {$R_{4}$};
        \node[relay] (r5) at (-1.0, -0.7) {$R_{5}$};
        \node[relay] (r6) at (0.8, -0.6)  {$R_{6}$};
        \node[relay] (r7) at (1.2, 0.5)   {$R_{7}$};
    \end{pgfonlayer}

    %% Alice connects to R1.
    \path[line width=12.0pt,draw=green!80] (-4.2, -0.4) edge (r1.center);
    \path[line width=8.0pt,draw=blue!80]   (-4.2, -0.4) edge (r1.center);
    \path[line width=4.0pt,draw=yellow!80] (-4.2, -0.4) edge (r1.center);
    \path[thick,draw=black           ]     (-4.2, -0.4) edge (r1.center);

    %% R1 connects to R2.
    \path[line width=8.0pt,draw=blue!80]   (r1.center) edge (r2.center);
    \path[line width=4.0pt,draw=yellow!80] (r1.center) edge (r2.center);
    \path[thick,draw=black]                (r1.center) edge (r2.center);

    %% R2 connects to R3.
    \path[line width=4.0pt,draw=yellow!80] (r2.center) edge (r3.center);
    \path[thick,draw=black]                (r2.center) edge (r3.center);

    %% R3 connects to Bob.
    \path[thick,draw=black] (r3.center) edge (4.4, -0.4);

    %% Helper lines for debugging.
    %% \draw[help lines] (-7,-3) grid (7,3);
\end{tikzpicture}

Alice finally asks $R_{3}$ to connect to Bob.

## The Tor Network

\centering
\begin{tikzpicture}
    \begin{axis}[
            title=Number of Relays,
            title style={font=\scriptsize\bfseries},
            no markers,
            enlarge x limits=false,
            grid=both,
            grid style=dashed,
            width=0.85\paperwidth,
            height=0.80\paperheight,
            date coordinates in=x,
            xmin=2010-01-01,
            xmax=2019-01-01,
            xtick={
                {2010-01-01},
                {2011-01-01},
                {2012-01-01},
                {2013-01-01},
                {2014-01-01},
                {2015-01-01},
                {2016-01-01},
                {2017-01-01},
                {2018-01-01},
                {2019-01-01}
            },
            cycle list name=exotic,
            every axis plot/.append style={thick},
            label style={font=\scriptsize},
            tick label style={font=\scriptsize},
            legend style={
                font=\tiny,
            },
            legend pos=north west,
            legend cell align=left,
            unbounded coords=discard,
            xticklabel style={
                anchor=near xticklabel,
            },
            xticklabel=\year\
            ]

        \addlegendentry{Relays}
        \addplot table [x=date, y=relays, col sep=comma] {data/networksize.csv};

        \addlegendentry{Bridges}
        \addplot table [x=date, y=bridges, col sep=comma] {data/networksize.csv};
    \end{axis}
\end{tikzpicture}

\tiny{Source: \href{https://metrics.torproject.org/}{metrics.torproject.org}}

## The Tor Network

\centering
\begin{tikzpicture}
    \begin{axis}[
            title=Total Relay Bandwidth,
            title style={font=\scriptsize\bfseries},
            no markers,
            enlarge x limits=false,
            grid=both,
            grid style=dashed,
            width=0.85\paperwidth,
            height=0.80\paperheight,
            date coordinates in=x,
            xmin=2010-01-01,
            xmax=2019-01-01,
            xtick={
                {2010-01-01},
                {2011-01-01},
                {2012-01-01},
                {2013-01-01},
                {2014-01-01},
                {2015-01-01},
                {2016-01-01},
                {2017-01-01},
                {2018-01-01},
                {2019-01-01}
            },
            cycle list name=exotic,
            every axis plot/.append style={thick},
            label style={font=\scriptsize},
            tick label style={font=\scriptsize},
            legend style={
                font=\tiny,
            },
            legend pos=north west,
            legend cell align=left,
            unbounded coords=discard,
            xticklabel style={
                anchor=near xticklabel,
            },
            ylabel={Bandwidth in Gbit/s},
            xticklabel=\year\
            ]

        \addlegendentry{Advertised Bandwidth}
        \addplot table [x=date, y=advbw, col sep=comma] {data/bandwidth-flags_compressed.csv};

        \addlegendentry{Bandwidth History}
        \addplot table [x=date, y=bwhist, col sep=comma] {data/bandwidth-flags_compressed.csv};
    \end{axis}
\end{tikzpicture}

\tiny{Source: \href{https://metrics.torproject.org/}{metrics.torproject.org}}

## The Tor Network

Tor's **safety** comes from **diversity**:

1. Diversity of relays. The more relays we have and the more diverse
   they are, the fewer attackers are in a position to do traffic confirmation.

2. Diversity of users and reasons to use it. 50000 users in Iran means
   almost all of them are normal citizens.

**Research problem**: How do we measure diversity over time?

## {.plain .noframenumbering}

\begin{tikzpicture}[overlay, remember picture]
    \node[anchor=center] at (current page.center) {
        \begin{minipage}[c]{0.85\textwidth}
            \small{\highlight{I live in Iran and I have been using Tor for
            censorship circumvention.} During political unrest while the government
            tightens grip on other censorship circumvention alternatives,
            \highlight{Tor with obfuscation plugins remains the only solution.} \\

            Tor changed my personal life in many ways. \highlight{It made it possible
            to access information on Youtube, Twitter, Blogger and countless other sites.}
            I am grateful of Tor project, people working on it as well as people running
            Tor nodes.}

            \begin{flushright}
                \footnotesize{---Anonymous Tor User.}
            \end{flushright}
        \end{minipage}
    };
\end{tikzpicture}

## {.plain}

\begin{tikzpicture}[remember picture,overlay]
    \node[at=(current page.center)] {\includegraphics[width=\paperwidth, height=\paperheight]{images/block_result.png}};
\end{tikzpicture}

## {.plain}

\begin{tikzpicture}[remember picture,overlay]
    \node[at=(current page.center)] {\includegraphics[width=\paperwidth, height=\paperheight]{images/tdc_dk_block.png}};
\end{tikzpicture}

## Introduction to Censorship {.c}

\vspace*{0.9cm}
\centering
\begin{tikzpicture}[overlay,scale=1.32]
    %% Clip everything that is outside of our "viewport"
    \clip (-7, -3) rectangle (7, 3);

    %% Our censored area.
    \node[circle, draw=red!40, fill=red!5, thick, dashed, minimum width=50cm] (censored area) at (-20, 0) {};
    \node[font=\footnotesize\bfseries, align=center] at (-4, 2.5) {Censored Region};

    %% Alice.
    \node[font=\small] at (-4, 1.5) {Alice};
    \node[alice, monitor, minimum size=1.2cm] (alice) at (-4, 0) {};
    \node[ellipse callout, draw, yshift=0.3cm, callout absolute pointer={(alice.mouth)}, font=\small\bfseries, align=center, fill=white] at (-2.5, 0.5) {!?!?!};

    \draw[<-, thick, OnionDarkPurple!80] (-2.5, 0) -- (-1.0, 0);

    %% Bob.
    \node[font=\small] at (4, 1.5) {Bob};
    \node[bob, mirrored, monitor, minimum size=1.2cm] (bob) at (4, 0) {};

    \node[font=\small] at (0, -2) {Alice is unable to reach Bob.};

    %% Helper lines for debugging.
    %% \node[] at (0.0, 0.0) {X};
    %% \draw[help lines] (-7, -3) grid (7, 3);
\end{tikzpicture}

## Introduction to Censorship {.c}

\vspace*{0.9cm}
\centering
\begin{tikzpicture}[overlay,scale=1.32]
    %% Clip everything that is outside of our "viewport"
    \clip (-7, -3) rectangle (7, 3);

    %% Our censored area.
    \node[circle, draw=red!40, fill=red!5, thick, dashed, minimum width=50cm] (censored area) at (-20, 0) {};
    \node[font=\footnotesize\bfseries, align=center] at (-4, 2.5) {Censored Region};

    %% Alice.
    \node[font=\small] at (-4, 1.5) {Alice};
    \node[alice, monitor, minimum size=1.2cm] (alice) at (-4, 0) {};
    \node[ellipse callout, draw, yshift=0.3cm, callout absolute pointer={(alice.mouth)}, font=\small\bfseries, align=center, fill=white] at (-2.5, 0.5) {!?!};

    \draw[<-, thick, OnionDarkPurple!80] (-2.5, 0) -- (-1.0, 0);
    \draw[->, thick, dashed, OnionDarkPurple!80] (-1.05, 0) -- (2.5, 0);

    %% Bob.
    \node[font=\small] at (4, 1.5) {Bob};
    \node[bob, mirrored, monitor, minimum size=1.2cm] (bob) at (4, 0) {};

    \node[font=\small] at (0, -2) {Alice can reach Bob, but their connection is throttled.};

    %% Helper lines for debugging.
    %% \node[] at (0.0, 0.0) {X};
    %% \draw[help lines] (-7, -3) grid (7, 3);
\end{tikzpicture}

## Introduction to Censorship {.c}

\vspace*{0.9cm}
\centering
\begin{tikzpicture}[overlay,scale=1.32]
    %% Clip everything that is outside of our "viewport"
    \clip (-7, -3) rectangle (7, 3);

    %% Our censored area.
    \node[circle, draw=red!40, fill=red!5, thick, dashed, minimum width=50cm] (censored area) at (-20, 0) {};
    \node[font=\footnotesize\bfseries, align=center] at (-4, 2.5) {Censored Region};

    %% Alice.
    \node[font=\small] at (-4, 1.5) {Alice};
    \node[alice, monitor, minimum size=1.2cm] (alice) at (-4, 0) {};

    \draw[<->, thick, OnionDarkPurple!80] (-2.5, 0) -- (2.5, 0);

    %% Bob.
    \node[font=\small] at (4, 1.5) {Bob};
    \node[graduate, mirrored, monitor, minimum size=1.2cm] (bob) at (4, 0) {};

    \node[font=\small] at (0, -2) {Alice can reach Bob because the censor thinks Bob is fine.};

    %% Helper lines for debugging.
    %% \node[] at (0.0, 0.0) {X};
    %% \draw[help lines] (-7, -3) grid (7, 3);
\end{tikzpicture}

## Anti-censorship Strategies

1. Censors will apply censorship to **all** relays in the network and effectively block access to the Tor network.
2. Censors will apply censorship to **known** bridges.

**Solution**: We make it difficult to find and block bridges and we make it
difficult to learn if a given connection is between a Tor user and an
entry-point into the Tor network.

## Bridges

\vspace*{0.9cm}
\centering
\begin{tikzpicture}[overlay,scale=1.32]
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{relay}=[circle, draw, thin, fill=OnionDarkPurple!80, text=white, font=\scriptsize, scale=0.8]
    \tikzstyle{bridge}=[circle, draw, thin, fill=cyan!80, text=white, font=\scriptsize, scale=0.8]

    %% Clip everything that is outside of our "viewport"
    \clip (-7, -3) rectangle (7, 3);

    %% Our censored area.
    \node[circle, draw=red!40, fill=red!5, thick, dashed, minimum width=50cm] (censored area) at (-20, 0) {};
    \node[font=\footnotesize\bfseries, align=center] at (-4, 2.5) {Censored Region};

    %% The Anonymity Network cloud.
    \node[cloud, fill=OnionPurple!40, cloud puffs=16, cloud puff arc=100, minimum width=5.5cm, minimum height=2.6cm, aspect=1] at (1.5, 2.0) {};

    %% The relay nodes inside the Anonymity Network cloud.
    \node[relay] (r1) at (-0.1, 1.95)  {$R_{1}$};
    \node[relay] (r2) at (0.7, 2.5)    {$R_{2}$};
    \node[relay] (r3) at (1.3, 1.8)    {$R_{3}$};
    \node[relay] (r4) at (1.9, 2.4)    {$R_{4}$};
    \node[relay] (r5) at (2.8, 2.0)    {$R_{5}$};

    %% The Bridge Network cloud.
    \node[cloud, fill=cyan!40, cloud puffs=17, cloud puff arc=80, minimum width=5.5cm, minimum height=2.6cm, aspect=1] at (1.5, -2.0) {};

    %% The bridges inside the Bridge Network cloud.
    \node[bridge] (b1) at (-0.1, -2.1)   {$B_{1}$};
    \node[bridge] (b2) at (0.8, -1.65)   {$B_{2}$};
    \node[bridge] (b3) at (1.4, -2.1)    {$B_{3}$};
    \node[bridge] (b4) at (2.0, -2.6)    {$B_{4}$};
    \node[bridge] (b5) at (2.6, -1.7)    {$B_{5}$};

    %% Alice.
    \node[font=\small] at (-4, 1.5) {Alice};
    \node[alice, monitor, minimum size=1.2cm] (alice) at (-4, 0) {};

    %% Bob.
    \node[font=\small] at (4, 1.5) {Bob};
    \node[bob, mirrored, monitor, minimum size=1.2cm] (bob) at (4, 0) {};

    %% Alice connects to B2
    \path[thick, draw=black] (alice.base) edge (b2);

    %% B2 connects to R1
    \path[thick, draw=black] (b2) edge (r1);

    %% R1 connects to R4
    \path[thick, draw=black] (r1) edge (r4);

    %% R4 connects to Bob
    \path[thick, draw=black] (r4) edge (bob);

    %% Helper lines for debugging.
    %% \node[] at (0.0, 0.0) {X};
    %% \draw[help lines] (-7, -3) grid (7, 3);
\end{tikzpicture}

## Bridges

\vspace*{0.9cm}
\centering
\begin{tikzpicture}[overlay,scale=1.32]
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{bridge}=[circle, draw, thin, fill=cyan!80, text=white, font=\scriptsize, scale=0.8]

    %% Clip everything that is outside of our "viewport"
    \clip (-7, -3) rectangle (7, 3);

    %% Our censored area.
    \node[circle, draw=red!40, fill=red!5, thick, dashed, minimum width=50cm] (censored area) at (-20, 0) {};
    \node[font=\footnotesize\bfseries, align=center] at (-4, 2.5) {Censored Region};

    %% Alice.
    \node[font=\small] at (-4, 1.5) {Alice};
    \node[alice, monitor, minimum size=1.2cm] (alice) at (-4, 0) {};

    %% Bridge.
    \node[font=\small] at (4, 1.5) {Bridge};
    \node[bridge, minimum size=2.5cm] (bridge) at (4, 0) {};

    %% Alice connects to B2
    \draw[<->, thick, OnionDarkPurple!80] (-3.0, 0) -- (3.0, 0);

    %% Label.
    \node[] at (0, 0.2) {\small{Tor Protocol}};

    %% Helper lines for debugging.
    %% \node[] at (0.0, 0.0) {X};
    %% \draw[help lines] (-7, -3) grid (7, 3);
\end{tikzpicture}

## Bridges and Pluggable Transports

\vspace*{0.9cm}
\centering
\begin{tikzpicture}[overlay,scale=1.32]
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{bridge}=[circle, draw, thin, fill=cyan!80, text=white, font=\scriptsize, scale=0.8]
    \tikzstyle{pt}=[rectangle, draw, thin, fill=teal!80, text=white, font=\small, scale=0.8]

    %% Clip everything that is outside of our "viewport"
    \clip (-7, -3) rectangle (7, 3);

    %% Our censored area.
    \node[circle, draw=red!40, fill=red!5, thick, dashed, minimum width=50cm] (censored area) at (-20, 0) {};
    \node[font=\footnotesize\bfseries, align=center] at (-4, 2.5) {Censored Region};

    %% Alice.
    \node[font=\small] at (-4, 1.5) {Alice};
    \node[alice, monitor, minimum size=1.2cm] (alice) at (-4, 0) {};

    %% PT Client.
    \node[pt, minimum width=3.0cm, rounded corners] (pt client) at (-4, -2) {PT Client};

    %% Bridge.
    \node[font=\small] at (4, 1.5) {Bridge};
    \node[bridge, minimum size=2.5cm] (bridge) at (4, 0) {};

    %% PT Server.
    \node[pt, minimum width=3.0cm, rounded corners] (pt server) at (4, -2) {PT Server};

    %% PT Client connects to PT Server.
    \draw[<->, thick, teal!80] (-3.0, -2) -- (3.0, -2);

    %% Label.
    \node[] at (0, -1.8) {\small{Obfuscated Protocol}};

    %% Onion connection between Alice and the PT Client.
    \draw[<->, thick, OnionDarkPurple!80, shorten >= 0.3cm, shorten <= 0.3cm] (alice.south) -- (pt client);

    %% Onion connection between the PT server and the bridge.
    \draw[<->, thick, OnionDarkPurple!80, shorten >= 0.3cm, shorten <= 0.3cm] (pt server) -- (bridge);

    %% Helper lines for debugging.
    %% \node[] at (0.0, 0.0) {X};
    %% \draw[help lines] (-7, -3) grid (7, 3);
\end{tikzpicture}

## Pluggable Transports

- Allows people to easily build, experiment, and deploy their own obfuscation
  technology without having to modify the Tor source code itself.

- The specification for Pluggable Transports is open and allows other vendors
  to implement support for PTs in their own products.

- Allows people to experiment with different transports for Tor that might not
  be doing any anti-censorship related obfuscation.

## Obfourscator (obfs4)

- Does full x25519 handshakes, but uses Elligator2 to map elliptic curve points.
- Allows you to tune timers for traffic.
- Makes active probing hard unless the adversary knows the parameters of the given bridge.

## SNI Domain Fronting using Meek

\vspace*{0.9cm}
\centering
\begin{tikzpicture}[overlay,scale=1.32]
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{bridge}=[circle, draw, thin, fill=cyan!80, text=white, font=\scriptsize, scale=0.8]

    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{web}=[circle, draw, thin, fill=green!80, text=white, font=\scriptsize, scale=0.8]

    %% Define the style for our info boxes and their titles.
    \tikzstyle{box}=[rectangle, draw=black, fill=white, thick, font=\scriptsize\ttfamily, rounded corners, inner sep=10pt, inner ysep=10pt]
    \tikzstyle{box title}=[fill=black, text=white, font=\scriptsize\bfseries]

    %% Clip everything that is outside of our "viewport"
    \clip (-7, -3) rectangle (7, 3);

    %% Our censored area.
    \node[circle, draw=red!40, fill=red!5, thick, dashed, minimum width=50cm] (censored area) at (-20, 0) {};
    \node[font=\footnotesize\bfseries, align=center] at (-4, 2.5) {Censored Region};

    %% Alice.
    \node[font=\small] at (-4, 1.5) {Alice};
    \node[alice, monitor, minimum size=1.2cm] (alice) at (-4, 0) {};

    %% Our DNS box.
    \node[box] (dns query) at (0, 2) {%
        \begin{minipage}{0.35\textwidth}
            \textbf{A?} ajax.aspnetcdn.com
        \end{minipage}
    };

    %% Title for our DNS box.
    \node[box title, right=10pt] at (dns query.north west) {DNS};

    %% Our TLS box.
    \node[box, text depth=1cm] (tls) at (0, -1) {%
        \begin{minipage}{0.35\textwidth}
            \textbf{SNI:} ajax.aspnetcdn.com
        \end{minipage}
    };

    %% Title for our TLS box.
    \node[box title, right=10pt] at (tls.north west) {TLS};

    %% Our HTTP box
    \node[box] (http request) at (0, -2) {%
        \begin{minipage}{0.35\textwidth}
            POST / HTTP/1.1 \\
            Host: \textbf{meek.azureedge.net} \\ \ \\
            \ldots
        \end{minipage}
    };

    %% Title for our HTTP box.
    \node[box title, right=10pt] at (http request.north west) {HTTP};

    %% Bridge.
    \node[font=\small] at (4, 2.5) {Bridge};
    \node[bridge, minimum size=2.5cm] (bridge) at (4, 1.5) {};

    %% Web server.
    \node[font=\small] at (4, -2) {Webserver};
    \node[web, minimum size=2.5cm] (webserver) at (4, -1) {};

    %% Connection between Alice and the DNS box.
    \draw[<->, thick, bend right, shorten <= 0.4cm, shorten >= 0.4cm] (alice) -- (dns query);

    %% Connection between Alice and the TLS box.
    \draw[<-, thick, shorten <= 0.4cm] (alice) -- (tls);

    %% Connection between the TLS box and the webserver
    \draw[->, thick, shorten >= 0.4cm] (tls) -- (webserver);

    %% Onion connection between the webserver and the bridge.
    \draw[<->, thick, OnionDarkPurple!80, shorten >= 0.3cm, shorten <= 0.3cm] (webserver) -- (bridge);

    %% Helper lines for debugging.
    %% \node[] at (0.0, 0.0) {X};
    %% \draw[help lines] (-7, -3) grid (7, 3);
\end{tikzpicture}

## SNI Domain Fronting using Meek

Very \textbf{efficient}, but \textbf{expensive} \alert{:-(}

Unpopular with the cloud providers:

**Google**
  : Never been a supported feature of Google.

**Amazon**
  : Already handled as a breach of AWS ToS.

## Domain Fronting in the Future?

- Use Encrypted SNI?
- Using message queue services provided by the different cloud vendors?
- Generally continue to use centralized services to give people in censored areas access.

## Bridge Distribution {.c}

\centering
\includegraphics[width=0.6\textwidth]{images/bridgedb.png}

\tiny{Source: \href{https://bridges.torproject.org/}{bridges.torproject.org}}

## Bridge Distribution using Moat {.c}

\centering
\includegraphics[width=0.7\textwidth]{images/moat.png}

## Snowflake {.c}

\centering
\includegraphics[width=1.0\textwidth]{images/snowflake.png}

\tiny{Source: \href{https://snowflake.torproject.org/}{snowflake.torproject.org}}

## Snowflake {.c}

\centering
\includegraphics[width=1.0\textwidth]{images/snowflake_firefox.png}

## Tor is not foolproof

- Operational security mistakes.
- Browser metadata fingerprinting.
- Browser exploits.
- Traffic analysis.

## How can you help?

\begin{columns}
    \begin{column}{0.65\textwidth}
        \begin{itemize}
            \item Run a Tor relay or a bridge!
            \item Teach others about Tor and privacy in general.
            \item Find, and maybe fix, bugs in Tor.
            \item Test Tor on your platform of choice.
            \item Work on some of the many open research projects.
            \item Donate at \href{https://donate.torproject.org/}{donate.torproject.org}
        \end{itemize}
    \end{column}

    \begin{column}{0.35\textwidth}
        \begin{center}
            \includegraphics[width=0.95\textwidth]{images/tor_peace.png}
        \end{center}
    \end{column}
\end{columns}

## {.c .plain .noframenumbering}

\centering

\vfill

\huge{Questions?}

\vfill

\includegraphics[width=0.4\textwidth]{images/tor_bike.png}

## {.c .plain .noframenumbering}

\centering

This work is licensed under a

\large{\href{https://creativecommons.org/licenses/by-sa/4.0/}{Creative Commons \\ Attribution-ShareAlike 4.0 International License}}

\vfill

\ccbysa

\vfill
