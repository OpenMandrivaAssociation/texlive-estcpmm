Name:		texlive-estcpmm
Version:	17335
Release:	2
Summary:	Style for Munitions Management Project Reports
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/estcpmm
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/estcpmm.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/estcpmm.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/estcpmm.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides a class which supports typesetting Cost and
Performance Reports and Final Reports for Munitions Management
Reports, US Environmental Security Technology Certification
Program. The class was commissioned and paid for by US Army
Corps of Engineers, Engineer Research and Development Center,
3909 Halls Ferry Road, Vicksburg, MS 39180-6199.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
