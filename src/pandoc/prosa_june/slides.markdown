---
title: Introduction to The Tor Ecosystem
subtitle: Privacy, Anonymity, and Anti-censorship
date: June 13, 2019
author:
  - name: Alexander Færøy
slides:
    aspect-ratio: 169
    font-size: 14pt
    table-of-contents: false
---

## About Me

\begin{columns}
    \begin{column}{0.65\textwidth}
        \begin{itemize}[label=\textbullet]
            \item Core Developer at The Tor Project since February 2017.
            \item Free Software developer since 2006.
            \item Worked with distributed systems in the Erlang
                  programming language, mobile web browsers, consulting, and firmware
                  development.
            \item Co-organizing the annual Danish hacker festival
                  \href{https://bornhack.dk/}{BornHack}.
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
        \begin{itemize}[label=\textbullet]
            \item Online anonymity and censorship circumvention.
                \begin{itemize}[label=\textendash]
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

\begin{description}[align=parleft,labelwidth=3cm]
    \item [1990s]       Onion routing for privacy online.
    \item [Early 2000s] Working with the U.S. Naval Research Laboratory.
    \item [2004]        Sponsorship by the Electronic Frontier Foundation.
    \item [2006]        The Tor Project, Inc. became a non-profit.
    \item [2007]        Expansion to anti-censorship.
    \item [2008]        Tor Browser development.
    \item [2010]        The Arab spring.
    \item [2013]        The summer of Snowden.
    \item [2018]        Dedicated anti-censorship team created.
\end{description}

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

\begin{tikzpicture}[remember picture,overlay, background rectangle/.style={fill=OnionPurple}, show background rectangle]
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

\framesubtitle{The Data About Data}

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

## Different Purposes of Anonymity

\centering
\begin{tikzpicture}
    %% Our speech bubble
    \tikzstyle{speech bubble}=[ellipse callout, scale=0.85, draw, yshift=0.3cm, font=\scriptsize, align=center]

    %% The title above each person.
    \tikzstyle{title}=[font=\footnotesize\bfseries]

    %% Our arrow.
    \tikzstyle{arrow}=[->, thick, OnionDarkPurple!80, shorten >= 0.2cm, shorten <= 0.2cm]

    %% Anonymity in the center.
    \node[font=\bfseries] (anonymity) at (0, -0.5) {Anonymity};

    %% Man in black -- our government security person.
    \node[title] at (-3.5, 2.0) {Governments};
    \node[maninblack, mirrored, minimum size=1.0cm] (maninblack) at (-3.5, 1.0) {};
    \node[speech bubble, callout absolute pointer={(maninblack.mouth)}] at (-5.5, 1.0) {It's traffic-analysis \\ resistance!};

    %% Alice -- our human rights activist.
    \node[title] at (3.5, 2.0) {Human Rights Activists};
    \node[alice, minimum size=1.0cm] (alice) at (3.5, 1.0) {};
    \node[speech bubble, callout absolute pointer={(alice.mouth)}] at (5.5, 1.0) {It's reachability!};

    %% Physician -- our privacy concerned citizen.
    \node[title] at (-3.5, -1.0) {Private Citizens};
    \node[physician, mirrored, female, minimum size=1.0cm] (physician) at (-3.5, -2.0) {};
    \node[speech bubble, callout absolute pointer={(physician.mouth)}] at (-5.5, -2.0) {It's privacy!};

    %% Business man -- our business man who cares about security.
    \node[title] at (3.5, -1.0) {Businesses};
    \node[businessman, minimum size=1.0cm] (businessman) at (3.5, -2.0) {};
    \node[speech bubble, callout absolute pointer={(businessman.mouth)}] at (5.5, -2.0) {It's network \\ security!};

    %% Arrows.
    \draw[arrow] (anonymity) -- (maninblack);
    \draw[arrow] (anonymity) -- (alice);
    \draw[arrow] (anonymity) -- (physician);
    \draw[arrow] (anonymity) -- (businessman);

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

\begin{itemize}[label=\textbullet]
    \item An open network -- everybody can join!
    \item Between 6000 and 7000 relay nodes.
    \item Kindly hosted by various individuals, companies, and non-profit organisations.
    \item 9 Directory Authority nodes and 1 Bridge Authority node.
    \item What is the IPv6 story?
\end{itemize}

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

\begin{enumerate}[(1), itemsep=12pt]
    \item Diversity of relays. The more relays we have and the more diverse
          they are, the fewer attackers are in a position to do traffic confirmation. \\ \ \\

          Research problem: How do we measure diversity over time?

    \item Diversity of users and reasons to use it. 50000 users in Iran means
          almost all of them are normal citizens.
\end{enumerate}

##

\begin{tikzpicture}[overlay, remember picture]
    \node[anchor=center] at (current page.center) {
        \begin{minipage}[c]{0.85\textwidth}
            \small{\alert{\textbf{I'm a political activist, part of a semi-criminalized
            minority.}} In my younger years I entered the public debate openly, and as a
            result got harassed by government agencies. I later tried to obfuscate my
            identity, but I found that my government has surprisingly broad powers to track
            down dissidents. \\

            Only by using anonymizing means, among which Tor is key, can I get my
            message out without having police come to "check my papers" in the middle of
            the night. \alert{\textbf{Tor allows me freedom to publish my message to the world
            without being personally persecuted for it.}} \\

            Being a dissident is hard enough, privacy is already heavily curtailed, so
            anonymized communication is a godsend.}

            \begin{flushright}
                \footnotesize{---Anonymous Tor User.}
            \end{flushright}
        \end{minipage}
    };
\end{tikzpicture}

##

\begin{tikzpicture}[overlay, remember picture]
    \node[anchor=center] at (current page.center) {
        \begin{minipage}[c]{0.85\textwidth}
            \small{\alert{\textbf{I'm a doctor in a very political town.}} I have patients
            who work on legislation that can mean billions of dollars to major telecom,
            social media, and search concerns. \\

            When I have to do research on diseases and treatment or look into aspects of my
            patients' histories, I am well aware that my search histories might be
            correlated to patient visits and leak information about their health, families,
            and personal lives. \alert{\textbf{I use Tor to do much of my research when I
            think there is a risk of correlating it to patient visits.}}}

            \begin{flushright}
                \footnotesize{---Anonymous Tor User.}
            \end{flushright}
        \end{minipage}
    };
\end{tikzpicture}

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
            title=Number of Relays per Platform,
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

        \addlegendentry{Linux}
        \addplot table [x=date, y=linux, col sep=comma] {data/platforms.csv};

        \addlegendentry{BSD}
        \addplot table [x=date, y=bsd, col sep=comma] {data/platforms.csv};

        \addlegendentry{Windows}
        \addplot table [x=date, y=windows, col sep=comma] {data/platforms.csv};

        \addlegendentry{macOS}
        \addplot table [x=date, y=macos, col sep=comma] {data/platforms.csv};

        \addlegendentry{Other}
        \addplot table [x=date, y=other, col sep=comma] {data/platforms.csv};
    \end{axis}
\end{tikzpicture}

\tiny{Source: \href{https://metrics.torproject.org/}{metrics.torproject.org}}

## The Implementation of Tor

\begin{itemize}[label=\textbullet]
    \item The reference Tor implementation is written in the C programming
          language.
    \item Ongoing experiments with Mozilla’s Rust programming language.
    \item Follow best practices: high coverage for tests, integration tests,
          coverity, static code analysis, and code review policies.
    \item Specification and discussion before implementation. Specifications
          can be found at \href{https://gitweb.torproject.org/torspec.git}{gitweb.torproject.org/torspec}.
\end{itemize}

## {.c}

\centering
\vspace*{0.5cm}
\includegraphics[width=0.85\textwidth]{images/viva64.png}
\vspace*{0.5cm}

\tiny{Source: \href{https://www.viva64.com/en/b/0507/}{viva64.com}}

## Onion Services

\begin{itemize}[label=\textbullet]
    \item Allows servers to be anonymous.
    \item The ".onion" Special-Use Domain Name (RFC 7686).
    \item Introduced in Tor version 0.0.6pre1 from April, 2004.
    \item Traffic stays within the Tor network: No need to exit the network.
    \item Onion addresses are either 16 characters long (for version 2) or 52
          characters long (for version 3). \\ \ \\

          Research problem: How do we handle these long addresses?
\end{itemize}

## {.plain}

\begin{tikzpicture}[remember picture,overlay]
    \node[at=(current page.center)] {\includegraphics[width=\paperwidth, height=\paperheight]{images/tor_browser_torproject_org.png}};
\end{tikzpicture}

## Onion Services

Properties includes:

\begin{itemize}[label=\textbullet]
    \item Self authenticated.
    \item End-to-end encrypted.
    \item Isolation and NAT punching.
    \item Minimized attack surface.
    \item Support for Unix domain sockets.
\end{itemize}

## Onion Services

\centering
\begin{tikzpicture}
    \begin{axis}[
            title=Onion Services Bandwidth,
            title style={font=\scriptsize\bfseries},
            no markers,
            enlarge x limits=false,
            grid=both,
            grid style=dashed,
            width=0.85\paperwidth,
            height=0.80\paperheight,
            date coordinates in=x,
            xmin=2015-01-01,
            xmax=2019-01-01,
            xtick={
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

        \addplot table [x=date, y=relayed, col sep=comma] {data/hidserv-rend-relayed-cells.csv};
    \end{axis}
\end{tikzpicture}

\tiny{Source: \href{https://metrics.torproject.org/}{metrics.torproject.org}}

## {.t}

\centering
\begin{tikzpicture}
    \tikzstyle{venn}=[circle, minimum width=2.8cm]
    \tikzstyle{venn label}=[font=\footnotesize, align=center]
    \tikzstyle{venn arrow}=[->, thick, OnionDarkPurple!80, shorten >= 0.2cm]

    \begin{scope}[blend group = soft light]
        \node[venn, fill=OnionPurple!80!white]   (onion services circle)     at ( 90:0.15) {};
        \node[venn, fill=orange!80!white] (criminal activity circle)  at (210:0.15) {};
        \node[venn, fill=cyan!80!white]   (unindexed websites circle) at (330:0.15) {};
    \end{scope}

    \node[venn label] (x) at (0, 0) {Dark Web};

    \node[venn label] (onion services label)     at ( 150:5) {Onion services};
    \node[venn label] (criminal activity label)  at ( 210:5) {Online criminal activity};
    \node[venn label] (unindexed websites label) at ( 330:5) {Unindexed websites};

    \path[venn arrow, bend left] (onion services label) edge (onion services circle);
    \path[venn arrow, bend left] (criminal activity label) edge (criminal activity circle);
    \path[venn arrow, bend right] (unindexed websites label) edge (unindexed websites circle);

    \node[] (venn description) at (0, -5) {The "Dark Web" as popularly depicted.};

    %% \draw[help lines] (-5,-3) grid (5,5);
\end{tikzpicture}

## {.t}

\centering
\begin{tikzpicture}
    \tikzstyle{venn}=[circle, minimum width=2.8cm]
    \tikzstyle{venn label}=[font=\footnotesize, align=center]
    \tikzstyle{venn arrow}=[->, thick, OnionDarkPurple!80, shorten >= 0.2cm]

    \begin{scope}[blend group = soft light]
        \node[venn, fill=OnionPurple!80!white]   (onion services circle)     at ( 90:1.3) {};
        \node[venn, fill=orange!80!white] (criminal activity circle)  at (210:1.3) {};
        \node[venn, fill=cyan!80!white]   (unindexed websites circle) at (330:1.3) {};
    \end{scope}

    \node (x) at (0, 0) {};

    \node[venn label] (onion services label)     at ( 150:5) {Onion services};
    \node[venn label] (criminal activity label)  at ( 210:5) {Online criminal activity};
    \node[venn label] (unindexed websites label) at ( 330:5) {Unindexed websites};

    \path[venn arrow, bend right] (onion services label) edge (onion services circle);
    \path[venn arrow, bend left] (criminal activity label) edge (criminal activity circle);
    \path[venn arrow, bend right] (unindexed websites label) edge (unindexed websites circle);

    \node[] (venn description) at (0, -5) {Closer to reality.};

    %% \draw[help lines] (-5,-3) grid (5,5);
\end{tikzpicture}

## {.t}

\centering
\begin{tikzpicture}
    \tikzstyle{venn}=[circle, minimum width=2.8cm]
    \tikzstyle{venn label}=[font=\footnotesize, align=center]
    \tikzstyle{venn arrow}=[->, thick, OnionDarkPurple!80, shorten >= 0.2cm]

    \begin{scope}[blend group = soft light]
        \node[venn, fill=OnionPurple!80!white]   (onion services circle)     at ( 90:1.3) {};
        \node[venn, fill=orange!80!white] (criminal activity circle)  at (210:1.3) {};
        \node[venn, fill=cyan!80!white]   (unindexed websites circle) at (330:1.3) {};
    \end{scope}

    \node (x) at (0, 0) {};

    \node[venn label] (onion services label)     at ( 150:5) {Onion services};
    \node[venn label] (criminal activity label)  at ( 210:5) {Online criminal activity};
    \node[venn label] (unindexed websites label) at ( 330:5) {Unindexed websites};

    \path[venn arrow, bend right] (onion services label) edge (onion services circle);
    \path[venn arrow, bend left] (criminal activity label) edge (criminal activity circle);
    \path[venn arrow, bend right] (unindexed websites label) edge (unindexed websites circle);

    \node[font=\bfseries\small] (dark web) at (-4.5, 1.0) {Dark web?};
    \path[venn arrow, bend right, very thick, black] (dark web) edge (onion services circle);

    \node[] (venn description) at (0, -5) {Closer to reality.};

    %% \draw[help lines] (-5,-3) grid (5,5);
\end{tikzpicture}

## {.t}

\centering
\begin{tikzpicture}
    \tikzstyle{venn}=[circle, minimum width=2.8cm]
    \tikzstyle{venn label}=[font=\footnotesize, align=center]
    \tikzstyle{venn arrow}=[->, thick, OnionDarkPurple!80, shorten >= 0.2cm]

    \begin{scope}[blend group = soft light]
        \node[venn, fill=OnionPurple!80!white]   (onion services circle)     at ( 90:1.3) {};
        \node[venn, fill=orange!80!white] (criminal activity circle)  at (210:1.3) {};
        \node[venn, fill=cyan!80!white]   (unindexed websites circle) at (330:1.3) {};
    \end{scope}

    \node (x) at (0, 0) {};

    \node[venn label] (onion services label)     at ( 150:5) {Onion services};
    \node[venn label] (criminal activity label)  at ( 210:5) {Online criminal activity};
    \node[venn label] (unindexed websites label) at ( 330:5) {Unindexed websites};

    \path[venn arrow, bend right] (onion services label) edge (onion services circle);
    \path[venn arrow, bend left] (criminal activity label) edge (criminal activity circle);
    \path[venn arrow, bend right] (unindexed websites label) edge (unindexed websites circle);

    \node[font=\bfseries\small] (dark web) at (-4.5, -0.5) {Dark web?};
    \path[venn arrow, bend left, very thick, black] (dark web) edge (criminal activity circle);

    \node[] (venn description) at (0, -5) {Closer to reality.};

    %% \draw[help lines] (-5,-3) grid (5,5);
\end{tikzpicture}

## {.t}

\centering
\begin{tikzpicture}
    \tikzstyle{venn}=[circle, minimum width=2.8cm]
    \tikzstyle{venn label}=[font=\footnotesize, align=center]
    \tikzstyle{venn arrow}=[->, thick, OnionDarkPurple!80, shorten >= 0.2cm]

    \begin{scope}[blend group = soft light]
        \node[venn, fill=OnionPurple!80!white]   (onion services circle)     at ( 90:1.3) {};
        \node[venn, fill=orange!80!white] (criminal activity circle)  at (210:1.3) {};
        \node[venn, fill=cyan!80!white]   (unindexed websites circle) at (330:1.3) {};
    \end{scope}

    \node (x) at (0, 0) {};

    \node[venn label] (onion services label)     at ( 150:5) {Onion services};
    \node[venn label] (criminal activity label)  at ( 210:5) {Online criminal activity};
    \node[venn label] (unindexed websites label) at ( 330:5) {Unindexed websites};

    \path[venn arrow, bend right] (onion services label) edge (onion services circle);
    \path[venn arrow, bend left] (criminal activity label) edge (criminal activity circle);
    \path[venn arrow, bend right] (unindexed websites label) edge (unindexed websites circle);

    \node[font=\bfseries\small] (dark web) at (4.5, 1.5) {Dark web?};
    \path[venn arrow, bend right, very thick, black] (dark web) edge (unindexed websites circle);

    \node[] (venn description) at (0, -5) {Closer to reality.};

    %% \draw[help lines] (-5,-3) grid (5,5);
\end{tikzpicture}

## {.t}

\centering
\begin{tikzpicture}
    \tikzstyle{venn}=[circle, minimum width=2.8cm]
    \tikzstyle{venn label}=[font=\footnotesize, align=center]
    \tikzstyle{venn arrow}=[->, thick, OnionDarkPurple!80, shorten >= 0.2cm]

    \begin{scope}[blend group = soft light]
        \node[venn, fill=OnionPurple!80!white]   (onion services circle)     at ( 90:1.3) {};
        \node[venn, fill=orange!80!white] (criminal activity circle)  at (210:1.3) {};
        \node[venn, fill=cyan!80!white]   (unindexed websites circle) at (330:1.3) {};
    \end{scope}

    \node (x) at (0, 0) {};

    \node[venn label] (onion services label)     at ( 150:5) {Onion services};
    \node[venn label] (criminal activity label)  at ( 210:5) {Online criminal activity};
    \node[venn label] (unindexed websites label) at ( 330:5) {Unindexed websites};

    \path[venn arrow, bend right] (onion services label) edge (onion services circle);
    \path[venn arrow, bend left] (criminal activity label) edge (criminal activity circle);
    \path[venn arrow, bend right] (unindexed websites label) edge (unindexed websites circle);

    \node[font=\bfseries\small] (dark web) at (4.5, 2.0) {Dark web?};
    \path[venn arrow, bend right, very thick, black, shorten >= 0.0cm] (dark web) edge (x);

    \node[] (venn description) at (0, -5) {Closer to reality.};

    %% \draw[help lines] (-5,-3) grid (5,5);
\end{tikzpicture}

## {.t}

\centering
\begin{tikzpicture}
    \tikzstyle{venn}=[circle, minimum width=2.8cm]
    \tikzstyle{venn label}=[font=\footnotesize, align=center]
    \tikzstyle{venn arrow}=[->, thick, OnionDarkPurple!80, shorten >= 0.2cm]

    \begin{scope}[blend group = soft light]
        \node[venn, fill=OnionPurple!80!white, minimum width=0.2cm] (onion services circle) at ( 90:0.3) {};
        \node[venn, fill=orange!80!white] (criminal activity circle)  at (210:1.3) {};
        \node[venn, fill=cyan!80!white]   (unindexed websites circle) at (330:1.3) {};
    \end{scope}

    \node (x) at (0, 0) {};

    \node[venn label] (onion services label)     at ( 150:5) {Onion services};
    \node[venn label] (criminal activity label)  at ( 210:5) {Online criminal activity};
    \node[venn label] (unindexed websites label) at ( 330:5) {Unindexed websites};

    \path[venn arrow, bend right] (onion services label) edge (onion services circle);
    \path[venn arrow, bend left] (criminal activity label) edge (criminal activity circle);
    \path[venn arrow, bend right] (unindexed websites label) edge (unindexed websites circle);

    \node[font=\bfseries\small] (dark web) at (4.5, 2.0) {Dark web?};
    \path[venn arrow, bend right, very thick, black, shorten >= 0.0cm] (dark web) edge (x);

    \node[] (venn description) at (0, -5) {Scale also matters.};

    %% \draw[help lines] (-5,-3) grid (5,5);
\end{tikzpicture}

## {.plain}

\begin{tikzpicture}[remember picture,overlay]
    \node[at=(current page.center)] {\includegraphics[width=\paperwidth, height=\paperheight]{images/facebookonion.png}};
\end{tikzpicture}

## {.c}

\centering
\vspace*{1.0cm}

\includegraphics[width=0.9\textwidth]{images/facebook_tor_news.png}

\vspace*{1.2cm}

\tiny{Source: \href{https://facebook.com/notes/facebook-over-tor/1-million-people-use-facebook-over-tor/865624066877648/}{facebook.com}}

## SecureDrop {.c}


\centering
\includegraphics[width=0.4\textwidth]{images/securedrop.png}

## OnionShare {.c}

\centering
\includegraphics[width=0.4\textwidth]{images/onionshare.png}

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

## {.plain}

\begin{tikzpicture}[remember picture,overlay]
    \node[at=(current page.center)] {\includegraphics[width=\paperwidth, height=\paperheight]{images/block_result.png}};
\end{tikzpicture}

## {.plain}

\begin{tikzpicture}[remember picture,overlay]
    \node[at=(current page.center)] {\includegraphics[width=\paperwidth, height=\paperheight]{images/tdc_dk_block.png}};
\end{tikzpicture}

## {.plain .c}

\centering
\includegraphics[width=0.8\textwidth]{images/iran_graph.png}

## Anti-censorship Strategies

\begin{itemize}[label=\textbullet]
    \item Censors will apply censorship to  nodes in the network.
    \item Same for known bridges.
    \item Solution: either make it hard to analyze the traffic or make it hard to block the bridges.
\end{itemize}

## Pluggable Transports {.c}

\centering
\includegraphics[width=0.9\textwidth]{images/pt.png}

## Obfourscator (obfs4)

\begin{itemize}[label=\textbullet]
    \item Does full x25519 handshakes, but uses Elligator2 to map elliptic curve points.
    \item Allows you to tune timers for traffic.
\end{itemize}

## Meek

\begin{itemize}[label=\textbullet]
    \item Connect with TLS with SNI set to some large user of the cloud provider.
    \item Inside your TLS connection you do a normal HTTP request, but with the Host header set to the server you want to reach inside the cloud.
    \item Efficient, but expensive :-(
\end{itemize}

## Domain Fronting

\begin{itemize}[label=\textbullet]
    \item Using ESNI?
    \item Using various cloud providers message queue services?
    \item Generally using large centralized services to give access to censored people.
\end{itemize}

## Snowflake {.c}

\centering
\includegraphics[width=1.0\textwidth]{images/snowflake.png}

## {.plain .noframenumbering}

%% FIXME(ahf): Remove text from ooni_probe.png and replace it with Tikz.

\centering
\begin{tikzpicture}[remember picture,overlay, background rectangle/.style={fill=OONIBlue}, show background rectangle]
    \node[text=white, at=(current page.north), yshift=-0.7cm, font=\Large\bfseries] {Open Observatory of Network Interference};
    \node[at=(current page.center)] {\includegraphics[width=\paperwidth]{images/ooni_probe.png}};
\end{tikzpicture}

## {.c}

\begin{tikzpicture}[remember picture,overlay, background rectangle/.style={fill=white}, show background rectangle]
    \node[at=(current page.center)] {\includegraphics[scale=0.80]{images/ooni_probe_android.png}};
\end{tikzpicture}

## {.b}

\centering
\begin{tikzpicture}[remember picture,overlay]
    \node[at=(current page.north), yshift=-3.3cm] {\includegraphics[width=\paperwidth]{images/ooni_explorer.png}};
\end{tikzpicture}

Check it out at \href{https://explorer.ooni.io/}{explorer.ooni.io}

## Tor is not foolproof

\begin{itemize}[label=\textbullet]
    \item Operational security mistakes.
    \item Browser metadata fingerprinting.
    \item Browser exploits.
    \item Traffic analysis.
\end{itemize}

## How can you help?

\begin{columns}
    \begin{column}{0.65\textwidth}
        \begin{itemize}[label=\textbullet]
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
