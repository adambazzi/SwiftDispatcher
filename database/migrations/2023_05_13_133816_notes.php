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
        Schema::create('notes', function (Blueprint $table) {
            $table->id();

            $table->string('note');

            $table->unsignedBigInteger('medical_record_id');
            $table->unsignedBigInteger('document_id');

            $table->foreign('medical_record_id')->references('id')->on('medical_records');
            $table->foreign('document_id')->references('id')->on('documents');

            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('notes');
    }
};
