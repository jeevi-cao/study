<?php
/**
 * Created by PhpStorm.
 * User: jeevi
 * Date: 2016/10/29
 * Time: 22:48
 */

namespace producer;

use Pheanstalk\Pheanstalk;

require_once (__DIR__."/vendor/autoload.php");


echo "<START ---->".PHP_EOL;

$pheanstalk = new Pheanstalk('127.0.0.1','11300');

$data = ['name' => 'caojianwei','age' => 20];
$pheanstalk
    ->useTube('testtube')
    ->put(json_encode($data));

echo "<END -->".PHP_EOL;




