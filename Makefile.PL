
require 5.004;  # make sure perl version is at least 5.004

if (defined $ENV{SDFHOME}) {
	warn <<EOT;

	The environment variable SDFHOME is defined as

		$ENV{SDFHOME}

	Since SDF 2.000, SDF is installed into the perl library
	tree.  Please remove the SDFHOME definition or make
	sure that only your private addition are there.

EOT
}

use ExtUtils::MakeMaker;
#use File::ShareDir::Install;

WriteMakefile(
	NAME		=> 'SDF',
	ABSTRACT	=> 'Simple Document Formatter',
	DISTNAME	=> 'sdf',
	VERSION		=> '2.2.0',
	AUTHOR		=> q{Drew Sullivan <drew@ss.org>},

#	LICENSE		=> 'Artistic_2_0',

#	CPANID		=> 'DSULLIVAN',
#	ORGANIZATION	=> 'Systems Software',
#	WEBSITE		=> 'http://www.ss.org/sdf',


	MIN_PERL_VERSION => 5.006,

#	'DIR'		=> [ qw(bin lib) ],
	EXE_FILES => [ qw(
		bin/mkpldocs
		bin/pod2sdf
		bin/poddiff
		bin/sdf
		bin/sdfapi
		bin/sdfcli
		bin/sdfget
	) ],


	'dist'          => {'COMPRESS'=>'gzip -9f', 'SUFFIX'=>'.gz'},

	PREREQ_PM    => {
			# if you need an earlier version let me know
#			'File::ShareData' => 1.00,
#			'File::ShareData::Install' => 1.00,
			'Test::Harness' => 3.00,
			'Test::Simple' => 0.44,
                    },


#MAN1PODS            => {
#    'doc/command.pod'    => 'blib/man1/command.1',
#    'scripts/script.pl'  => 'blib/man1/script.1',
#  }
	);

#install_share 'share';

package MY;

#use File::ShareDir::Install qw(postamble);

# What happens when we say 'make test'
# Copied libwww Makefile.PL
sub test {
    q(
TEST_VERBOSE=0

test: all
	$(FULLPERL) t/TEST $(TEST_VERBOSE)

);
}

# Use t/sdftest for test target
#sub test
#{
#    q(
#TEST_VERBOSE=0
#
#test: all
#	cd t && ./sdftest $(FULLPERL)
#
#);
#}

