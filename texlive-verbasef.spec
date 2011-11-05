# revision 21922
# category Package
# catalog-ctan /macros/latex/contrib/verbasef
# catalog-date 2011-04-02 14:59:54 +0200
# catalog-license gpl
# catalog-version 1.1
Name:		texlive-verbasef
Version:	1.1
Release:	1
Summary:	VERBatim Automatic Splitting of External Files
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/verbasef
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verbasef.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/verbasef.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Verbasef allows you to input (subsections of a) file, print
them in verbatim mode, while automatically breaking up the
inputted lines into pieces of a given length, which are output
as figures. These figures are posted using the [H]
specification, which forces LaTeX to place the figure at the
spot of invocation, rather than floating the figures to the top
of the next page. The package requires the verbatim, here and
vrbexin packages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/verbasef/verbasef.sty
%doc %{_texmfdistdir}/doc/latex/verbasef/verbasef-doc.pdf
%doc %{_texmfdistdir}/doc/latex/verbasef/verbasef-doc.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
