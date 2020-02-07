---
title: An Introduction to the Tor Ecosystem for Developers
date: February 2, 2020
institute: FOSDEM
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

**Early 2000s**
  : Working with the U.S. Naval Research Laboratory.

**2004**
  : Sponsorship by the Electronic Frontier Foundation.

**2006**
  : The Tor Project, Inc. became a non-profit.

**2008**
  : Tor Browser development.

**2010**
  : The Arab spring.

**2013**
  : The summer of Snowden.

**2018**
  : Anti-censorship team created.

**2019**
  : Tor Browser for Android released.

**2020**
  : Network Health team created.

## {.plain}

\tikzset{external/export next=false}
\begin{tikzpicture}[remember picture, overlay, background rectangle/.style={fill=OnionDarkPurple}, show background rectangle]
    \node[text=white, at=(current page.north), yshift=-2.5cm, font=\bfseries] {Somewhere between 2,000,000 and 8,000,000 daily users.};
    \node[at=(current page.center), yshift=-2.5cm, align=center] {\input{images/tor_group.tex}};
\end{tikzpicture}

## {.plain}

\tikzset{external/export next=false}
\begin{tikzpicture}[remember picture,overlay, background rectangle/.style={fill=OnionDarkPurple}, show background rectangle]
    \node[at=(current page.center)] {\includegraphics[scale=0.25]{images/tor_browser.png}};
\end{tikzpicture}

## {.plain}

\tikzset{external/export next=false}
\begin{tikzpicture}[remember picture,overlay, background rectangle/.style={fill=OnionDarkPurple}, show background rectangle]
    \node[at=(current page.center)] {\includegraphics[scale=0.20]{images/tor_browser_android.png}};
\end{tikzpicture}

## {.plain}

But we also ship Tor to others:

\begin{itemize}
    \item We have our own Debian mirror on \href{https://deb.torproject.org/}{deb.torproject.org}.
    \item Other free software distributions. This is often where the relay operators get their Tor version from.
    \item Brave's "Private Tab" feature uses Tor.
    \item OnionShare, SecureDrop, etc.
\end{itemize}

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
            xmax=2020-01-01,
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
                {2019-01-01},
                {2020-01-01}
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

\tiny Source: \href{https://metrics.torproject.org/}{metrics.torproject.org}

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
            xmax=2020-01-01,
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
                {2019-01-01},
                {2020-01-01}
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

\tiny Source: \href{https://metrics.torproject.org/}{metrics.torproject.org}

## The Tor Network

Tor's **safety** comes from **diversity**:

1. Diversity of relays. The more relays we have and the more diverse
   they are, the fewer attackers are in a position to do traffic confirmation.

2. Diversity of users and reasons to use it. 50,000 users in Iran means
   almost all of them are normal citizens.

**Research problem**: How do we measure diversity over time?

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
            xmax=2020-01-01,
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
                {2019-01-01},
                {2020-01-01}
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

\tiny Source: \href{https://metrics.torproject.org/}{metrics.torproject.org}

## {.c .noframenumbering}

\vspace*{0.9cm}
\centering
\tikzset{external/export next=false}
\begin{tikzpicture}[overlay,scale=1.32]
    %% Clip everything that is outside of our "viewport"
    \clip (-7, -3) rectangle (7, 3);

    %% Trac Logo.
    \node[] at (0, 0) {
        \includegraphics[width=8cm]{images/trac_logo.png}
    };

    %% Trac URL
    \node[] at (0, -2) {
        \url{https://trac.torproject.org/}
    };

    %% Helper lines for debugging.
    % \node[] at (0.0, 0.0) {X};
    % \draw[help lines] (-7, -3) grid (7, 3);
\end{tikzpicture}

## {.c .noframenumbering}

\vspace*{0.9cm}
\centering
\tikzset{external/export next=false}
\begin{tikzpicture}[overlay,scale=1.32]
    %% Clip everything that is outside of our "viewport"
    \clip (-7, -3) rectangle (7, 3);

    %% Trac Logo.
    \node[] at (-3, 0) {
        \includegraphics[width=6cm]{images/trac_logo.png}
    };

    %% Gitlab Logo.
    \node[] at (3, 0) {
        \includegraphics[height=5cm]{images/gitlab_logo.png}
    };

    %% Arrow.
    \draw[OnionPurple, ultra thick, ->] (-0.75, 0) -- (0.75, 0);

    %% Helper lines for debugging.
    % \node[] at (0.0, 0.0) {X};
    % \draw[help lines] (-7, -3) grid (7, 3);
\end{tikzpicture}


## Network Team {.c}

The team dedicated to develop and maintain the "Tor" codebase.

Internally, we often refer to "Tor" as "little-t-tor".

Deal with everything that "impacts the network".

## Network Team

- The reference Tor implementation is written in C.
- Ongoing experiments with Mozilla’s Rust programming language.
- Follow best practices: high coverage for tests, integration tests, coverity,
  static code analysis, and code review policies.
- The team is responsible for: feature development, code reviews, auditing, working with downstream projects (Tor Browser and distro packagers), and specification design and implementation.

## {.c}

\centering
\vspace*{0.5cm}
\includegraphics[width=0.85\textwidth]{images/viva64.png}
\vspace*{0.5cm}

\tiny Source: \href{https://www.viva64.com/en/b/0507/}{viva64.com}

## Tor Releases {.c}

\centering

\small\begin{tabular}{lllll}
\toprule
\textbf{Version} & \textbf{Merge Window} & \textbf{Feature Freeze} & \textbf{Release} & \textbf{End of Life} \\
\midrule
0.3.5 (\alert{LTS}) &  15/6/2018 & 15/9/2018 &  7/1/2019 &  1/2/2022 \\
0.4.0               & 15/10/2018 & 15/1/2019 &  2/5/2019 &  \textbf{2/2/2020} \\
0.4.1               &  15/2/2018 & 15/5/2019 & 20/8/2019 & 20/5/2020 \\
0.4.2               &  10/6/2019 & 15/9/2019 & 9/12/2019 & 15/9/2022 \\
0.4.3               & 11/10/2019 & 15/1/2020 & 15/4/2020 & TBD       \\
\midrule
0.4.4               &  15/2/2020 & 15/5/2020 & 15/8/2020  & TBD      \\
0.4.5               &  15/6/2020 & 15/9/2020 & 15/12/2020 & TBD      \\
\hline
\end{tabular}

## Contributing to Tor

\begin{enumerate}
    \item Find a ticket on \url{https://trac.torproject.org/} that you are interested in hacking on.
    \item Hack on it until you think it's time to share your work.
    \item Ensure that tests and various other code requirements are satisfied using \texttt{make check}.
    \item Write a "changes" file.
    \item Open a PR on \url{https://github.com/torproject/tor} and await review.
\end{enumerate}

## Contributing to Tor

- For "upfront CI" we use a mixture of Travis and AppVeyor. This covers (some
  of) Linux, macOS, and Windows.
- Once a patch lands, we have a setup of Jenkins builder too.
- Check whether "changes" file is included, whether functions become overly complex, etc.

## Contributing to Tor

Protocol changes require a specification proposal and discussion before
implementation.

Specifications can be found at
\href{https://gitweb.torproject.org/torspec.git}{gitweb.torproject.org/torspec}.

## Bandwidth Scanning {.c}

\centering
\begin{tikzpicture}
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{relay}=[circle, draw, thin, fill=OnionDarkPurple!80, text=white, font=\scriptsize, scale=0.8]
    \tikzstyle{web}=[circle, draw, thin, fill=green!80, text=white, font=\scriptsize, scale=0.8]
    \tikzstyle{scanner}=[circle, draw, thin, fill=cyan!80, text=white, font=\scriptsize, scale=0.8]

    %% The Anonymity Network cloud.
    \node[] at (0, 2) {The Tor Network};
    \node[cloud, fill=OnionPurple!40, cloud puffs=16, cloud puff arc=100, minimum width=5.5cm, minimum height=2.6cm, aspect=1] at (0,0) {};

    %% The relay nodes inside the Anonymity Network cloud.
    \node[relay] (e1) at (0.0, 0.1)   {$E_{1}$};

    \node[relay] (r1) at (-1.9, -0.1)  {$R_{1}$};
    \node[relay] (r3) at (1.8, -0.4)  {$R_{3}$};
    \node[relay] (r4) at (-0.7, 0.7)  {$R_{4}$};
    \node[relay] (r5) at (-1.0, -0.7) {$R_{5}$};
    \node[relay] (r6) at (0.8, -0.6)  {$R_{6}$};
    \node[relay] (r2) at (1.2, 0.5)   {$R_{2}$};

    %% Web server.
    \node[font=\small] at (5, 1.5) {Webserver};
    \node[web, minimum size=2cm] (webserver) at (5, 0) {};

    %% BW Scanner.
    \node[font=\small] at (-5, 1.5) {Bandwidth Scanner};
    \node[scanner, minimum size=2cm] (bwscanner) at (-5, 0) {};

    %% Lines
    \draw[ultra thick] (bwscanner) -- (r1);
    \draw[ultra thick] (r1) -- (e1);
    \draw[ultra thick] (e1) -- (webserver);

    %% Helper lines for debugging.
    % \draw[help lines] (-7,-3) grid (7,3);
\end{tikzpicture}

## Bandwidth Scanning {.c}

\centering
\begin{tikzpicture}
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{relay}=[circle, draw, thin, fill=OnionDarkPurple!80, text=white, font=\scriptsize, scale=0.8]
    \tikzstyle{web}=[circle, draw, thin, fill=green!80, text=white, font=\scriptsize, scale=0.8]
    \tikzstyle{scanner}=[circle, draw, thin, fill=cyan!80, text=white, font=\scriptsize, scale=0.8]

    %% The Anonymity Network cloud.
    \node[] at (0, 2) {The Tor Network};
    \node[cloud, fill=OnionPurple!40, cloud puffs=16, cloud puff arc=100, minimum width=5.5cm, minimum height=2.6cm, aspect=1] at (0,0) {};

    %% The relay nodes inside the Anonymity Network cloud.
    \node[relay] (e1) at (0.0, 0.1)   {$E_{1}$};

    \node[relay] (r1) at (-1.9, -0.1)  {$R_{1}$};
    \node[relay] (r3) at (1.8, -0.4)  {$R_{3}$};
    \node[relay] (r4) at (-0.7, 0.7)  {$R_{4}$};
    \node[relay] (r5) at (-1.0, -0.7) {$R_{5}$};
    \node[relay] (r6) at (0.8, -0.6)  {$R_{6}$};
    \node[relay] (r2) at (1.2, 0.5)   {$R_{2}$};

    %% Web server.
    \node[font=\small] at (5, 1.5) {Webserver};
    \node[web, minimum size=2cm] (webserver) at (5, 0) {};

    %% BW Scanner.
    \node[font=\small] at (-5, 1.5) {Bandwidth Scanner};
    \node[scanner, minimum size=2cm] (bwscanner) at (-5, 0) {};

    %% Lines
    \draw[ultra thick] (bwscanner) -- (r5);
    \draw[ultra thick] (r5) -- (e1);
    \draw[ultra thick] (e1) -- (webserver);

    %% Helper lines for debugging.
    % \draw[help lines] (-7,-3) grid (7,3);
\end{tikzpicture}

## Bandwidth Scanning {.c}

\centering
\begin{tikzpicture}
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{relay}=[circle, draw, thin, fill=OnionDarkPurple!80, text=white, font=\scriptsize, scale=0.8]
    \tikzstyle{web}=[circle, draw, thin, fill=green!80, text=white, font=\scriptsize, scale=0.8]
    \tikzstyle{scanner}=[circle, draw, thin, fill=cyan!80, text=white, font=\scriptsize, scale=0.8]

    %% The Anonymity Network cloud.
    \node[] at (0, 2) {The Tor Network};
    \node[cloud, fill=OnionPurple!40, cloud puffs=16, cloud puff arc=100, minimum width=5.5cm, minimum height=2.6cm, aspect=1] at (0,0) {};

    %% The relay nodes inside the Anonymity Network cloud.
    \node[relay] (e1) at (0.0, 0.1)   {$E_{1}$};

    \node[relay] (r1) at (-1.9, -0.1)  {$R_{1}$};
    \node[relay] (r3) at (1.8, -0.4)  {$R_{3}$};
    \node[relay] (r4) at (-0.7, 0.7)  {$R_{4}$};
    \node[relay] (r5) at (-1.0, -0.7) {$R_{5}$};
    \node[relay] (r6) at (0.8, -0.6)  {$R_{6}$};
    \node[relay] (r2) at (1.2, 0.5)   {$R_{2}$};

    %% Web server.
    \node[font=\small] at (5, 1.5) {Webserver};
    \node[web, minimum size=2cm] (webserver) at (5, 0) {};

    %% BW Scanner.
    \node[font=\small] at (-5, 1.5) {Bandwidth Scanner};
    \node[scanner, minimum size=2cm] (bwscanner) at (-5, 0) {};

    %% Lines
    \draw[ultra thick] (bwscanner) -- (r4);
    \draw[ultra thick] (r4) -- (e1);
    \draw[ultra thick] (e1) -- (webserver);

    %% Helper lines for debugging.
    % \draw[help lines] (-7,-3) grid (7,3);
\end{tikzpicture}

## Simple Bandwidth Scanner

\begin{itemize}
    \item Bandwidth Scanner implemented in the Python programming language.
    \item Well-documented internals.
    \item Used by 3 out of 6 of the Directory Authorities that use input from Bandwidth Scanners.
    \item Could benefit from more contributors \alert{:-)}
    \item Written by juga0, Matt Traudt, and teor.
\end{itemize}

\centering
\large
\url{https://sbws.readthedocs.io/}

## Anti-censorship Team

\begin{itemize}
    \item New team created in early 2019 to handle all anti-censorship work
          that was previously handled by the network team.
    \item Develops and maintains the Pluggable Transports that are shipped with in Tor Browser.
    \item Focus on Snowflake, BridgeDB, and Gettor.
\end{itemize}

## {.plain}

\tikzset{external/export next=false}
\begin{tikzpicture}[remember picture,overlay]
    \node[at=(current page.center)] {\includegraphics[width=\paperwidth, height=\paperheight]{images/block_result.png}};
\end{tikzpicture}

## Pluggable Transports

\vspace*{0.9cm}
\centering
\tikzset{external/export next=false}
\begin{tikzpicture}[overlay,scale=1.32]
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{bridge}=[circle, draw, thin, fill=OnionPurple, text=white, font=\scriptsize, scale=0.8]
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
    \node[font=\small] at (4, 1.5) {Bridge Relay};
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

## BridgeDB {.c}

\centering
\includegraphics[width=0.6\textwidth]{images/bridgedb.png}

\tiny Source: \href{https://bridges.torproject.org/}{bridges.torproject.org}

## BridgeDB access via Moat {.c}

\centering
\includegraphics[width=0.7\textwidth]{images/moat.png}

## Snowflake {.c}

\vspace*{0.9cm}
\centering
\tikzset{external/export next=false}
\begin{tikzpicture}[overlay,scale=1.32]
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{bridge}=[circle, draw, thin, fill=cyan!80, text=white, font=\scriptsize, scale=0.8]
    \tikzstyle{pt}=[rectangle, draw, thin, fill=teal!80, text=white, font=\small, scale=0.8]
    \tikzstyle{broker}=[rectangle, draw, rounded corners, thin, fill=orange!80, text=white, font=\small, scale=0.8]

    %% Clip everything that is outside of our "viewport"
    \clip (-7, -3) rectangle (7, 3);

    %% Our censored area.
    \node[circle, draw=red!40, fill=red!5, thick, dashed, minimum width=50cm] (censored area) at (-20, 0) {};
    \node[font=\footnotesize\bfseries, align=center] at (-4, 2.5) {Censored Region};

    %% Alice.
    \node[font=\small] at (-4, 1.5) {Alice};
    \node[alice, monitor, minimum size=1.2cm] (alice) at (-4, 0) {};

    %% Snowflake PT Client.
    \node[pt, minimum width=3.5cm, rounded corners] (snowflake client) at (-4, -2) {Snowflake PT Client};

    %% Snowflake PT Server.
    \node[pt, minimum width=3.5cm, rounded corners] (snowflake server) at (4, -2) {Snowflake PT Server};

    %% Bridge.
    \node[font=\small] at (4, 1.5) {Bridge};
    \node[bridge, minimum size=2.5cm] (bridge) at (4, 0) {};

    %% Broker.
    \node[broker, minimum width=3cm, minimum height=1.2cm] (snowflake broker) at (0, 1.85) {Snowflake Broker};

    %% Onion connection between Alice and the Snowflake PT Client.
    \draw[<->, thick, OnionDarkPurple!80, shorten >= 0.3cm, shorten <= 0.3cm] (alice.south) -- (snowflake client);

    %% Onion connection between the Snowflake PT server and the bridge.
    \draw[<->, thick, OnionDarkPurple!80, shorten >= 0.3cm, shorten <= 0.3cm] (snowflake server) -- (bridge);

    %% Snowflake
    \node[] (snowflake proxy) at (0, -2) {\includegraphics[angle=0, origin=c]{images/snowflake-status.png}};

    %% Random snowflakes.
    \node[scale=0.53] at (1.4, -1)  {\includegraphics[angle=37, origin=c]{images/snowflake-status.png}};
    \node[scale=0.65] at (1.9, 0)   {\includegraphics[angle=67, origin=c]{images/snowflake-status.png}};
    \node[scale=0.50] at (2.4, 0.9) {\includegraphics[angle=23, origin=c]{images/snowflake-status.png}};
    \node[scale=0.55] at (0.95, 0.67)   {\includegraphics[angle=17, origin=c]{images/snowflake-status.png}};

    %% Helper lines for debugging.
    %% \node[] at (0.0, 0.0) {X};
    %% \draw[help lines] (-7, -3) grid (7, 3);
\end{tikzpicture}

## Snowflake {.c}

\vspace*{0.9cm}
\centering
\tikzset{external/export next=false}
\begin{tikzpicture}[overlay,scale=1.32]
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{bridge}=[circle, draw, thin, fill=cyan!80, text=white, font=\scriptsize, scale=0.8]
    \tikzstyle{pt}=[rectangle, draw, thin, fill=teal!80, text=white, font=\small, scale=0.8]
    \tikzstyle{broker}=[rectangle, draw, rounded corners, thin, fill=orange!80, text=white, font=\small, scale=0.8]

    %% Clip everything that is outside of our "viewport"
    \clip (-7, -3) rectangle (7, 3);

    %% Our censored area.
    \node[circle, draw=red!40, fill=red!5, thick, dashed, minimum width=50cm] (censored area) at (-20, 0) {};
    \node[font=\footnotesize\bfseries, align=center] at (-4, 2.5) {Censored Region};

    %% Alice.
    \node[font=\small] at (-4, 1.5) {Alice};
    \node[alice, monitor, minimum size=1.2cm] (alice) at (-4, 0) {};

    %% Snowflake PT Client.
    \node[pt, minimum width=3.5cm, rounded corners] (snowflake client) at (-4, -2) {Snowflake PT Client};

    %% Snowflake PT Server.
    \node[pt, minimum width=3.5cm, rounded corners] (snowflake server) at (4, -2) {Snowflake PT Server};

    %% Bridge.
    \node[font=\small] at (4, 1.5) {Bridge};
    \node[bridge, minimum size=2.5cm] (bridge) at (4, 0) {};

    %% Broker.
    \node[broker, minimum width=3cm, minimum height=1.2cm] (snowflake broker) at (0, 1.85) {Snowflake Broker};

    %% Onion connection between Alice and the Snowflake PT Client.
    \draw[<->, thick, OnionDarkPurple!80, shorten >= 0.3cm, shorten <= 0.3cm] (alice.south) -- (snowflake client);

    %% Onion connection between the Snowflake PT server and the bridge.
    \draw[<->, thick, OnionDarkPurple!80, shorten >= 0.3cm, shorten <= 0.3cm] (snowflake server) -- (bridge);

    %% Snowflake
    \node[] (snowflake proxy) at (0, -2) {\includegraphics[angle=0, origin=c]{images/snowflake-status.png}};

    %% Arrow between the Snowflake proxy and the broker.
    \draw[<->, thick, teal!80, shorten >= 0.3cm, shorten <= 0.3cm] (snowflake broker.south) -- (snowflake proxy.north);

    %% Helper lines for debugging.
    %% \node[] at (0.0, 0.0) {X};
    %% \draw[help lines] (-7, -3) grid (7, 3);
\end{tikzpicture}

## Snowflake {.c}

\vspace*{0.9cm}
\centering
\tikzset{external/export next=false}
\begin{tikzpicture}[overlay,scale=1.32]
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{bridge}=[circle, draw, thin, fill=cyan!80, text=white, font=\scriptsize, scale=0.8]
    \tikzstyle{pt}=[rectangle, draw, thin, fill=teal!80, text=white, font=\small, scale=0.8]
    \tikzstyle{broker}=[rectangle, draw, rounded corners, thin, fill=orange!80, text=white, font=\small, scale=0.8]

    %% Clip everything that is outside of our "viewport"
    \clip (-7, -3) rectangle (7, 3);

    %% Our censored area.
    \node[circle, draw=red!40, fill=red!5, thick, dashed, minimum width=50cm] (censored area) at (-20, 0) {};
    \node[font=\footnotesize\bfseries, align=center] at (-4, 2.5) {Censored Region};

    %% Alice.
    \node[font=\small] at (-4, 1.5) {Alice};
    \node[alice, monitor, minimum size=1.2cm] (alice) at (-4, 0) {};

    %% Snowflake PT Client.
    \node[pt, minimum width=3.5cm, rounded corners] (snowflake client) at (-4, -2) {Snowflake PT Client};

    %% Snowflake PT Server.
    \node[pt, minimum width=3.5cm, rounded corners] (snowflake server) at (4, -2) {Snowflake PT Server};

    %% Bridge.
    \node[font=\small] at (4, 1.5) {Bridge};
    \node[bridge, minimum size=2.5cm] (bridge) at (4, 0) {};

    %% Broker.
    \node[broker, minimum width=3cm, minimum height=1.2cm] (snowflake broker) at (0, 1.85) {Snowflake Broker};

    %% Onion connection between Alice and the Snowflake PT Client.
    \draw[<->, thick, OnionDarkPurple!80, shorten >= 0.3cm, shorten <= 0.3cm] (alice.south) -- (snowflake client);

    %% Onion connection between the Snowflake PT server and the bridge.
    \draw[<->, thick, OnionDarkPurple!80, shorten >= 0.3cm, shorten <= 0.3cm] (snowflake server) -- (bridge);

    %% Snowflake
    \node[] (snowflake proxy) at (0, -2) {\includegraphics[angle=0, origin=c]{images/snowflake-status.png}};

    %% Arrow between the Snowflake proxy and the broker.
    \draw[<->, thick, teal!80, shorten >= 0.3cm, shorten <= 0.3cm] (snowflake broker.south) -- (snowflake proxy.north);

    %% Arrow between the PT client and the broker.
    \draw[<->, thick, teal!80, shorten >= 0.3cm, shorten <= 0.3cm, bend right] (snowflake client.east) -- (snowflake broker.south west);

    %% Helper lines for debugging.
    %% \node[] at (0.0, 0.0) {X};
    %% \draw[help lines] (-7, -3) grid (7, 3);
\end{tikzpicture}

## Snowflake {.c}

\vspace*{0.9cm}
\centering
\tikzset{external/export next=false}
\begin{tikzpicture}[overlay,scale=1.32]
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{bridge}=[circle, draw, thin, fill=cyan!80, text=white, font=\scriptsize, scale=0.8]
    \tikzstyle{pt}=[rectangle, draw, thin, fill=teal!80, text=white, font=\small, scale=0.8]
    \tikzstyle{broker}=[rectangle, draw, rounded corners, thin, fill=orange!80, text=white, font=\small, scale=0.8]

    %% Clip everything that is outside of our "viewport"
    \clip (-7, -3) rectangle (7, 3);

    %% Our censored area.
    \node[circle, draw=red!40, fill=red!5, thick, dashed, minimum width=50cm] (censored area) at (-20, 0) {};
    \node[font=\footnotesize\bfseries, align=center] at (-4, 2.5) {Censored Region};

    %% Alice.
    \node[font=\small] at (-4, 1.5) {Alice};
    \node[alice, monitor, minimum size=1.2cm] (alice) at (-4, 0) {};

    %% Snowflake PT Client.
    \node[pt, minimum width=3.5cm, rounded corners] (snowflake client) at (-4, -2) {Snowflake PT Client};

    %% Snowflake PT Server.
    \node[pt, minimum width=3.5cm, rounded corners] (snowflake server) at (4, -2) {Snowflake PT Server};

    %% Bridge.
    \node[font=\small] at (4, 1.5) {Bridge};
    \node[bridge, minimum size=2.5cm] (bridge) at (4, 0) {};

    %% Broker.
    \node[broker, minimum width=3cm, minimum height=1.2cm] (snowflake broker) at (0, 1.85) {Snowflake Broker};

    %% Onion connection between Alice and the Snowflake PT Client.
    \draw[<->, thick, OnionDarkPurple!80, shorten >= 0.3cm, shorten <= 0.3cm] (alice.south) -- (snowflake client);

    %% Onion connection between the Snowflake PT server and the bridge.
    \draw[<->, thick, OnionDarkPurple!80, shorten >= 0.3cm, shorten <= 0.3cm] (snowflake server) -- (bridge);

    %% Snowflake
    \node[] (snowflake proxy) at (0, -2) {\includegraphics[angle=0, origin=c]{images/snowflake-status.png}};

    %% Arrow between the Snowflake PT client and the proxy.
    \draw[<->, thick, cyan!80, shorten >= 0.3cm, shorten <= 0.3cm] (snowflake client.east) -- (snowflake proxy.west);

    %% Helper lines for debugging.
    %% \node[] at (0.0, 0.0) {X};
    %% \draw[help lines] (-7, -3) grid (7, 3);
\end{tikzpicture}

## Snowflake {.c}

\vspace*{0.9cm}
\centering
\tikzset{external/export next=false}
\begin{tikzpicture}[overlay,scale=1.32]
    %% Define the style for our relay nodes inside the Anonymity Network cloud.
    \tikzstyle{bridge}=[circle, draw, thin, fill=cyan!80, text=white, font=\scriptsize, scale=0.8]
    \tikzstyle{pt}=[rectangle, draw, thin, fill=teal!80, text=white, font=\small, scale=0.8]
    \tikzstyle{broker}=[rectangle, draw, rounded corners, thin, fill=orange!80, text=white, font=\small, scale=0.8]

    %% Clip everything that is outside of our "viewport"
    \clip (-7, -3) rectangle (7, 3);

    %% Our censored area.
    \node[circle, draw=red!40, fill=red!5, thick, dashed, minimum width=50cm] (censored area) at (-20, 0) {};
    \node[font=\footnotesize\bfseries, align=center] at (-4, 2.5) {Censored Region};

    %% Alice.
    \node[font=\small] at (-4, 1.5) {Alice};
    \node[alice, monitor, minimum size=1.2cm] (alice) at (-4, 0) {};

    %% Snowflake PT Client.
    \node[pt, minimum width=3.5cm, rounded corners] (snowflake client) at (-4, -2) {Snowflake PT Client};

    %% Snowflake PT Server.
    \node[pt, minimum width=3.5cm, rounded corners] (snowflake server) at (4, -2) {Snowflake PT Server};

    %% Bridge.
    \node[font=\small] at (4, 1.5) {Bridge};
    \node[bridge, minimum size=2.5cm] (bridge) at (4, 0) {};

    %% Broker.
    \node[broker, minimum width=3cm, minimum height=1.2cm] (snowflake broker) at (0, 1.85) {Snowflake Broker};

    %% Onion connection between Alice and the Snowflake PT Client.
    \draw[<->, thick, OnionDarkPurple!80, shorten >= 0.3cm, shorten <= 0.3cm] (alice.south) -- (snowflake client);

    %% Onion connection between the Snowflake PT server and the bridge.
    \draw[<->, thick, OnionDarkPurple!80, shorten >= 0.3cm, shorten <= 0.3cm] (snowflake server) -- (bridge);

    %% Snowflake
    \node[] (snowflake proxy) at (0, -2) {\includegraphics[angle=0, origin=c]{images/snowflake-status.png}};

    %% Arrow between the Snowflake PT client and the proxy.
    \draw[<->, thick, cyan!80, shorten >= 0.3cm, shorten <= 0.3cm] (snowflake client.east) -- (snowflake proxy.west);

    %% Arrow between the Snowflake proxy and the bridge.
    \draw[<->, thick, teal!80, shorten >= 0.3cm, shorten <= 0.3cm] (snowflake proxy.east) -- (snowflake server.west);

    %% Helper lines for debugging.
    %% \node[] at (0.0, 0.0) {X};
    %% \draw[help lines] (-7, -3) grid (7, 3);
\end{tikzpicture}

## Snowflake {.c}

\centering
\includegraphics[width=1.0\textwidth]{images/snowflake_firefox.png}

## Snowflake {.c}

\begin{itemize}
    \item The Client and Broker component written in Google's Go programming language.
    \item Proxy WebExtension written in JavaScript.
    \item Go version exists of the Proxy for more static deployments.
\end{itemize}

\centering
\large
\url{https://snowflake.torproject.org/}

## Applications Team

The team responsible for the user-facing applications such as Tor Browser.

Works closely with the UX team on analysing and improving the user experience
of our products.

## Tor Browser {.c}

\vspace*{0.9cm}
\centering
\tikzset{external/export next=false}
\begin{tikzpicture}[overlay,scale=1.32]
    %% Clip everything that is outside of our "viewport"
    \clip (-7, -3) rectangle (7, 3);

    %% Firefox
    \node[] (firefox) at (-3, 0) {
        \includegraphics[width=4.5cm, height=4.5cm]{images/firefox_logo.png}
    };

    %% Tor Logo
    \node[] (tor) at (-4.5, 2.2) {
        \includegraphics[height=1.5cm]{images/tor_logo.png}
    };

    %% PT Guy.
    \node[] (pt) at (-1.5, 2.2) {
        \includegraphics[width=2.1cm, height=2.1cm]{images/pt_guy.png}
    };

    %% No Script
    \node[] (noscript) at (-4.5, -2.2) {
        \includegraphics[width=1.5cm, height=1.5cm]{images/noscript_logo.png}
    };

    %% HTTPS Everywhere
    \node[] (https_everywhere) at (-1.5, -2.2) {
        \includegraphics[width=1.5cm, height=1.5cm]{images/https_everywhere_logo.png}
    };

    %% Tor Browser
    \node[] (torbrowser) at (3, 0) {
        \includegraphics[width=5cm, height=5cm]{images/tor_browser_stable_logo.png}
    };

    %% Lines.
    % \begin{pgfonlayer}{background}
    %    \draw[ultra thick] (firefox.center) -- (tor.center);
    %    \draw[ultra thick] (firefox.center) -- (pt.center);
    %    \draw[ultra thick] (firefox.center) -- (noscript.center);
    %    \draw[ultra thick] (firefox.center) -- (https_everywhere.center);
    % \end{pgfonlayer}

    %% Equal sign.
    \node[] at (0, 0) {\Huge $=$};

    %% Helper lines for debugging.
    % \node[] at (0.0, 0.0) {X};
    % \draw[help lines] (-7, -3) grid (7, 3);
\end{tikzpicture}

## Tor Browser

\begin{columns}
    \begin{column}{0.65\textwidth}
            \textbf{Anti-Censorship Team}
                  \begin{itemize}
                      \item FTE.
                      \item Meek.
                      \item Obfs 3 and 4.
                      \item Scramblesuit.
                  \end{itemize}

            \textbf{Applications Team}
                  \begin{itemize}
                      \item Tor Launcher.
                      \item Tor Button.
                  \end{itemize}

            \textbf{Network Team}
                  \begin{itemize}
                      \item Tor ("little-t-tor")
                  \end{itemize}
    \end{column}

    \begin{column}{0.35\textwidth}
        \begin{center}
            \includegraphics[width=0.95\textwidth]{images/tor_browser_stable_logo.png}
        \end{center}
    \end{column}
\end{columns}

## Reproducible Builds

\vspace*{0.9cm}
\centering
\tikzset{external/export next=false}
\begin{tikzpicture}[overlay,scale=1.32]
    %% Clip everything that is outside of our "viewport"
    \clip (-7, -3) rectangle (7, 3);

    \node[] (source) at (-2.5, 1) {
        \Large Source
    };

    \node[] (binary) at (2.5, 1) {
        \Large Binary
    };

    %% Arrow.
    \draw[OONIBlue, ultra thick, ->] (source) -- (binary) node[pos=0.5, below, black] {Build Step};

    %% Helper lines for debugging.
    % \node[] at (0.0, 0.0) {X};
    % \draw[help lines] (-7, -3) grid (7, 3);
\end{tikzpicture}

## Reproducible Builds

\vspace*{0.9cm}
\centering
\tikzset{external/export next=false}
\begin{tikzpicture}[overlay,scale=1.32]
    %% Clip everything that is outside of our "viewport"
    \clip (-7, -3) rectangle (7, 3);

    \node[] (source) at (-2.5, 1) {
        \Large Source
    };

    \node[] (binary) at (2.5, 1) {
        \Large Binary
    };

    \node[text=OnionDarkGray] (verifiable) at (-4.0, -1) {
        Verifiable
    };

    %% Arrow.
    \draw[OONIBlue, ultra thick, ->] (source) -- (binary) node[pos=0.5, below, black] {Build Step};

    \draw[OnionGreen, ultra thick, ->, ] (verifiable) to [out=90, in=180] (source);

    %% Helper lines for debugging.
    % \node[] at (0.0, 0.0) {X};
    % \draw[help lines] (-7, -3) grid (7, 3);
\end{tikzpicture}

## Reproducible Builds

\vspace*{0.9cm}
\centering
\tikzset{external/export next=false}
\begin{tikzpicture}[overlay,scale=1.32]
    %% Clip everything that is outside of our "viewport"
    \clip (-7, -3) rectangle (7, 3);

    \node[] (source) at (-2.5, 1) {
        \Large Source
    };

    \node[] (binary) at (2.5, 1) {
        \Large Binary
    };

    \node[text=OnionDarkGray] (verifiable) at (-4.0, -1) {
        Verifiable
    };

    \node[text=OnionDarkGray] (usable) at (4.0, -1) {
        Usable
    };

    %% Arrow.
    \draw[OONIBlue, ultra thick, ->] (source) -- (binary) node[pos=0.5, below, black] {Build Step};

    \draw[OnionGreen, ultra thick, ->, ] (verifiable) to [out=90, in=180] (source);
    \draw[OnionGreen, ultra thick, ->] (usable) to [out=90, in=0] (binary);

    %% Helper lines for debugging.
    % \node[] at (0.0, 0.0) {X};
    % \draw[help lines] (-7, -3) grid (7, 3);
\end{tikzpicture}

## Reproducible Builds

\vspace*{0.9cm}
\centering
\tikzset{external/export next=false}
\begin{tikzpicture}[overlay,scale=1.32]
    %% Clip everything that is outside of our "viewport"
    \clip (-7, -3) rectangle (7, 3);

    \node[] (source) at (-2.5, 1) {
        \Large Source
    };

    \node[] (binary) at (2.5, 1) {
        \Large Binary
    };

    \node[text=OnionDarkGray] (verifiable) at (-4.0, -1) {
        Verifiable
    };

    \node[text=OnionDarkGray] (usable) at (4.0, -1) {
        Usable
    };

    \node[text=OnionPurple] (question) at (0, -1) {
       \Huge ?
    };

    %% Arrow.
    \draw[OONIBlue, ultra thick, ->] (source) -- (binary) node[pos=0.5, below, black] {Build Step};

    \draw[OnionGreen, ultra thick, ->, ] (verifiable) to [out=90, in=180] (source);
    \draw[OnionGreen, ultra thick, ->] (usable) to [out=90, in=0] (binary);

    \draw[OnionGreen, ultra thick, ->, shorten >= 0.3cm, shorten <= 0.3cm] (question) -- (0, 0.5);

    %% Helper lines for debugging.
    % \node[] at (0.0, 0.0) {X};
    % \draw[help lines] (-7, -3) grid (7, 3);
\end{tikzpicture}

## Other Projects

Unfortunatenly, we don't have time to go over everything we do in the Tor
Project in this talk. We also have teams doing amazing work in areas such as:

\begin{itemize}
    \item Infrastructure.
    \item UX.
    \item Handling metrics in a safe manner.
    \item And much more!
\end{itemize}

## How can you help?

\begin{columns}
    \begin{column}{0.65\textwidth}
        \begin{itemize}
            \item Hack on some of our cool projects.
            \item Find, and maybe fix, bugs in Tor.
            \item Test Tor on your platform of choice.
            \item Work on some of the many open research projects.
            \item Run a Tor relay or a bridge!
            \item Teach others about Tor and privacy in general.
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

\huge Questions?

\vfill

\includegraphics[width=0.4\textwidth]{images/tor_bike.png}

## {.c .plain .noframenumbering}

\centering

This work is licensed under a

\large \href{https://creativecommons.org/licenses/by-sa/4.0/}{Creative Commons \\ Attribution-ShareAlike 4.0 International License}

\vfill

\ccbysa

\vfill
