<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Article extends Model
{
    use HasFactory;
    
    protected $fillable = [
        'title', 
        'original_content', 
        'updated_content', 
        'source_url', 
        'references'
    ];

    protected $casts = [
        'references' => 'array',
    ];
}