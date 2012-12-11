%define	rname	actionpack

Summary:	Part of Rails framework handling controller/view split
Name:		ruby-%{rname}
Version:	3.2.3
Release:	1
URL:		http://www.rubyonrails.com/
Source0:	http://rubygems.org/gems/%{rname}-%{version}.gem
License:	MIT
Group:		Development/Ruby
BuildArch:	noarch
BuildRequires:	ruby-RubyGems 

%description
Action Pack splits the response to a web request into a controller part
(performing the logic) and a view part (rendering a template). This two-step
approach is known as an action, which will normally create, read, update, or
delete (CRUD for short) some sort of model part (often backed by a database)
before choosing either to render a template or redirecting to another action.

Action Pack implements these actions as public methods on Action Controllers
and uses Action Views to implement the template rendering. Action Controllers
are then responsible for handling all the actions relating to a certain part
of an application. This grouping usually consists of actions for lists and for
CRUDs revolving around a single (or a few) model objects. So ContactController
would be responsible for listing contacts, creating, deleting, and updating
contacts. A WeblogController could be responsible for both posts and comments.

Action View templates are written using embedded Ruby in tags mingled in with
the HTML. To avoid cluttering the templates with code, a bunch of helper
classes provide common behavior for forms, dates, and strings. And it's easy
to add specific helpers to keep the separation as the application evolves.

Note: Some of the features, such as scaffolding and form building, are tied to
ActiveRecord[http://activerecord.rubyonrails.org] (an object-relational
mapping package), but that doesn't mean that Action Pack depends on Active
Record. Action Pack is an independent package that can be used with any sort
of backend (Instiki[http://www.instiki.org], which is based on an older version
of Action Pack, used Madeleine for example). Read more about the role Action
Pack can play when used together with Active Record on
http://www.rubyonrails.org.

%prep

%build

%install
rm -rf %buildroot
gem install -E -n %{buildroot}%{_bindir} --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

rm -rf %{buildroot}%{ruby_gemdir}/cache
chmod g-w,g+r,o+r -R %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{rname}-%{version}
%{ruby_gemdir}/gems/%{rname}-%{version}
%{ruby_gemdir}/specifications/%{rname}-%{version}.gemspec


%changelog
* Wed Apr 25 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 3.2.3-1
+ Revision: 793332
- update to 3.2.3

* Wed Feb 15 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.2.1-2
+ Revision: 774161
- mass rebuild of ruby packages against ruby 1.9.1

* Mon Jan 30 2012 Crispin Boylan <crisb@mandriva.org> 3.2.1-1
+ Revision: 769661
- New release

* Tue Mar 15 2011 Rémy Clouard <shikamaru@mandriva.org> 2.3.11-1
+ Revision: 645162
- new version 2.3.11

* Thu Dec 09 2010 Rémy Clouard <shikamaru@mandriva.org> 2.3.10-2mdv2011.0
+ Revision: 618261
- add provides to fix rails dependencies

* Fri Oct 15 2010 Rémy Clouard <shikamaru@mandriva.org> 2.3.10-1mdv2011.0
+ Revision: 585833
- bump release & fix url

* Sat Sep 18 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 2.3.9-1mdv2011.0
+ Revision: 579505
- new release: 2.3.9

* Sun Sep 13 2009 Frederik Himpe <fhimpe@mandriva.org> 2.3.4-1mdv2010.0
+ Revision: 438624
- Update to new version 2.3.4

* Wed Jul 29 2009 Frederik Himpe <fhimpe@mandriva.org> 2.3.3-1mdv2010.0
+ Revision: 404439
- Update to new version 2.3.3

* Fri Jun 12 2009 Lev Givon <lev@mandriva.org> 2.1.2-1mdv2010.0
+ Revision: 385324
- Update to 2.1.2.

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 2.1.0-2mdv2009.0
+ Revision: 269227
- rebuild early 2009.0 package (before pixel changes)

* Tue Jun 03 2008 Alexander Kurtakov <akurtakov@mandriva.org> 2.1.0-1mdv2009.0
+ Revision: 214639
- new version 2.1.0

* Mon Jan 14 2008 Alexander Kurtakov <akurtakov@mandriva.org> 2.0.2-1mdv2008.1
+ Revision: 151329
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Apr 23 2007 Olivier Blin <blino@mandriva.org> 1.13.3-1mdv2008.0
+ Revision: 17565
- 1.13.3
- drop Patch0 (fixed upstream)

* Sat Apr 21 2007 Pascal Terjan <pterjan@mandriva.org> 1.12.5-2mdv2008.0
+ Revision: 16670
- ri is now in ri/ and not ri/ri/
- Use Development/Ruby group


* Thu Nov 16 2006 Olivier Blin <oblin@mandriva.com> 1.12.5-1mdv2007.0
+ Revision: 84899
- Patch0: fix rdoc generation (from upstream trac)
- 1.12.5
- Import ruby-actionpack

* Sat Jul 29 2006 Olivier Blin <blino@mandriva.com> 1.12.3-1mdv2007.0
- 1.12.3

* Mon Feb 13 2006 Pascal Terjan <pterjan@mandriva.org> 1.11.2-3mdk
- Ship the gemspec

* Mon Feb 13 2006 Pascal Terjan <pterjan@mandriva.org> 1.11.2-2mdk
- Don't ship too much ri, else we get conflicts

* Sun Feb 12 2006 Pascal Terjan <pterjan@mandriva.org> 1.11.2-1mdk
- First Mandriva release

