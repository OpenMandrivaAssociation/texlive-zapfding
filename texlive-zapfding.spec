%global tl_name zapfding
%global tl_revision 77161

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	URW Base 35 font pack for LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/urw/base35
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/zapfding.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
A set of fonts for use as "drop-in" replacements for Adobe's basic set,
comprising: Century Schoolbook (substituting for Adobe's New Century
Schoolbook); Dingbats (substituting for Adobe's Zapf Dingbats); Nimbus
Mono L (substituting for Adobe's Courier); Nimbus Roman No9 L
(substituting for Adobe's Times); Nimbus Sans L (substituting for
Adobe's Helvetica); Standard Symbols L (substituting for Adobe's
Symbol); URW Bookman; URW Chancery L Medium Italic (substituting for
Adobe's Zapf Chancery); URW Gothic L Book (substituting for Adobe's
Avant Garde); and URW Palladio L (substituting for Adobe's Palatino).


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from zapfding:
Map uzd.map
TL_DROPIN_EOF
