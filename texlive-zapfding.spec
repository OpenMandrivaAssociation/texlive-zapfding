# revision 31835
# category Package
# catalog-ctan /fonts/urw/base35
# catalog-date 2012-06-06 22:57:48 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-zapfding
Version:	20140418
Release:	2
Summary:	URW "Base 35" font pack for LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/urw/base35
License:	GPL
Source0:	http://mirror.macomnet.net/pub/CTAN/systems/texlive/tlnet/archive/zapfding.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: - Century Schoolbook (substituting for
Adobe's New Century Schoolbook); - Dingbats (substituting for
Adobe's Zapf Dingbats); - Nimbus Mono L (substituting for
Abobe's Courier); - Nimbus Roman No9 L (substituting for
Adobe's Times); - Nimbus Sans L (substituting for Adobe's
Helvetica); - Standard Symbols L (substituting for Adobe's
Symbol); - URW Bookman; - URW Chancery L Medium Italic
(substituting for Adobe's Zapf Chancery); - URW Gothic L Book
(substituting for Adobe's Avant Garde); and - URW Palladio L
(substituting for Adobe's Palatino).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/zapfding/config.uzd
%{_texmfdistdir}/fonts/afm/adobe/zapfding/pzdr.afm
%{_texmfdistdir}/fonts/afm/urw/zapfding/uzdr.afm
%{_texmfdistdir}/fonts/map/dvips/zapfding/uzd.map
%{_texmfdistdir}/fonts/tfm/adobe/zapfding/pzdr.tfm
%{_texmfdistdir}/fonts/tfm/urw35vf/zapfding/uzdr.tfm
%{_texmfdistdir}/fonts/type1/urw/zapfding/uzdr.pfb
%{_texmfdistdir}/fonts/type1/urw/zapfding/uzdr.pfm
%{_texmfdistdir}/tex/latex/zapfding/uuzd.fd

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts tex %{buildroot}%{_texmfdistdir}
