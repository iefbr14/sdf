use File::ShareDir qw(dist_dir);
use Test::More;

diag dist_dir('My-Dist');

pass;
done_testing;
