Name:		texlive-verbasef
Version:	21922
Release:	1
Summary:	VERBatim Automatic Splitting of External Files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/verbasef
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verbasef.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verbasef.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Verbasef allows you to input (subsections of a) file, print
them in verbatim mode, while automatically breaking up the
inputted lines into pieces of a given length, which are output
as figures. These figures are posted using the [H]
specification, which forces LaTeX to place the figure at the
spot of invocation, rather than floating the figures to the top
of the next page. The package requires the verbatim, here and
vrbexin packages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/verbasef/verbasef.sty
%doc %{_texmfdistdir}/doc/latex/verbasef/verbasef-doc.pdf
%doc %{_texmfdistdir}/doc/latex/verbasef/verbasef-doc.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
