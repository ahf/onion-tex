---
title: Browsing the Web Securely with Tor
date: March 5, 2020
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
                  Team Lead of the Network Team since late 2019.
            \item Free Software developer since 2006.
            \item Worked with distributed systems in the Erlang programming
                  language, WebKit-based mobile browsers, embedded
                  development, and software development consulting.
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

**2007**
  : Expansion to anti-censorship.

**2008**
  : \highlight{Tor Browser development.}

**2010**
  : The Arab spring.

**2013**
  : The summer of Snowden.

**2018**
  : Anti-censorship team created.

**2019**
  : \highlight{Tor Browser for Android released.}

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
    \node[at=(current page.center)] {\includegraphics[scale=0.15]{images/tor_browser_android_shadow.png}};
\end{tikzpicture}

## {.plain}

\tikzset{external/export next=false}
\begin{tikzpicture}[remember picture,overlay, background rectangle/.style={fill=OnionDarkPurple}, show background rectangle]
    \node[at=(current page.center)] {\includegraphics[scale=0.15]{images/tor_browser_android_shadow2.png}};
\end{tikzpicture}

## Tor Releases {.c}

\centering

\small\begin{tabular}{lllll}
\toprule
\textbf{Version} & \textbf{Merge Window} & \textbf{Feature Freeze} & \textbf{Release} & \textbf{End of Life} \\
\midrule
0.3.5 (\alert{LTS}) &  15/6/2018 & 15/9/2018 &  7/1/2019 &  1/2/2022 \\
0.4.0               & 15/10/2018 & 15/1/2019 &  2/5/2019 &  2/2/2020 \\
0.4.1               &  15/2/2018 & 15/5/2019 & 20/8/2019 & 20/5/2020 \\
0.4.2               &  10/6/2019 & 15/9/2019 & 9/12/2019 & 15/9/2022 \\
0.4.3               & 11/10/2019 & 15/1/2020 & 15/4/2020 & TBD       \\
\midrule
0.4.4               &  15/2/2020 & 15/5/2020 & 15/8/2020  & TBD      \\
0.4.5               &  15/6/2020 & 15/9/2020 & 15/12/2020 & TBD      \\
\hline
\end{tabular}

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

## {.plain}

\tikzset{external/export next=false}
\begin{tikzpicture}[remember picture,overlay, background rectangle/.style={fill=OnionDarkPurple}, show background rectangle]
    \node[at=(current page.center)] {\includegraphics[scale=0.25]{images/tor_browser_circuit.png}};
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

## Tor Browser

The philosophy behind the design choices in Tor Browser:

\begin{itemize}
    \item Preserve existing user model.
    \item Favor changes that are least likely to break sites.
    \item Plugins must be restricted.
    \item Minimize Global Privacy Options.
    \item No filters.
    \item Stay current.
\end{itemize}

## Tor Browser

The security requirements are primarily concerned with ensuring the safe use of Tor.

\begin{itemize}
    \item Proxy Obedience.
    \item State Separation.
    \item Disk Avoidance.
    \item Application Data Isolation.
\end{itemize}

## {.plain}

\tikzset{external/export next=false}
\begin{tikzpicture}[remember picture,overlay, background rectangle/.style={fill=OnionDarkPurple}, show background rectangle]
    \node[at=(current page.center)] {\includegraphics[scale=0.30]{images/tor_browser_security.png}};
\end{tikzpicture}

## Tor Browser

Focus on strong privacy protection:

\begin{itemize}
    \item Cross-Origin Identifier Unlinkability.
    \item Cross-Origin Fingerprinting Unlinkability.
    \item Long-Term Unlinkability.
\end{itemize}

## {.plain}

\tikzset{external/export next=false}
\begin{tikzpicture}[remember picture, overlay, background rectangle/.style={fill=OnionDarkPurple}, show background rectangle]
    \node[text=white, at=(current page.center), font=\bfseries\footnotesize] {\texttt{Mozilla/5.0 (Windows NT 6.1; rv:60.0) Gecko/20100101 Firefox/60.0}};
\end{tikzpicture}

## Tor Browser

\begin{columns}
    \begin{column}{0.5\textwidth}
        \begin{center}
            \includegraphics[width=0.95\textwidth]{images/fingerprint-firefox.png}
            Firefox 60
        \end{center}
    \end{column}

    \begin{column}{0.5\textwidth}
        \begin{center}
            \includegraphics[width=0.95\textwidth]{images/fingerprint-tor.png}
            Tor Browser
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

## Build Process {.t}

\centering
\begin{tikzpicture}
    \tikzstyle{build step}=[rectangle, minimum height=0.8cm, minimum width=2cm, draw, thin, fill=OnionDarkPurple!80, text=white, font=\small, scale=0.8]

    %% Alice.
    \node[alice, monitor, minimum size=1.25cm] (alice) at (-6.5, 0.5) {};

    \node[build step, minimum width=2cm, rounded corners] (fetch step) at (-4, 0)   { Fetch };
    \node[build step, minimum width=2cm, rounded corners] (verify step) at (-2, 0)  { Verify };
    \node[build step, minimum width=2cm, rounded corners] (build step) at (0, 0)    { Build };
    \node[build step, minimum width=2cm, rounded corners] (sign step) at (2, 0)     { Sign };
    \node[build step, minimum width=2cm, rounded corners] (publish step) at (4, 0)  { Publish };

    \draw[OnionGreen, ultra thick, ->, shorten >= 0.1cm, shorten <= 0.1cm] (alice.south east) to [out=270, in=270] (fetch step);
    \draw[OnionGreen, ultra thick, ->, shorten >= 0.1cm, shorten <= 0.1cm] (fetch step) to [out=90, in=90] (verify step);
    \draw[OnionGreen, ultra thick, ->, shorten >= 0.1cm, shorten <= 0.1cm] (verify step) to [out=270, in=270] (build step);
    \draw[OnionGreen, ultra thick, ->, shorten >= 0.1cm, shorten <= 0.1cm] (build step) to [out=90, in=90] (sign step);
    \draw[OnionGreen, ultra thick, ->, shorten >= 0.1cm, shorten <= 0.1cm] (sign step) to [out=270, in=270] (publish step);

    %% Helper lines for debugging.
    %% \draw[help lines] (-7,-3) grid (7,3);
\end{tikzpicture}

## Build Process {.t}

\centering
\begin{tikzpicture}
    \tikzstyle{build step}=[rectangle, minimum height=0.8cm, minimum width=2cm, draw, thin, fill=OnionDarkPurple!80, text=white, font=\small, scale=0.8]

    %% Alice.
    \node[alice, monitor, minimum size=1.25cm] (alice) at (-6.5, 0.5) {};

    %% Adversary.
    \node[maninblack, monitor, minimum size=1.25cm] (adversary) at (1.5, -2.5) {};

    \node[build step, minimum width=2cm, rounded corners] (fetch step) at (-4, 0)   { Fetch };
    \node[build step, minimum width=2cm, rounded corners] (verify step) at (-2, 0)  { Verify };
    \node[build step, minimum width=2cm, rounded corners, fill=red!50, text=black] (build step) at (0, 0)    { Build };
    \node[build step, minimum width=2cm, rounded corners] (sign step) at (2, 0)     { Sign };
    \node[build step, minimum width=2cm, rounded corners] (publish step) at (4, 0)  { Publish };

    \draw[OnionGreen, ultra thick, ->, shorten >= 0.1cm, shorten <= 0.1cm] (alice.south east) to [out=270, in=270] (fetch step);
    \draw[OnionGreen, ultra thick, ->, shorten >= 0.1cm, shorten <= 0.1cm] (fetch step) to [out=90, in=90] (verify step);
    \draw[OnionGreen, ultra thick, ->, shorten >= 0.1cm, shorten <= 0.1cm] (verify step) to [out=270, in=270] (build step);
    \draw[OnionGreen, ultra thick, ->, shorten >= 0.1cm, shorten <= 0.1cm] (build step) to [out=90, in=90] (sign step);
    \draw[OnionGreen, ultra thick, ->, shorten >= 0.1cm, shorten <= 0.1cm] (sign step) to [out=270, in=270] (publish step);

    \path[ultra thick, ->, red!50, bend right, shorten >= 0.1cm, shorten <= 0.1cm] (adversary.north) edge (build step);

    %% Helper lines for debugging.
    %% \draw[help lines] (-7,-3) grid (7,3);
\end{tikzpicture}

## Build Process {.t}

\centering
\begin{tikzpicture}
    \tikzstyle{build step}=[rectangle, minimum height=0.8cm, minimum width=2cm, draw, thin, fill=OnionDarkPurple!80, text=white, font=\small, scale=0.8]

    %% Alice.
    \node[alice, monitor, minimum size=1.25cm] (alice) at (-6.5, 0.0) {};

    \node[build step, rounded corners] (alice fetch step) at (-4, -0.5)   { Fetch };
    \node[build step, rounded corners] (alice verify step) at (-2, -0.5)  { Verify };
    \node[build step, rounded corners] (alice build step) at (0, -0.5)    { Build };

    \node[bob, monitor, minimum size=1.25cm] (bob) at (-6.5, -2.5) {};
    \node[build step, rounded corners] (bob fetch step) at (-4, -3)   { Fetch };
    \node[build step, rounded corners] (bob verify step) at (-2, -3)  { Verify };
    \node[build step, rounded corners] (bob build step) at (0, -3)    { Build };

    \node[builder, female, monitor, minimum size=1.25cm] (builder) at (-6.5, -5.0) {};
    \node[build step, rounded corners] (builder fetch step) at (-4, -5.5)   { Fetch };
    \node[build step, rounded corners] (builder verify step) at (-2, -5.5)  { Verify };
    \node[build step, rounded corners] (builder build step) at (0, -5.5)    { Build };

    \draw[OnionGreen, ultra thick, ->, shorten >= 0.1cm, shorten <= 0.1cm] (alice.south east) to [out=270, in=270] (alice fetch step);
    \draw[OnionGreen, ultra thick, ->, shorten >= 0.1cm, shorten <= 0.1cm] (alice fetch step) to [out=90, in=90] (alice verify step);
    \draw[OnionGreen, ultra thick, ->, shorten >= 0.1cm, shorten <= 0.1cm] (alice verify step) to [out=270, in=270] (alice build step);

    \draw[OnionGreen, ultra thick, ->, shorten >= 0.1cm, shorten <= 0.1cm] (bob.south east) to [out=270, in=270] (bob fetch step);
    \draw[OnionGreen, ultra thick, ->, shorten >= 0.1cm, shorten <= 0.1cm] (bob fetch step) to [out=90, in=90] (bob verify step);
    \draw[OnionGreen, ultra thick, ->, shorten >= 0.1cm, shorten <= 0.1cm] (bob verify step) to [out=270, in=270] (bob build step);

    \draw[OnionGreen, ultra thick, ->, shorten >= 0.1cm, shorten <= 0.1cm] (builder.south east) to [out=270, in=270] (builder fetch step);
    \draw[OnionGreen, ultra thick, ->, shorten >= 0.1cm, shorten <= 0.1cm] (builder fetch step) to [out=90, in=90] (builder verify step);
    \draw[OnionGreen, ultra thick, ->, shorten >= 0.1cm, shorten <= 0.1cm] (builder verify step) to [out=270, in=270] (builder build step);

    \node[build step, minimum width=2cm, rounded corners] (verify build step) at (4, -3)     { Verify };

    \draw[OnionGreen, ultra thick, ->, shorten >= 0.3cm, shorten <= 0.3cm] (alice build step) to (verify build step);
    \draw[OnionGreen, ultra thick, ->, shorten >= 0.3cm, shorten <= 0.3cm] (bob build step) to (verify build step);
    \draw[OnionGreen, ultra thick, ->, shorten >= 0.3cm, shorten <= 0.3cm] (builder build step) to (verify build step);

    %% Helper lines for debugging.
    %% \draw[help lines] (-7,-3) grid (7,3);
\end{tikzpicture}

## Reproducible Builds

\begin{columns}
    \begin{column}{0.3\textwidth}
        \centering
        \includegraphics[width=0.8\textwidth]{images/bitcoin_logo.png}
    \end{column}

    \begin{column}{0.3\textwidth}
        \centering
        \includegraphics[width=0.8\textwidth]{images/tor_logo.png}
    \end{column}

    \begin{column}{0.3\textwidth}
        \centering
        \includegraphics[width=0.8\textwidth]{images/debian_logo.png}
    \end{column}
\end{columns}

## Reproducible Builds Workflow

\centering\includegraphics[width=0.85\textwidth]{images/29510.png}

## Reproducible Builds Workflow

\centering\includegraphics[width=0.98\textwidth]{images/29510_c2.png}

## Reproducible Builds Workflow

\lstinputlisting[language=diff]{listings/diffoscope_1.txt}

## Reproducible Builds Workflow

\lstinputlisting[language=diff]{listings/diffoscope_strtab.txt}

## Reproducible Builds Workflow

\lstinputlisting[language=diff]{listings/diffoscope_comment.txt}

## Tor is not foolproof

- Browser metadata fingerprinting.
- Browser exploits.
- Traffic analysis.
- Operational security mistakes.

## How can you help?

\centering
Help test our Alpha releases

\vfill

\begin{columns}
    \begin{column}{0.5\textwidth}
        \centering
        \includegraphics[width=0.6\textwidth]{images/tor_browser_logo_alpha.png}
    \end{column}

    \begin{column}{0.5\textwidth}
        \centering
        \includegraphics[width=0.6\textwidth]{images/tor_browser_logo_nightly.png}
    \end{column}
\end{columns}

\vfill

\large\href{https://www.torproject.org/download/alpha/}{torproject.org/download/alpha/}

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

\huge Questions?

\vfill

\normalsize

\begin{columns}
    \begin{column}{0.60\textwidth}
        \begin{itemize}
            \setlength\itemsep{0.75em}

            \item[\faTwitter] \colorhref{https://twitter.com/ahfaeroey}{@ahfaeroey}
            \item[\faEnvelope] \colorhref{mailto:ahf@torproject.org}{ahf@torproject.org}
            \item[\faKey] OpenPGP: \\ \texttt{1C1B C007 A9F6 07AA 8152} \\ \texttt{C040 BEA7 B180 B149 1921}
        \end{itemize}
    \end{column}

    \begin{column}{0.40\textwidth}
        \begin{center}
            \includegraphics[width=0.95\textwidth]{images/tor_bike.png}
        \end{center}
    \end{column}
\end{columns}

## {.c .plain .noframenumbering}

\centering

This work is licensed under a

\large \href{https://creativecommons.org/licenses/by-sa/4.0/}{Creative Commons \\ Attribution-ShareAlike 4.0 International License}

\vfill

\ccbysa

\vfill
