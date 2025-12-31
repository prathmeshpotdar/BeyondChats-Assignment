<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('articles', function (Blueprint $table) {
            $table->id();
            $table->string('title'); // The article title
            
            // We use 'longText' to ensure we can store large blog posts
            $table->longText('original_content'); 
            $table->longText('updated_content')->nullable(); 
            
            $table->string('source_url'); // Link to the original BeyondChats blog
            $table->json('references')->nullable(); // Stores the Google links found in Phase 2
            
            $table->timestamps(); // Created_at and Updated_at
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('articles');
    }
};