%global tl_name verbasef
%global tl_revision 21922

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	VERBatim Automatic Splitting of External Files
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/verbasef
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/verbasef.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/verbasef.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows you to input (subsections of a) file, print them in
verbatim mode, while automatically breaking up the input lines into
pieces of a given length, which are output as figures. These figures are
posted using the [H] specification, which forces LaTeX to place the
figure at the spot of invocation, rather than floating the figures to
the top of the next page. The package requires the verbatim, here and
vrbexin packages.

