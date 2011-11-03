# revision 17335
# category Package
# catalog-ctan /macros/latex/contrib/estcpmm
# catalog-date 2010-03-04 23:40:34 +0100
# catalog-license lppl
# catalog-version 0.4
Name:		texlive-estcpmm
Version:	0.4
Release:	1
Summary:	Style for Munitions Management Project Reports
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/estcpmm
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/estcpmm.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/estcpmm.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/estcpmm.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Provides a class which supports typesetting Cost and
Performance Reports and Final Reports for Munitions Management
Reports, US Environmental Security Technology Certification
Program. The class was commissioned and paid for by US Army
Corps of Engineers, Engineer Research and Development Center,
3909 Halls Ferry Road, Vicksburg, MS 39180-6199.

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
%{_texmfdistdir}/tex/latex/estcpmm/estcpmm.cls
%doc %{_texmfdistdir}/doc/latex/estcpmm/README
%doc %{_texmfdistdir}/doc/latex/estcpmm/estcp.pdf
%doc %{_texmfdistdir}/doc/latex/estcpmm/estcpmm.bib
%doc %{_texmfdistdir}/doc/latex/estcpmm/estcpmm.pdf
%doc %{_texmfdistdir}/doc/latex/estcpmm/red_corps_castle2.pdf
%doc %{_texmfdistdir}/doc/latex/estcpmm/sample.pdf
%doc %{_texmfdistdir}/doc/latex/estcpmm/sample.tex
#- source
%doc %{_texmfdistdir}/source/latex/estcpmm/Makefile
%doc %{_texmfdistdir}/source/latex/estcpmm/estcpmm.dtx
%doc %{_texmfdistdir}/source/latex/estcpmm/estcpmm.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
